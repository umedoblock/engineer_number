# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

# coding: utf-8

from decimal import Decimal, getcontext
import math, numbers, warnings, re

from .constants import *

import gettext
gettext.install("engineer_number", "")

class EngineerNumber(numbers.Real):
    """新しい EngineerNumber object を作ります。
    EngineerNumber object の精度は，Python3 の float object に依存します。
    Python3 では float object を C 言語の double 型の変数(=ob_fval) として定義
    しています。よって， EngineerNumber object の精度は，C 言語の double 型に
    依存します。

    'value' は，浮動小数点数，整数，文字列，または他の EngineerNumber object
    を引数に出来ます。何らの値も与えられなければ， EngineerNumber('0') を返し
    ます。
    'exponent10' が引数と出来るのは整数のみです。

    value * 10 ** exponent10
    の計算結果を EngineerNumber object の値とします。
    """

    # EngineerNumber instance を __str__() にて
    # 文字列表現した時の、小数点以下の有効桁数。
    round_ndigits = 3

    @classmethod
    def _parse_string(cls, ss):
        "有効数字の数値と 10 の乗数値を、tuple に詰めて返します。"

        sign = 1
#       print("ss=\"{}\"".format(ss))
#       pattern = r'([+\-]?[0-9\.]*|[a-zA-Z%]+)'
#       pattern = '([+\-]?)([0-9\.]*)([a-zA-Z%]*)'
#       pattern = '[+\-]?|[0-9\.]*|[a-zA-Z%]*'
#       parts = re.findall(pattern, ss)
        L = list(d_SYMBOL_EXPONENT)
        L.append("K")
        fmt = "|".join(["{}"] * len(L))
        fmt = fmt.format(*L)
    #   print("fmt =", fmt)

      # symbol_pattern = re.compile(r'([+\-0-9eE\.]*)({})$'.format(fmt))
      # symbol_pattern = re.compile(r'([+\-\deE.]*)(\D)$'.format(fmt))
      # m = symbol_pattern.search(ss)
      # print("m={}".format(m))

      # parts = m.groups()
      # parts = re.search(r'([+\-]?[0-9\.]*)({})$'.format(fmt), ss).groups()
        pattern = re.compile(r'([+\-]?)([0-9\.]*)({})$'.format(fmt))
        pattern = re.compile(r'([+\-]?)([0-9\.]*)(\D+)$')
        pattern = re.compile(r'([+\-]?)([0-9\.]*)(\D*)$')
        parts = pattern.search(ss).groups()
        _sign, numerical_part, suffix = parts
        if _sign == "-1":
            sign = -1
        if suffix == ".":
            si = ""
        else:
            si = suffix
        if parts == ('', ''):
            si = ss[-1]
#       print("numerical_part={}, si={}".format(numerical_part, si))
#       raise()
#       pattern = re.compile(r'([+\-0-9\.]*)([a-zA-Z]*|%)$')
#       pattern = re.compile(r'([+\-]?)([0-9\.]*)([^+\-0-9\.]*)$')
#       pattern = re.compile(r'([+\-]?)([0-9eE\.]*)([^+\-0-9\.]*)$')
#       pattern = re.compile(r'([+\-]?)([0-9eE\.]*)([^+\-0-9\.]*)$')
#       m = pattern.search(ss)
#       parts = m.groups()

#       if True or ss.startswith("10"):
#           print("ss=\"{}\"".format(ss))
#           print("ss[-1]=\"{}\"".format(ss[-1]))
#           print("parts=\"{}\"".format(parts))
#           print("parts==\"{}\"".format(parts == ('', '')))
#           print("numerical_part=\"{}\"".format(numerical_part))
#           print("suffix=\"{}\"".format(suffix))
#           print("si=\"{}\"".format(si))
        inappropriate = ss.replace("".join(parts), "")
      # if len(parts) > 1:
      #     sign, numerical_part, si = parts
      # else:
      #     numerical_part = parts[0]
      #     si = ""
