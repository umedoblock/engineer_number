# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

import os, sys, math
import argparse, gettext
from itertools import *

import lib
lib.init_engineer_number()
from engineer_number import *
from engineer_number.constants import *
from engineer_number.lib import get_resistors, get_capacitors

# >>> math.log(2)
# 0.6931471805599453
# >>> math.log(2, math.e)
# 0.6931471805599453
# >>> math.log(8, 2) # swaped math logarithm
# 3.0 # 2 ** 3 = 8, pow(2, 3)

NAMES = ("duty", "t", "f", "rc", "c")

class LMC555(object):
    def __init__(self, **kwds):
        for key, value in kwds.items():
            setattr(self, key, value)

def lmc555_fifty_duty(Rc, C=EngineerNumber("0.1u")):
    # FIGURE 12. 50% Duty Cycle Oscillator.
    t = math.log(2, math.e) * Rc * C
    f = 1 / t

    return t, f

# esn means e_series_name
def brute_force_LMC555(resistor_e_sesires, capacitor_e_sesires):
    resistors = get_resistors(resistor_e_sesires, ORDERS_RESISTOR)
    capacitors = get_capacitors(capacitor_e_sesires, ORDERS_CAPACITOR)

    len_combinations = len(resistors) * len(capacitors)

  # print("len(resistors) =", len(resistors))
  # print("len(capacitors) =", len(capacitors))
  # print("len_combinations =", len_combinations)

    tf = [None] * len_combinations
    i = 0
    for rc, c in product(resistors, capacitors):
        t, f = lmc555_fifty_duty(rc, c)

        duty = EngineerNumber("0.5")

        kwds = {}
        for name in NAMES:
            kwds[name] = locals()[name]
        l555 = LMC555(**kwds)
        tf[i] = l555
        i += 1
    tf = tf[:i]

    return tf

def look_for_fifty_duty_Hz(parameters, Hz):
    parameters.sort(key=lambda parameter: math.fabs(Hz - parameter.f))
    return parameters

def parse_args():
    parser = argparse.ArgumentParser(description=_("look for optimized Hz."))

    parser.add_argument("--Hz", metavar="f", dest="Hz",
                       default=1000,
                       type=EngineerNumber,
                       help="frequency default: 1000")
    parser.add_argument("--top", metavar="t", dest="top",
                       type=int, default=10,
                       help="ranking default: 10")
    args = parser.parse_args()
    return args

def view_tf(tf, top=-1):
    fmt = ", ".join(["{!s:>8s}"] * len(NAMES))

    print(fmt.format(*NAMES))
    for lmc555 in tf[:top]:
        tup = (getattr(lmc555, name) for name in NAMES)
        print(fmt.format(*tup))

if __name__ == "__main__":
    args = parse_args()

    parameters = brute_force_LMC555("E12", "E6")

    tf = look_for_fifty_duty_Hz(parameters, EngineerNumber(args.Hz))

  # print("len(tf)=", len(tf))
  # print()
    top = args.top
    view_tf(tf, top)
    print()
