import os, sys, math
import argparse, gettext

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

class LMC555(object):
    def __init__(self, **kwds):
        for key, value in kwds.items():
            setattr(self, key, value)

        self._calc_duty()

    def _calc_duty(self):
        self.dutyL = self.tL / self.t
        self.dutyH = 1 - self.dutyL

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
def brute_force_LMC555(resistor_esn, capacitor_esn):
    Rs = get_resistors(resistor_esn)
    Cs = get_capacitors(capacitor_esn)
    len_combination = len(Rs) ** 2 * len(Cs)
    print("len(Rs) ** 2 =", len(Rs) ** 2)
    print("len(Cs) =", len(Cs))
    print("len_combination =", len_combination)

    tf = [None] * len_combination
    i = 0
    for c in Cs:
        print("i = {}".format(i))
        for rb in Rs:
            for ra in Rs:
                tL, tH, t, f = lmc555(ra, rb, c)

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

NAMES = ("tL", "tH", "t", "f", "ra", "rb", "c")

def look_for_optimized_Hz(parameters, Hz):
    # 周波数を優先して sort
    parameters.sort(key=lambda parameter: math.fabs(Hz - parameter.f))
    return parameters

def parse_args():
    parser = argparse.ArgumentParser(description=_("look for optimized Hz."))

    parser.add_argument("--Hz", metavar="f", dest="Hz",
                       default=1000,
                       help="frequency default: 1000")
    parser.add_argument("--duty", metavar="d", dest="duty",
                       type=float, default="0.5",
                       help="duty default: 0.5")
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
