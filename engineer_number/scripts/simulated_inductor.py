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

from engineer_number import EngineerNumber as ENM
from engineer_number.constants import *
from engineer_number.lib import get_resistors, close_values

NAMES = ("le", "r1", "c2", "r3", "r4", "r5")

class SimlatedInductor(object):
    def __init__(self, **kwds):
        for key, value in kwds.items():
            setattr(self, key, value)

def brute_force_to_look_for_rc(c2=None, e_series_resistors="E12", e_series_capacitors="E6", orders_resistor=ORDERS_RESISTOR, orders_capacitor=ORDERS_CAPASITOR):
    resistors = get_resistors(e_series_resistors, orders_resistor)
    if not c2:
        capacitors = get_capacitors(e_series_capacitors, orders_capacitor)
    else:
        capacitors = (c2,)
    r_combinations_with_replacement = list(combinations_with_replacement(resistors, 3))
    parameters = [None] * (len(r_combinations_with_replacement) * len(resistors) * len(capacitors))

    i = 0
    for c2, r4 in product(capacitors, resistors):
        for r5, r3, r1 in r_combinations_with_replacement:
            le = c2 * (r1 * r3 * r5) / r4
            kwds = {}
            for name in NAMES:
                kwds[name] = locals()[name]
            si = SimlatedInductor(**kwds)
    #       print("i =", i)
            parameters[i] = si
            i += 1

    return parameters

def view_parameters(parameters, top=-1):
    fmt = ", ".join(["{!s:>8s}"] * len(NAMES))

    print(fmt.format(*NAMES))
    for parameter in parameters[:top]:
        tup = (getattr(parameter, name) for name in NAMES)
        print(fmt.format(*tup))

def parse_args():
    parser = argparse.ArgumentParser(description=_("look for simulated inductor."))

    parser.add_argument("--c", metavar="N", dest="c",
                       default=ENM("0.1u"),
                       help='capasitance default: ENM("0.1u")')
    parser.add_argument("--le", metavar="N", dest="le",
                       default=ENM("530u"),
                       type=ENM,
                       help='Henly default: ENM("530u"')
    parser.add_argument("--e_series", metavar="N", dest="e_series",
                       nargs="?", default="E12",
                       help="e_series default: E12")
    parser.add_argument("--top", metavar="N", dest="top",
                       type=int, nargs="?", default=10,
                       help="ranking default: 10")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()

    e_series = args.e_series
#   le = args.le
    c2 = ENM(args.c)
# # c2, r1, r3, r5, r4 = ENM("0.1u"), ENM("1k"), ENM("10k"), ENM("10k"), ENM("1k")
# # le = c2 * (r1 * r3 * r5) / r4
# # print("le =", le)
  # c2 = ENM("0.1u")
  # le = ENM("530u")
# # 530u = 0.1u * (r1 * r3 * r5) / r4
# # 530u / 0.u = (r1 * r3 * r5) / r4
  # x = ENM("530u") / c2

# r1 * r3 * r5 / r4 =
# >>> ENM("530u") / ENM("0.1u")
# EngineerNumber("5.300k")

    parameters = brute_force_to_look_for_rc(c2, "E12", "E6", ORDERS_KILO, ORDERS_NANO)
    parameters.sort(key=lambda parameter: math.fabs(args.le - parameter.le))

    view_parameters(parameters, args.top)
