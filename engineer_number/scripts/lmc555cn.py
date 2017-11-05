# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

import math, argparse
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
CONST = math.log(2, math.e)

NAMES = ("tL", "tH", "t", "dutyL", "dutyH", "f", "ra", "rb", "c")

class LMC555(object):
    def __init__(self, **kwds):
        for key, value in kwds.items():
            setattr(self, key, value)

def lmc555(Ra, Rb, C=EngineerNumber("0.1u")):
    tL = CONST * Rb * C
    tH = tL + CONST * Ra * C
    t = tL + tH
    f = 1 / t

    return (tL, tH, t, f)

def check_Hz_in_range(r_min, r_max, c):
    tf = []
    ra = EngineerNumber(r_min)
    rb = EngineerNumber(r_max)

    tL, tH, t, f = lmc555(ra, rb, c)
    tup = (tL, tH, t, f, ra, rb, c)
    tf.append(tup)

    ra, rb = rb, ra
    tL, tH, t, f = lmc555(ra, rb, c)
    tup = (tL, tH, t, f, ra, rb, c)
    tf.append(tup)

    return tf

# esn means e_series_name
def brute_force_LMC555(resistor_e_sesires, capacitor_e_sesires):
    resistors = get_resistors(resistor_e_sesires, ORDERS_RESISTOR)
    capacitors = get_capacitors(capacitor_e_sesires, ORDERS_CAPACITOR)

    combi_rbra = tuple(product(resistors, resistors))
    len_combinations = len(combi_rbra) * len(capacitors)

  # print("len(resistors) ** 2 =", len(resistors) ** 2)
  # print("len(combi_rbra) =", len(combi_rbra))
  # print("len(capacitors) =", len(capacitors))
  # print("len_combinations =", len_combinations)
  # print("len(resistors) ** 2 * len(capacitors) / len_combinations =", len(resistors) ** 2 * len(capacitors) / len_combinations)

    tf = [None] * len_combinations
    i = 0
    for rbra, c in product(combi_rbra, capacitors):
        rb, ra = rbra
        tL, tH, t, f = lmc555(ra, rb, c)

        dutyL = tL / t
        dutyH = 1 - dutyL

        kwds = {}
        for name in NAMES:
            kwds[name] = locals()[name]
        l555 = LMC555(**kwds)
        tf[i] = l555
        i += 1
    tf = tf[:i]

    return tf

def look_for_optimized_duty(parameters, duty):
    # dutyL を優先して sort。
    parameters.sort(key=lambda parameter: math.fabs(duty - parameter.dutyL))
    return parameters

def look_for_optimized_Hz(parameters, Hz):
    # 周波数を優先して sort
    parameters.sort(key=lambda parameter: math.fabs(Hz - parameter.f))
    return parameters

def parse_args():
    parser = argparse.ArgumentParser(description=_("look for optimized Hz."))

    parser.add_argument("--Hz", metavar="f", dest="Hz",
                       default=1000,
                       type=EngineerNumber,
                       help="frequency default: 1000")
    parser.add_argument("--duty", metavar="d", dest="duty",
                       type=EngineerNumber, default="0.1",
                       help="duty default: 0.1")
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

    tf = look_for_optimized_Hz(parameters, EngineerNumber(args.Hz))
#   tf = look_for_optimized_duty(parameters, EngineerNumber(args.duty))

  # print("len(tf)=", len(tf))
  # print()
    top = args.top
    view_tf(tf, top)
    print()
