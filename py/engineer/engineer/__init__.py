import os
import sys
import math

from constants import *

class Number(object):

    def __init__(self, value, factor=ONE):
        self.num = value * factor
        self._normalize()

    def _normalize(self):
        num = self.num
        while isinstance(num, Number):
            num = num.num
        if num == 0:
            self.value = 0
            self.factor = 1
            return
        if num >= 0:
            sign_num = 1
        else:
            sign_num = -1
        num *= sign_num
      # print('num={}'.format(num))
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
        if not isinstance(other, Number):
            other = Number(other)
        if isinstance(other, Number):
            n = self.num + other.num
        else:
            n = self.num + other
        return Number(n)

    def __sub__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        n = self.num - other.num
        return Number(n)

    def __mul__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        n = self.num * other.num
        return Number(n)

    def __floordiv__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        n = self.num // other.num
        return Number(n)

    def __truediv__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        n = self.num / other.num
        return Number(n)

    def __mod__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        n = self.num % other.num
        return Number(n)

    def __divmod__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        div, mod = divmod(self.num, other.num)
        return (Number(div), Number(mod))

    def __pow__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        n = pow(self.num, other.num)
        return Number(n)

    def __int__(self):
        raise RuntimeError('no meaning: convert to integer.')

    def __float__(self):
        return float(self.num)

    def __radd__(self, other):
        n = other + self.num
        return Number(n)

    def __rsub__(self, other):
        n = other - self.num
        return Number(n)

    def __rmul__(self, other):
      # print('self=', type(self))
      # print('other=', type(other))
        n = other * self.num
        return Number(n)

    def __rfloordiv__(self, other):
        n = other // self.num
      # print('self.num={} // other={}, n={}'.format(self.num, other, n))
        return Number(n)

    def __rtruediv__(self, other):
      # print('self=', type(self))
      # print('other=', type(other))
        n = other / self.num
        return Number(n)

    def __rmod__(self, other):
        n = other % self.num
        return Number(n)

    def __rdivmod__(self, other):
        div, mod = divmod(other, self.num)
        return (Number(div), Number(mod))

    def __rpow__(self, other):
        n = pow(other, self.num)
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
