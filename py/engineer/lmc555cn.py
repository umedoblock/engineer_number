import os
import sys
import math

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

def lmc555(Ra, Rb, C=Number(0.1*MICRO)):
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

if __name__ == '__main__':
    c = Number(0.1, MICRO)
    ra = Number(10, MEGA)
    rb = Number(1, KILO)

    ra = Number(1, KILO)
    rb = Number(10, MEGA)

    ra = Number(220, KILO)
    rb = Number(390, KILO)

    # 剣菱
    c = Number(10, MICRO)
    ra = rb = Number(48, KILO)

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

    tf = []
    condition = False
    for r2 in E12:
        for r1 in E12:
            rb = Number(r2 * 10, KILO)
            ra = Number(r1 * 10, KILO)
            tL, tH, t, f = lmc555(ra, rb, c)
            condition = 1 or t == f and t == 1
            tup = (t, f, ra, rb, c)
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

    tf.sort(key=lambda x: math.fabs(1 - x[0]))
#   print('len(tf)=', len(tf))
    top = 3
    for t, f, ra, rb, c in tf[:top]:
        print(t, f, ra, rb, c)
        print('t={}, f ={}, ra={}, rb={}'.format(t, f, ra, rb))
        print()
