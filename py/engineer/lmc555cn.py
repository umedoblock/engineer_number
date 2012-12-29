import os
import sys
import math
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), 'engineer'))
from engineer import *
from engineer.constants import *

# >>> math.log(2)
# 0.6931471805599453
# >>> math.log(2, math.e)
# 0.6931471805599453
# >>> math.log(8, 2) # swaped math logarithm
# 3.0 # 2 ** 3 = 8, pow(2, 3)
CONST = math.log(2, math.e)

# c = 0.1 * MICRO

# tH = 0.693 * (ra + rb) * c
# tL = 0.693 * rb * c
# t = tH + tL
#   = 0.693 * (ra + 2 * rb) * c
# t = 0.693 * 3 * r * c if r = ra = rb

# t = 0.001 # 1 kHz
# = 0.693 * (ra + 2 * rb) * c
# = 0.693 * (ra + 2 * rb) * c = 0.001
# c = 0.001 / (0.693 * (ra + 2 * rb))

# if r = ra = rb = 1 kR
# c = 0.001 / (0.693 * (1k + 2 * 1k))
#   = 0.001 / (0.693 * 3k )
# >>> 0.001 / (0.693 * 3000 )
# 4.81000481000481e-07
# 0.481000481000481e-06
# 0.481 * 10 ** -6
# 0.481 * MICRO

def lmc555(Ra, Rb, C=EngineerNumber(0.1*MICRO)):
    _c2gnd = 0.1 * MICRO
    tH = CONST * (Ra + Rb) * C
    tL = CONST * Rb * C
    t = tL + tH
    f = 1 / t

    return (tL, tH, t, f)

'''
手持ちの抵抗は最大で 10M R
手持ちの抵抗は最小で 1 R
t = 0.693 * (ra + 2 * rb) * c
ここで、抵抗部分を rx として、
t = 0.693 * rx * c
制限があるのは、cの値なので、まずcの値を適当に決める。
"・０．１μＦ５０Ｖ
積層セラミックコンデンサ
（ムラタ製または各社相当品）"

積セラ 50V 0.1uF 2.54ピッチ[R指]
積セラ 50V 0.1uF 5.08ピッチ[R指]
積セラ 50V 1uF[R指]

LMC555 CMOS タイマ
■ 5V 電源で1mW 以下の消費電力
■ 3MHzまでの無安定周波数
■ 1.5V 動作電源電圧の保証
■ 出力は5V 電源で、TTL、CMOS ロジックと完全互換
'''

def look_for_optimized_Hz(Hz, c=EngineerNumber(0.1, MICRO)):
    #                         k                    M
    factor_big = (1, 10, 100, 1000, 10000, 100000, 1000000)
    Rs = []
    for factor in factor_big:
        for n in E12:
            r = factor * n
            Rs.append(r)
    Rs.append(10 * MEGA)
    combination = len(E12) ** 2 * len(factor_big)
    print('combination =', combination)
    combination = (len(E12) * len(factor_big) + 1) ** 2
    print('combination =', combination)
    tf = []
    condition = False
    for r2 in Rs:
        for r1 in Rs:
            rb = EngineerNumber(r2, ONE)
            ra = EngineerNumber(r1, ONE)
            tL, tH, t, f = lmc555(ra, rb, c)
            condition = 1 or t == f and t == 1
            tup = (tL, tH, t, f, ra, rb, c) # sort() x index refer here.
            tf.append(tup)
          # if condition:
          #     print('--')
          #     print('ra = {:.3e}'.format(ra))
          #     print('rb = {:.3e}'.format(rb))
          #     print('c = {:.3e}'.format(c))
          #     print()

          #     print('tL = {:.3e}'.format(tL))
          #     print('tH = {:.3e}'.format(tH))
          #     print('t = {:.3e}'.format(t))
          #     print('f = {:.3e}'.format(f))

    # Hz を優先して sort。
    tf.sort(key=lambda x: math.fabs(Hz - x[3]))
    return tf

def parse_args():
    parser = argparse.ArgumentParser(description='look for optimized Hz.')

    parser.add_argument('--Hz', metavar='N', dest='Hz',
                       type=int, nargs='?', default=1000,
                       help='frequency')
    parser.add_argument('--capacita', metavar='N', dest='c_str',
                       nargs='?', default='0.100m',
                       help='capacita')
    parser.add_argument('--top', metavar='N', dest='top',
                       type=int, nargs='?', default=10,
                       help='ranking')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

    c = EngineerNumber(0.1, MICRO)
    ra = EngineerNumber(10, MEGA)
    rb = EngineerNumber(1, KILO)

    ra = EngineerNumber(1, KILO)
    rb = EngineerNumber(10, MEGA)

    ra = EngineerNumber(220, KILO)
    rb = EngineerNumber(390, KILO)

    # 剣菱
    c = EngineerNumber(10, MICRO)
    ra = rb = EngineerNumber(48, KILO)

    print('ra = {}'.format(ra))
    print('rb = {}'.format(rb))
    print('c = {}'.format(c))
    print()

    tL, tH, t, f = lmc555(ra, rb, c)
    print('tL = {}'.format(tL))
    print('tH = {}'.format(tH))
    print('t = {}'.format(t))
    print('f = {}'.format(f))
    print()

    c = EngineerNumber(0.1, MICRO)
    c = EngineerNumber.make(args.c_str)
    Hz = args.Hz
#   tf = look_for_optimized_Hz(1, c)
#   tf = look_for_optimized_Hz(10000, c)
    tf = look_for_optimized_Hz(Hz, c)

    print('len(tf)=', len(tf))
    print()
    top = args.top
    for tL, tH, t, f, ra, rb, c in tf[:top]:
        print('tL={}, tH={}, t={}, f={}, ra={}, rb={}, c={}'.format(tL, tH, t, f, ra, rb, c))
