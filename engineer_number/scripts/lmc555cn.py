import os, sys, math
import argparse, gettext

import lib
lib.init_engineer_number()
from engineer_number import *
from engineer_number.constants import *
from engineer_number.lib import get_resistors

# >>> math.log(2)
# 0.6931471805599453
# >>> math.log(2, math.e)
# 0.6931471805599453
# >>> math.log(8, 2) # swaped math logarithm
# 3.0 # 2 ** 3 = 8, pow(2, 3)
CONST = math.log(2, math.e)

def lmc555(Ra, Rb, C=EngineerNumber('0.1u')):
    tH = CONST * (Ra + Rb) * C
    tL = CONST * Rb * C
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

def look_for_optimized_duty(Hz, c=EngineerNumber('0.1u'), duty=EngineerNumber(0.5)):
    Rs = get_resistors('E12')
    len_combination = len(Rs) ** 2
  # print('len_combination =', len_combination)

    tf = []
    for r2 in Rs:
        for r1 in Rs:
            rb = EngineerNumber(r2, ONE)
            ra = EngineerNumber(r1, ONE)
            tL, tH, t, f = lmc555(ra, rb, c)
            dutyL = tL / t
            dutyH = tH / t
            tup = (dutyL, dutyH, t, f, ra, rb, c)
            tf.append(tup)

    # dutyL を優先して sort。
    tf.sort(key=lambda x: math.fabs(0.5 - x[0]))
    return tf

NAMES = ("tL", "tH", "t", "f", "ra", "rb", "c")

def look_for_optimized_Hz(Hz, c=EngineerNumber('0.1u')):
    Rs = get_resistors('E12')
    len_combination = len(Rs) ** 2
  # print('len_combination =', len_combination)

    tf = []
    for r2 in Rs:
        for r1 in Rs:
            d = {}
            rb = EngineerNumber(r2, ONE)
            ra = EngineerNumber(r1, ONE)
            tL, tH, t, f = lmc555(ra, rb, c)

            for name in NAMES:
                d[name] = locals()[name]
            tf.append(d)

    # Hz を優先して sort。
    tf.sort(key=_most)
    return tf

Hz=1000
def _most(d, f=Hz):
    return math.fabs(f - d["f"])

def parse_args():
    parser = argparse.ArgumentParser(description=_('look for optimized Hz.'))

    parser.add_argument('--Hz', metavar='N', dest='Hz',
                       nargs='?', default=1000,
                       help='frequency default: 1000')
    parser.add_argument('--capacita', metavar='N', dest='c_str',
                       nargs='?', default='0.1u',
                       help='capacita default: 0.1u')
    parser.add_argument('--top', metavar='N', dest='top',
                       type=int, nargs='?', default=10,
                       help='ranking default: 10')
    args = parser.parse_args()
    return args

def view_tf(tf, top=-1):
    fmt = ", ".join(["{!s:>8s}"] * len(NAMES))

    print(fmt.format(*NAMES))
    for d in tf[:top]:
        tup = (d[name] for name in NAMES)
        print(fmt.format(*tup))

if __name__ == '__main__':
    args = parse_args()

    c = EngineerNumber(args.c_str)
    Hz = EngineerNumber(args.Hz)
    tf = look_for_optimized_Hz(Hz, c)
#   tf = look_for_optimized_duty(Hz, c)

  # print('len(tf)=', len(tf))
  # print()
    top = args.top
    view_tf(tf, top)
    print()
