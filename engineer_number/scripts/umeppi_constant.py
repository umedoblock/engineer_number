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

NAMES = ("ra", "rb", "c", "ta", "tb", "T")

TA = EngineerNumber(6.5535, -3)
TB = EngineerNumber(607, -6)
RARB = 5.590

class UmeppiConstants(object):
    def __init__(self, **kwds):
        for key, value in kwds.items():
            setattr(self, key, value)

def umeppi_constants(ra, rb, c, ta, tb):
    if tb > TB and ra / rb > RARB and ta <= TA:
        return True
    else:
        return False

# esn means e_series_name
def brute_force_umeppi(resistor_e_sesires, capacitor_e_sesires):
    orders_resistor=range(KILO, MEGA + 1)
    orders_capacitor=range(PICO, MICRO + 3)
    resistors = get_resistors(resistor_e_sesires, orders_resistor)
    capacitors = get_capacitors(capacitor_e_sesires, orders_capacitor)

    len_combinations = (len(resistors) ** 2) * len(capacitors)

  # print("len(resistors) =", len(resistors))
  # print("len(capacitors) =", len(capacitors))
  # print("len_combinations =", len_combinations)

    uc = [None] * len_combinations
    i = 0
    for c in capacitors:
        c_0693 = 0.693 * c
        for rb in resistors:
            tb = c_0693 * rb
            if not tb > TB:
                continue
            for ra in resistors:
                if not ra / rb > RARB:
                    continue
                ta = c_0693 * ra + tb
                if not ta <= TA:
                    continue

                T = ta + tb
                kwds = {}
                for name in NAMES:
                    kwds[name] = locals()[name]
                ucs = UmeppiConstants(**kwds)
                uc[i] = ucs
                i += 1
    uc = uc[:i]

    return uc

def look_for_umeppi(parameters):
    parameters.sort(key=lambda parameter: math.fabs(parameter.T))
    return parameters

def parse_args():
    parser = argparse.ArgumentParser(description=_("look for optimized umeppi."))

#   parser.add_argument("--T", metavar="f", dest="T",
#                      default=1000,
#                      type=EngineerNumber,
#                      help="frequency default: 1000")
    parser.add_argument("--top", metavar="t", dest="top",
                       type=int, default=10,
                       help="ranking default: 10")
    args = parser.parse_args()
    return args

def view_uc(uc, top=-1):
    fmt = ", ".join(["{!s:>8s}"] * len(NAMES))

    print(fmt.format(*NAMES))
    for umeppi in uc[:top]:
        tup = (getattr(umeppi, name) for name in NAMES)
        print(fmt.format(*tup))

if __name__ == "__main__":
    args = parse_args()

    parameters = brute_force_umeppi("E12", "E6")

    uc = look_for_umeppi(parameters)

  # print("len(uc)=", len(uc))
  # print()
    top = args.top
    view_uc(uc, top)
    print()
