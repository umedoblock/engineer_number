# engineer_number moduce
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is receased under the MIT Lilense.
# https://github.com/umedoblock/engineer_number

import math, argparse
from itertools import *

import lib
lib.init_engineer_number()

from engineer_number import EngineerNumber
from engineer_number.constants import *
from engineer_number.lib import get_resistors, get_capacitors, close_values

NAMES = ("ce", "c3", "r1", "r2", "r4", "r5")

class CapacitanceMultiplier(object):
    def __init__(self, **kwds):
        for key, value in kwds.items():
            setattr(self, key, value)

def brute_force_to_look_for(c3=None, e_series_resistors="E12",
                                     e_series_capacitors="E6",
                                     orders_resistor=ORDERS_RESISTOR,
                                     orders_capacitor=ORDERS_CAPACITOR):
    resistors = get_resistors(e_series_resistors, orders_resistor)
    if not c3:
        capacitors = get_capacitors(e_series_capacitors, orders_capacitor)
    else:
        capacitors = c3
    r_combinations_with_replacement = list(combinations_with_replacement(resistors, 2))
    parameters = [None] * (len(r_combinations_with_replacement) ** 2 * len(capacitors))

    i = 0
    for r1r5, r2r4 in product(r_combinations_with_replacement, r_combinations_with_replacement):
        r1, r5 = r1r5
        r2, r4 = r2r4
        for c3 in capacitors:
            ce = c3 * (r1 * r5) / (r2 * r4)
            kwds = {}
            for name in NAMES:
                kwds[name] = locals()[name]
            cm = CapacitanceMultiplier(**kwds)
    #       print("i =", i)
            parameters[i] = cm
            i += 1

    return parameters

def view_parameters(parameters, top=-1):
    fmt = ", ".join(["{!s:>8s}"] * len(NAMES))

    print(fmt.format(*NAMES))
    for parameter in parameters[:top]:
        tup = (getattr(parameter, name) for name in NAMES)
        print(fmt.format(*tup))

def parse_args():
    parser = argparse.ArgumentParser(description=_("look for capacitance multiplier."))

    parser.add_argument("--ce", metavar="N", dest="ce",
                       default=EngineerNumber("0.1u"),
                       type=EngineerNumber,
                       help='capasitance default: EngineerNumber("0.1u")')
    parser.add_argument("--c3", metavar="N", dest="c3",
                       nargs='?', default=None,
                       help='optional capasitance default: None')
    parser.add_argument("--e_series", metavar="N", dest="e_series",
                       default="E12",
                       help="e_series default: E12")
    parser.add_argument("--top", metavar="N", dest="top",
                       type=int, default=10,
                       help="ranking default: 10")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()

    e_series = args.e_series
    if args.c3:
      # print("args.c3 =", args.c3.split())
        c3 = [EngineerNumber(c) for c in args.c3.split()]
    else:
        c3 = None

    parameters = brute_force_to_look_for(c3, "E12", "E6", ORDERS_KILO, ORDERS_NANO)
    parameters.sort(key=lambda parameter: math.fabs(args.ce - parameter.ce))

    view_parameters(parameters, args.top)
