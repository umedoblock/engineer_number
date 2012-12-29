import os
import sys
import math
import numbers

from constants import *

class Number(numbers.Real):

    ndigits = 3

    @classmethod
    def make(cls, ss):
        value, factor = Number._parse_string(ss)
      # print('value =', value, 'factor =', factor)
        number = Number(value, factor)
        return number

    @classmethod
    def _parse_string(cls, ss):
        si_prifixes = ''.join(d_FACTOR_SYMBOL.values())
      # print('si_prifixes =', si_prifixes)
      # print('ss =', ss)
        if ss[-1].isalpha():
            si = ss[-1]
        else:
            si = ''
        value = float(ss.replace(si, ''))
      # print('si =', si, 'value =', value)
        factor_index = tuple(d_FACTOR_SYMBOL.values()).index(si)
        factor = tuple(d_FACTOR_SYMBOL.keys())[factor_index]

        return (value, factor)

    def __init__(self, value, factor=ONE):
        self.num = value * factor
        self._normalize()

    def _normalize(self):
        num = self.num
        while isinstance(num, Number):
            num = num.num
        if num == 0:
            self._value = 0
            self._factor = 1
            return
        elif num > 0:
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
        self._value = value
        self._factor = factor
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

    def _get_num(self):
        self_num = self.num
        while isinstance(self_num, Number):
            self_num = self_num.num
        return self_num

    def __eq__(self, other):
      # self_num = self._get_num()
      # # cannot determine that other is Number instance.
      # # so repeated copy and paste.
      # while isinstance(other, Number):
      #     other = other.num
      # return round(self) == round(other, Number.ndigits)

        if not isinstance(other, Number):
            other = Number(other, ONE)
      # print('self._value =', self._value)
      # print('other._value =', other._value)
      # print('self._factor =', self._factor)
      # print('other._factor =', other._factor)
        return self._factor == other._factor and \
               round(self) == round(other)

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        self_num = self._get_num()
        # cannot determine that other is Number instance.
        # so repeated copy and paste.
        while isinstance(other, Number):
            other = other.num
        return self_num > other

    def __ge__(self, other):
      # print(dir(1.0))
      # print(dir(self))
        return self > other or self == other

    def __lt__(self, other):
        self_num = self._get_num()
        # cannot determine that other is Number instance.
        # so repeated copy and paste.
        while isinstance(other, Number):
            other = other.num
        return self_num < other

    def __le__(self, other):
        return self < other or self == other

    def __repr__(self):
        # for Number in tuple.
        return str(self)

    def __str__(self):
        symbol = ''
        if self._factor in d_FACTOR_SYMBOL:
            symbol = d_FACTOR_SYMBOL[self._factor]
#           s = '{:.3f}{}'
            fmt = ':.{}f'.format(Number.ndigits)
            fmt = '{' + fmt + '}{}'
            s = fmt.format(round(self), symbol)
        else:
            s = str(self.num)
        return s

    def __abs__(self):
        return abs(self.num)

    def __pos__(self):
        return +self.num

    def __neg__(self):
        return -self.num

    def __ceil__(self):
        return math.ceil(self.num)

    def __round__(self, ndigits=None):
        if ndigits is None:
            ndigits = Number.ndigits
      # print('__round__()')
        return round(self._value, ndigits=ndigits)

    def __floor__(self):
        return math.floor(self.num)

    def __trunc__(self):
        return math.trunc(self.num)
