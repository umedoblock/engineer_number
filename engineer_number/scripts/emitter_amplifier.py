# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

import os
import sys
import math, argparse

import lib
lib.init_engineer_number()

from engineer_number import EngineerNumber
from engineer_number.constants import *
from engineer_number.lib import get_resistors, close_e_series

NAMES = ("Rb1", "Rb2", "Rc", "Re", "gain", "Vcc", "Vcb", "Vb", "Vc", "Ve", "Vce", "ie", "ic", "ib", "ibias", "Pce")

class EmitterCommonAmp(object):
    def __init__(self, **kwds):
        for key, value in kwds.items():
            setattr(self, key, value)

def _emitter_common_amplifier(Vcc, ic, hfe, Rc, Re, e_series):
    ib = ic / hfe # ?
    ie = ic + ib
    Vc = Rc * ic   # 6
    Ve = Re * ie

    # 注意
    # must be Vc + Ve <= Vcc
    if Vc + Ve > Vcc:
      # raise ValueError("invalid Vc and Ve combination compare Vcc.")
      # print("added(Vc={}, Ve={})={} is greater ghan Vcc={}.".format(Vc, Ve, Vc + Ve, Vcc))
        return None

    Vce = Vcc - (Vc + Ve) # 7
    gain = Vc / Ve
    Pce = Vce * ic        # 8
    # Pce は小さきこと。
    # 2SC1815 の場合，
    # Pce < 400mW(=PD)

    Vb = Ve + 0.6 # 9
    Vcb = Vcc - Vb

    # hfe = 200 # 10
    ibias = 10 * ib # 11
    Rb2 = Vb / ibias # 12
    Rb1 = Vcb / ibias # 13
    Rb2_ = close_e_series(Rb2, "down", e_series)
    Rb1_ = close_e_series(Rb1, "down", e_series)
    Rb2, Rb1 = Rb2_, Rb1_
    if (not Rb2) or (not Rb1):
#       print("--")
#       print("Rb2={}, Rb2_={}".format(Rb2, Rb2_))
#       print("Rb1={}, Rb1_={}".format(Rb1, Rb1_))
        return None
    Radd = Rb1 + Rb2
    ibias = Vcc / Radd

    kwds = {}
    for name in NAMES:
        kwds[name] = locals()[name]
    eca = EmitterCommonAmp(**kwds)
    return eca

def brute_force_to_look_for_gain_and_Pce(Vcc, ic, hfe, e_series):
    resistors = get_resistors(e_series)
    parameters = [None] * len(resistors) ** 2

    i = 0
    for Rc in resistors:
        for Re in resistors:
            eca = _emitter_common_amplifier(Vcc, ic, hfe, Rc, Re, e_series)
            if eca:
                parameters[i] = eca
                i += 1

    return parameters[:i]

def look_for_optimized_gain(gain, ic, Vcc, hfe=200, e_series="E12", orders=ORDERS_KILO):
    resistors = get_resistors(e_series, ORDERS_RESISTOR)

    gain_ = gain
    parameters = []
#   print("resistors =", resistors)
    for Rc in resistors:
        d = {}
        ie = ic + ic / hfe

        Vc = Rc * ic   # 6
        Re = Rc / gain_

        Re_ = close_e_series(Re, "up", e_series, orders)
        if not Re_:
            continue

        Re = Re_
        Ve = Re * ie

        # 注意
        # must be Vc + Ve <= Vcc
        if Vc + Ve > Vcc:
          # raise ValueError("invalid Vc and Ve combination compare Vcc.")
          # print("added(Vc={}, Ve={})={} is greater ghan Vcc={}.".format(Vc, Ve, Vc + Ve, Vcc))
            continue

        gain = Vc / Ve

        Vce = Vcc - (Vc + Ve) # 7

        Pce = Vce * ic        # 8
        # Pce は小さきこと。
        # 2SC1815 の場合，
        # Pce < 400mW(=PD)

        Vb = Ve + 0.6 # 9
        Vcb = Vcc - Vb

        # hfe = 200 # 10
        ib = ic / hfe # ?
        ibias = 10 * ib # 11

        Rb2 = Vb / ibias # 12
        Rb1 = Vcb / ibias # 13
        Rb2_ = close_e_series(Rb2, "down", e_series, orders)
        Rb1_ = close_e_series(Rb1, "down", e_series, orders)
        Rb2, Rb1 = Rb2_, Rb1_
        if (not Rb2) or (not Rb1):
#           print("--")
#           print("Rb2={}, Rb2_={}".format(Rb2, Rb2_))
#           print("Rb1={}, Rb1_={}".format(Rb1, Rb1_))
            continue

        Radd = Rb1 + Rb2
      # print("Radd =", Radd)

        ibias = Vcc / Radd

        kwds = {}
        for name in NAMES:
            kwds[name] = locals()[name]
        eca = EmitterCommonAmp(**kwds)

        parameters.append(eca)

    parameters.sort(key=lambda parameter: math.fabs(gain_ - parameter.gain))
#   print("parameters =")
#   print(parameters)
    return parameters

def view_apmlifiered(gained, top=-1):
    fmt = ", ".join(["{!s:>8s}"] * len(NAMES))

    print(fmt.format(*NAMES))
    for eca in gained[:top]:
        tup = (getattr(eca, name) for name in NAMES)
        print(fmt.format(*tup))

def parse_args():
    parser = argparse.ArgumentParser(description=_("look for optimized Hz."))

    parser.add_argument("--gain", metavar="N", dest="gain",
                       type=float, nargs="?", default=5,
                       help="gain default: 5")
    parser.add_argument("--Vcc", metavar="N", dest="Vcc",
                       type=float, nargs="?", default=5.0,
                       help="Vcc default: 5.0")
    parser.add_argument("--ic", metavar="N", dest="ic",
                       nargs="?", default=EngineerNumber("0.8m"),
                       help="collect i default: 0.8m")
    parser.add_argument("--e_series", metavar="N", dest="e_series",
                       nargs="?", default="E12",
                       help="e_series default: E12")
    parser.add_argument("--hfe", metavar="N", dest="hfe",
                       type=int, nargs="?", default=200,
                       help="hfe default: 200")
    parser.add_argument("--top", metavar="N", dest="top",
                       type=int, nargs="?", default=10,
                       help="ranking default: 10")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()

    ic = EngineerNumber(args.ic)
    Vcc = EngineerNumber(args.Vcc)
    gain = args.gain
    top = args.top
    hfe = args.hfe
    e_series = args.e_series

  # parameters = brute_force_to_look_for_gain_and_Pce(Vcc, ic, hfe, e_series)
  # parameters.sort(key=lambda parameter: parameter.gain, reverse=True)
  # parameters.sort(key=lambda parameter: abs(10 - parameter.gain))
  # parameters.sort(key=lambda parameter: parameter.Pce)
  # parameters.sort(key=lambda parameter: \
  #     math.fabs(EngineerNumber("1m") - parameter.Ve))
  # parameters.sort(key=lambda parameter: \
  #     math.fabs(EngineerNumber("100m") - parameter.Vc))

    parameters = look_for_optimized_gain(gain, ic, Vcc, hfe, e_series)

    view_apmlifiered(parameters, top)

    print()
