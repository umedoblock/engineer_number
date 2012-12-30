import os
import sys
import math
import numbers
import warnings

from .constants import *

class EngineerNumber(numbers.Real):

    round_ndigits = 3

    @classmethod
    def _parse_string(cls, ss):
        si_prifixes = ''.join(d_FACTOR_SYMBOL.values())
      # print('si_prifixes =', si_prifixes)
      # print('ss =', ss)
        if ss[-1].isalpha():
            si = ss[-1]
        else:
            si = ''
        if si == 'K':
          # message = ('cannot accept "K" as SI prefix symbol. '
          #            'please use "k" as prefix if you hope to describe kilo.'
          #            'Because "K" means Kelbin celcius.')
            message = ('"K" を SI 接頭辞の記号として使用することは出来ません。'
                       'kilo を表現したい場合、 "K" ではなく、小文字の "k" を'
                       'お使い下さい。'
                       'なぜならば、"K" は、Kelvin 温度を表現するための'
                       '単位記号だからです。')
            raise ValueError(message)

        value = float(ss.replace(si, ''))
      # print('si =', si, 'value =', value)
        factor = cls._si2factor(si)

        return (value, factor)

    @classmethod
    def _si2factor(cls, si):
        try:
            factor_index = tuple(d_FACTOR_SYMBOL.values()).index(si)
        except ValueError as raiz:
            if raiz.args[0] == 'tuple.index(x): x not in tuple':
              # message = \
              #     ('SI prefix symbol must be in '
              #      '{}'.format(ordered_FACTOR_SYMBOL)
                message = \
                    ('SI 接頭辞の記号は、次のいずれかでなければなりません。'
                     '{}'.format(ordered_FACTOR_SYMBOL))
                raise ValueError(message)
            else:
                raise raiz
        factor = tuple(d_FACTOR_SYMBOL.keys())[factor_index]
        return factor

    def __init__(self, value, factor=ONE):
        if isinstance(value, str):
            value, factor_parsed = EngineerNumber._parse_string(value)
            factor *= factor_parsed
        self.num = value * factor
        self._normalize()

    def _normalize(self):
        num = self.num
        while isinstance(num, EngineerNumber):
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
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num + other.num
        return EngineerNumber(n)

    def __sub__(self, other):
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num - other.num
        return EngineerNumber(n)

    def __mul__(self, other):
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num * other.num
        return EngineerNumber(n)

    def __floordiv__(self, other):
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num // other.num
        return EngineerNumber(n)

    def __truediv__(self, other):
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num / other.num
        return EngineerNumber(n)

    def __mod__(self, other):
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num % other.num
        return EngineerNumber(n)

    def __divmod__(self, other):
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        div, mod = divmod(self.num, other.num)
        return (EngineerNumber(div), EngineerNumber(mod))

    def __pow__(self, other):
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = pow(self.num, other.num)
        return EngineerNumber(n)

    def __int__(self):
        if self._factor < 1:
          # message = 'number(={}) in range(0, 1) convert to int.'.format(self)
            message = ('0 < number(={}) < 1 を満たす数字を '
                       'int に変換しようとしました。'.format(self))
            warnings.warn('{}'.format(message), UserWarning)
        return int(self.num)

    def __float__(self):
        return float(self.num)

    def __radd__(self, other):
        n = other + self.num
        return EngineerNumber(n)

    def __rsub__(self, other):
        n = other - self.num
        return EngineerNumber(n)

    def __rmul__(self, other):
      # print('self=', type(self))
      # print('other=', type(other))
        n = other * self.num
        return EngineerNumber(n)

    def __rfloordiv__(self, other):
        n = other // self.num
      # print('self.num={} // other={}, n={}'.format(self.num, other, n))
        return EngineerNumber(n)

    def __rtruediv__(self, other):
      # print('self=', type(self))
      # print('other=', type(other))
        n = other / self.num
        return EngineerNumber(n)

    def __rmod__(self, other):
        n = other % self.num
        return EngineerNumber(n)

    def __rdivmod__(self, other):
        div, mod = divmod(other, self.num)
        return (EngineerNumber(div), EngineerNumber(mod))

    def __rpow__(self, other):
        n = pow(other, self.num)
        return EngineerNumber(n)

    def _get_num(self):
        self_num = self.num
        while isinstance(self_num, EngineerNumber):
            self_num = self_num.num
        return self_num

    def __eq__(self, other):
      # self_num = self._get_num()
      # # cannot determine that other is EngineerNumber instance.
      # # so repeated copy and paste.
      # while isinstance(other, EngineerNumber):
      #     other = other.num
      # return round(self) == round(other, EngineerNumber.round_ndigits)

        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other, ONE)
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
        # cannot determine that other is EngineerNumber instance.
        # so repeated copy and paste.
        while isinstance(other, EngineerNumber):
            other = other.num
        return self_num > other

    def __ge__(self, other):
      # print(dir(1.0))
      # print(dir(self))
        return self > other or self == other

    def __lt__(self, other):
        self_num = self._get_num()
        # cannot determine that other is EngineerNumber instance.
        # so repeated copy and paste.
        while isinstance(other, EngineerNumber):
            other = other.num
        return self_num < other

    def __le__(self, other):
        return self < other or self == other

    def __repr__(self):
        # for EngineerNumber in tuple.
        return str(self)

    def detail(self):
        print(self)
        print('_factor =', self._factor)
        print(' _value =', self._value)
        print('    num =', self.num)

    def __str__(self):
        symbol = ''
        if self._factor in d_FACTOR_SYMBOL:
            symbol = d_FACTOR_SYMBOL[self._factor]
#           s = '{:.3f}{}'
            fmt = ':.{}f'.format(EngineerNumber.round_ndigits)
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
            ndigits = EngineerNumber.round_ndigits
      # print('__round__()')
        return round(self._value, ndigits=ndigits)

    def __floor__(self):
        return math.floor(self.num)

    def __trunc__(self):
        return math.trunc(self.num)
