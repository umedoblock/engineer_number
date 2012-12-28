import os
import sys
import math

sys.path.append(os.path.join(os.path.dirname(__file__)))
from constants import *

class Number(object):

    def __init__(self, value, factor=ONE):
        if not factor in FACTORS:
            print('value={}, warning: '.format(value), end='')
            print(Warning('factor={:.3e} not in FACTORS={}'.format(factor, FACTORS)))
        self.num = value * factor
        self._normalize()

    def _normalize(self):
        num = self.num
        if num >= 0:
            sign_num = 1
        else:
            sign_num = -1
        num *= sign_num
      # print('_normalize(num={})'.format(num))
      # if math.fabs(num) <= 1:
      #     self.value = num
      #     self.factor = ONE
      #     return
      # print('math.log10(num={})'.format(num))
        exponent = math.log10(num)
        if exponent >= 0:
            sign_exponent = 1
        else:
            sign_exponent = -1
        div, mod = divmod(exponent, 3)
        exponent *= sign_exponent
        exponent10 = div * 3
        factor = 10 ** exponent10
        value = num / factor
        value *= sign_num
      # print('=========================')
      # print('num={:.3e}'.format(num))
      # print('exponent10={}, exponent={}, factor={}, value={}'.format(exponent10, exponent, factor, value))
      # print('=========================')
        self.value = value
        self.factor = factor
        return self

    def __add__(self, other):
        n = self.num + other.num
        return Number(n)

    def __sub__(self, other):
        n = self.num - other.num
        return Number(n)

    def __mul__(self, other):
        n = self.num * other.num
        return Number(n)

    def __floordiv__(self, other):
        n = self.num // other.num
        return Number(n)

    def __truediv__(self, other):
        n = self.num / other.num
        return Number(n)

    def __mod__(self, other):
        n = self.num % other.num
        return Number(n)

    def __divmod__(self, other):
        div, mod = divmod(self.num, other.num)
        return (Number(div), Number(mod))

    def __pow__(self, other):
        n = pow(self.num, other.num)
        return Number(n)

    def __repr__(self):
        # for Number in tuple.
        return str(self)

    def __str__(self):
        symbol = ''
        if self.factor in d_FACTOR_SYMBOL:
            symbol = d_FACTOR_SYMBOL[self.factor]
            s = '{:.3f}{}'.format(round(self.value, 3), symbol)
        else:
            s = str(self.num)
        return s

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

def lmc555(Ra, Rb, C=0.1*MICRO):
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