#       if inappropriate and inappropriate != "." and not si in d_SYMBOL_EXPONENT:
#           si = inappropriate
        if si == "K":
          # message = ("cannot accept "K" as SI prefix symbol. "
          #            "please use "k" as prefix if you hope to describe kilo."
          #            "Because "K" means Kelbin celcius.")
            message = _(""
                       '"K" を SI 接頭辞の記号として'
                       '使用することは出来ません。\n'
                       'kilo を表現したい場合、 "K" ではなく、小文字の "k" を'
                       'お使い下さい。\n'
                       'なぜならば、"K" は、Kelvin 温度を表現するための'
                       '単位記号だからです。')
            raise KeyError(message)
      # print("si =", si, "value =", value)
        exponent10 = cls._si2exponent10(si)

      # print("numerical_part = '{}'".format(numerical_part))
        value = float(numerical_part)

        return (sign, value, exponent10)

    @classmethod
    def _si2exponent10(cls, si):
        """SI 接頭辞に対応する、10 の乗数値を返します。"""
        try:
            exponent10 = d_SYMBOL_EXPONENT[si]
        except KeyError as raiz:
          # message = \
          #     ("SI prefix symbol must be in "
          #      "{}".format(tuple(d_SYMBOL_EXPONENT)))
            tup = tuple(d_SYMBOL_EXPONENT)
            fmt = ", ".join(['"{}"'] * len(tup))
            fmt = "({})".format(fmt)
            symbols = fmt.format(*tup)
            message = \
               _("SI 接頭辞の記号は、次のいずれかでなければなりません。"
                 "{}").format(symbols)
            raise KeyError(message)
        return exponent10

    def __init__(self, value=0.0, exponent10=0):
        """有効数値と 10 の乗数値を指定します。
        value を、二つの方法により指定できます。
        一つ目は、有効数値を整数値、浮動小数値として指定する方法です。
        二つ目は、有効数値の文字列と SI 接頭辞を連結し、文字列として
        指定する方法です。
        exponent10 は、無指定であれば、0 として取り扱います。

        以下の計算式により、value, exponent10 の値から、
        EngineerNumber.num 属性の値を計算します。
        num = value * 10 ** exponent10
        """
        # value is None
        if value is None:
            print("value={}, exponent10={}".format(value, exponent10))
            raise ValueError()
        elif value == "":
            value = 0.0

        sign = 1

        if not isinstance(value, int) and not isinstance(value, float):
            _value = None
            try:
                _value = float(value)
            except ValueError as e:
                expression = "could not convert string to float: "
                if not e.args[0].startswith(expression):
                    raise e
            if isinstance(_value, float) and _value <= 1.0:
                value = _value

        if isinstance(value, str):
            if not value:
                value = "0"
            sign, value, adjust_exponent10 = EngineerNumber._parse_string(value)
            exponent10 += adjust_exponent10
        self.num = sign * value * (10 ** exponent10)
        # >>> 10 ** 0
        # 1
        self._normalize()

    def __getitem__(self, si_prefix):
        """self[si_prefix] として、SI 接頭辞変換を行う。"""
        return self._force(si_prefix)

    def _force(self, si=""):
        """SI 接頭辞により有効数字を変換。"""
        exponent10 = EngineerNumber._si2exponent10(si)
        value = self.num / (10 ** exponent10)
        fmt = ":.{}f".format(EngineerNumber.round_ndigits)
        fmt = "{" + fmt + "}{}"
        s = fmt.format(round(value, EngineerNumber.round_ndigits), si)
        return s

    def _normalize(self):
        """EngineerNumber.num の値から、_num, _exponent10 を正規化する。
        num, _num, _exponent10 の計算方法は、簡単に以下の通り。

        _exponent10 = (log10(num) // GROUP_OF_DIGITS(=3)) * GROUP_OF_DIGITS
        _num = num // (10 ** _exponent10)
        num =(大体同じ、approximately equal to) _num * 10 ** _exponent10

        _exponent10 は SI 接頭辞と連動するため、
        GROUP_OF_DIGITS(=3) の整数倍になっていることに注意。"""

        num = self.num
        while isinstance(num, EngineerNumber):
            num = num.num
        if num == 0:
            self._num = 0
            self._exponent10 = 0
            return
        elif num > 0:
            sign_num = 1
        else:
            sign_num = -1
        num *= sign_num
      # print("num={}".format(num))
        exponent = math.log10(num)
        if exponent >= 0:
            sign_exponent = 1
        else:
            sign_exponent = -1
        div, mod = divmod(exponent, GROUP_OF_DIGITS)
        div = int(div)
        exponent *= sign_exponent
        exponent10 = div * GROUP_OF_DIGITS
        factor = 10 ** exponent10
        _num = num / factor
        _num *= sign_num

        self._num = _num
        self._exponent10 = exponent10
        return self

    def calc_error(self, other):
        # calc error self with other
        num = abs(self.num - other.num)
        return EngineerNumber(num / self.num)

    def in_tolerance_error(self, other, tolerance_error):
        if self.calc_error(other) <= tolerance_error:
            return True
        else:
            return False

    def sqrt(self):
        """math.sqrt() の help を読んで。"""
        root = math.sqrt(self)
        return EngineerNumber(root)

    def _detail(self):
        """主に debug 用。
        github への移行を期に，非公開とした。"""
        print(self)
        print("        num =", self.num)
        print("     _num =", self._num)
        print("_exponent10 =", self._exponent10)

    def __add__(self, other):
        """object.__add__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num + other.num
        return EngineerNumber(n)

    def __sub__(self, other):
        """object.__sub__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num - other.num
        return EngineerNumber(n)

    def __mul__(self, other):
        """object.__mul__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num * other.num
        return EngineerNumber(n)

    def __floordiv__(self, other):
        """object.__floordiv__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num // other.num
        return EngineerNumber(n)

    def __truediv__(self, other):
        """object.__truediv__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num / other.num
        return EngineerNumber(n)

    def __mod__(self, other):
        """object.__mod__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = self.num % other.num
        return EngineerNumber(n)

    def __divmod__(self, other):
        """object.__divmod__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        div, mod = divmod(self.num, other.num)
        return (EngineerNumber(div), EngineerNumber(mod))

    def __pow__(self, other):
        """object.__pow__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other)
        n = pow(self.num, other.num)
        return EngineerNumber(n)

    def __int__(self):
        """object.__int__() の help を読んで。"""
        if self._exponent10 < 0:
          # message = "abs(number(={})) in range(0, 1) convert to int.".format(self)
            message = _("0 < abs(number(={})) < 1 を満たす数字を "
                        "int に変換しようとしました。").format(self)
            raise UserWarning(message)
        return int(self.num)

    def __float__(self):
        """object.__float__() の help を読んで。"""
        return float(self.num)

    def __radd__(self, other):
        """object.__radd__() の help を読んで。"""
        n = other + self.num
        return EngineerNumber(n)

    def __rsub__(self, other):
        """object.__rsub__() の help を読んで。"""
        n = other - self.num
        return EngineerNumber(n)

    def __rmul__(self, other):
        """object.__rmul__() の help を読んで。"""
      # print("self=", type(self))
      # print("other=", type(other))
        n = other * self.num
        return EngineerNumber(n)

    def __rfloordiv__(self, other):
        """object.__rfloordiv__() の help を読んで。"""
        n = other // self.num
      # print("self.num={} // other={}, n={}".format(self.num, other, n))
        return EngineerNumber(n)

    def __rtruediv__(self, other):
        """object.__rtruediv__() の help を読んで。"""
      # print("self=", type(self))
      # print("other=", type(other))
        n = other / self.num
        return EngineerNumber(n)

    def __rmod__(self, other):
        """object.__rmod__() の help を読んで。"""
        n = other % self.num
        return EngineerNumber(n)

    def __rdivmod__(self, other):
        """object.__rdivmod__() の help を読んで。"""
        div, mod = divmod(other, self.num)
        return (EngineerNumber(div), EngineerNumber(mod))

    def __rpow__(self, other):
        """object.__rpow__() の help を読んで。"""
        n = pow(other, self.num)
        return EngineerNumber(n)

    def __eq__(self, other):
        """object.__eq__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other, ONE)
        return self._exponent10 == other._exponent10 and \
               round(self) == round(other)

    def __ne__(self, other):
        """object.__ne__() の help を読んで。"""
        return not self == other

    def __gt__(self, other):
        """object.__gt__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other, ONE)
        return round(self) > round(other)

    def __ge__(self, other):
        """object.__ge__() の help を読んで。"""
        return self > other or self == other

    def __lt__(self, other):
        """object.__lt__() の help を読んで。"""
        if not isinstance(other, EngineerNumber):
            other = EngineerNumber(other, ONE)
        return round(self) < round(other)

    def __le__(self, other):
        """object.__le__() の help を読んで。"""
        return self < other or self == other

    def __repr__(self):
        """object.__repr__() の help を読んで。"""
        # for EngineerNumber in tuple.
        return 'EngineerNumber("{}")'.format(str(self))

    def __str__(self):
        """object.__str__() の help を読んで。"""
        symbol = ""
        if self._exponent10 in d_EXPONENT_SYMBOL:
            symbol = d_EXPONENT_SYMBOL[self._exponent10]
#           s = "{:.3f}{}"
            fmt = ":.{}f".format(EngineerNumber.round_ndigits)
            fmt = "{" + fmt + "}{}"
            round_num = \
                round(self._num, EngineerNumber.round_ndigits)
            s = fmt.format(round_num, symbol)
        else:
            s = str(self.num)
        return "{}".format(s)

    def __abs__(self):
        """object.__abs__() の help を読んで。"""
        return abs(self.num)

    def __pos__(self):
        """object.__pos__() の help を読んで。"""
        return +self.num

    def __neg__(self):
        """object.__neg__() の help を読んで。"""
        return -self.num

    def __round__(self, ndigits=None):
        """object.__round__() の help を読んで。"""
        if ndigits is None:
            ndigits = EngineerNumber.round_ndigits
        if self._exponent10 < 0:
            ndigits += abs(self._exponent10)
        return round(self.num, ndigits)

    def __ceil__(self):
        """math.__ceil__() の help を読んで。"""
        return math.ceil(self.num)

    def __floor__(self):
        """math.floor() の help を読んで。"""
        return math.floor(self.num)

    def __trunc__(self):
        """math.trunc() の help を読んで。"""
        return math.trunc(self.num)
