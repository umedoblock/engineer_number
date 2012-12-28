import numbers
import math

EXA = 10 ** 18
PETA = 10 ** 15
TERA = 10 ** 12
GIGA = 10 ** 9
MEGA = 10 ** 6
KILO = 10 ** 3
ONE = 10 ** 0
MILLI = 10 ** -3
MICRO = 10 ** -6
NANO = 10 ** -9
PICO = 10 ** -12

FACTOR_BIG = (EXA, PETA, TERA, GIGA, MEGA, KILO)
FACTOR_SMALL = (MILLI, MICRO, NANO, PICO)
FACTORS = FACTOR_BIG + (ONE,) + FACTOR_SMALL

d_FACTOR_SYMBOL = {
    EXA:   'E',
    PETA:  'P',
    TERA:  'T',
    GIGA:  'G',
    MEGA:  'M',
    KILO:  'k',
    ONE:   '',
    MILLI: 'm',
    MICRO: 'u',
    NANO:  'n',
    PICO:  'p',
}

E6 = (1.0, 1.5, 2.2, 3.3, 4.7, 6.8, 10.0)
E12 = (1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2, 10.0)
E24 = (1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7,
       3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5,
       8.2, 9.1, 10.0)

# len(E12) = 13
# >>> 13 * 2
# 26
# >>> 13 * 4
# 52
# >>> 13 * 6
# 78

# combination
# for FACTOR_SMALL
# >>> (13 * 2) ** 2
# 676

# for FACTOR_BIG
# >>> (13 * 4) ** 2
# 2704

# for FACTORS
# >>> (13 * 6) ** 2
# 6084

# E series
class Enum(numbers.Number):
    @classmethod
    def generate(cls, num):
        exponent = math.log10(num)
        if exponent > 0:
            sign = 1
        else:
            sign = -1
        div, mod = divmod(exponent, 3)
        exponent *= sign
        exponent10 = div * 3
        factor = 10 ** exponent10
        value = num / factor
#       print('=========================')
#       print('num={:.3e}'.format(num))
#       print('exponent10={}, exponent={}, factor={}, value={}'.format(exponent10, exponent, factor, value))
#       print('=========================')
        return Enum(value, factor)

    def __init__(self, value, factor):
        if not factor in FACTORS:
            print('value={}, warning: '.format(value), end='')
            print(Warning('factor={:.3e} not in FACTORS={}'.format(factor, FACTORS)))
      # self.num = num
        self.value = value
        self.factor = factor
        self.num = self.value * self.factor

    def __mul__(self, other):
        n = self.num * other.num
        return Enum.generate(n)

    def __str__(self):
        symbol = ''
        if self.factor in d_FACTOR_SYMBOL:
            symbol = d_FACTOR_SYMBOL[self.factor]
            s = '{}{}'.format(round(self.value, 1), symbol)
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

if __name__ == '__main__':
    c = 0.1 * MICRO
    ra = 10 * MEGA
    rb = 1 * KILO

    ra = 1 * KILO
    rb = 10 * MEGA

    ra = 220 * KILO
    rb = 390 * KILO

    # 剣菱
    c = 10 * MICRO
    ra = rb = 48 * KILO

    print('ra = {:.3e}'.format(ra))
    print('rb = {:.3e}'.format(rb))
    print('c = {:.3e}'.format(c))
    print()

    tL, tH, t, f = lmc555(ra, rb, c)
    print('tL = {:.3e}'.format(tL))
    print('tH = {:.3e}'.format(tH))
    print('t = {:.3e}'.format(t))
    print('f = {:.3e}'.format(f))

    tf = []
    condition = False
    for r2 in E12:
        for r1 in E12:
            rb = r2 * 10 * KILO
            ra = r1 * 10 * KILO
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

  # tf.sort(key=lambda x: math.fabs(1 - x[0]))
  # print('len(tf)=', len(tf))
  # top = 3
  # for t, f, ra, rb, c in tf[:top]:
  #     print('t={:.3f}, f ={:.3f}, ra={:.1e}, rb={:.1e}'.format(t, f, ra, rb))


    print()

    #208 大文字小文字をそのうち直す。
    m3_3 = Enum(3.3, MEGA)
    print('3.3 MEGA =', m3_3)
    k47 = Enum(47, KILO)
    print('47 KILO =', k47)

    mili47 = Enum(47, MILLI)
    print('47 MILLI =', mili47)
    mcr3_3 = Enum(3.3, MICRO)
    print('3.3 MICRO =', mcr3_3)

    print('155.1G =', k47 * m3_3)
    print('155.1 NANO =', mili47 * mcr3_3)

    print('2.2 KILO =', k47 * mili47)
    print('10.9 =', m3_3 * mcr3_3)
    print('155.1 MILI =', k47 * mcr3_3)
    print('155.1 KILO =', m3_3 * mili47)

    # TOO BIG
    T10 = Enum(10, TERA)
    G40 = Enum(40, GIGA)
    BIG400 = T10 * G40
    print('T10 =', T10)
    print('G40 =', G40)
    print('BIG400 =', BIG400)

    # too small
    m1 = Enum(1, MICRO)
    n4 = Enum(4, NANO)
    small4 = m1 * n4
    print('m1 =', m1, m1.num)
    print('n4 =', n4, n4.num)
    print('small4 =', small4, small4.num)

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
