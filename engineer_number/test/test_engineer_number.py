# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

import os, sys, math
import unittest
from test import support

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from engineer_number import *
from engineer_number.constants import *
from engineer_number.wire import *

class TestEngineerNumber(unittest.TestCase):
    def test_as_number(self):
        self.assertEqual(1000000000000000000000000.0, EngineerNumber("1Y"))
        self.assertEqual(1000000000000000000000.0, EngineerNumber("1Z"))
        self.assertEqual(1000000000000000000.0, EngineerNumber("1E"))
        self.assertEqual(1000000000000000.0, EngineerNumber("1P"))
        self.assertEqual(1000000000000.0, EngineerNumber("1T"))
        self.assertEqual(1000000000.0, EngineerNumber("1G"))
        self.assertEqual(1000000.0, EngineerNumber("1M"))
        self.assertEqual(1000.0, EngineerNumber("1k"))
        self.assertEqual(100.0, EngineerNumber("1h"))
        self.assertEqual(10.0, EngineerNumber("1da"))
        self.assertEqual(1.0, EngineerNumber("1"))
        self.assertEqual(0.1, EngineerNumber("1d"))
        self.assertEqual(0.01, EngineerNumber("1c"))
        self.assertEqual(0.001, EngineerNumber("1m"))
        self.assertEqual(0.000001, EngineerNumber("1u"))
        self.assertEqual(0.000000001, EngineerNumber("1n"))
        self.assertEqual(0.000000000001, EngineerNumber("1p"))
        self.assertEqual(0.000000000000001, EngineerNumber("1f"))
        self.assertEqual(0.000000000000000001, EngineerNumber("1a"))
        self.assertEqual(0.000000000000000000001, EngineerNumber("1z"))
        self.assertEqual(0.000000000000000000000001, EngineerNumber("1y"))

    def test__num(self):
        self.assertAlmostEqual(123.456, EngineerNumber("123.456Y")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456Z")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456E")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456P")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456T")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456G")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456M")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456k")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456m")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456u")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456n")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456p")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456f")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456a")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456z")._num)
        self.assertAlmostEqual(123.456, EngineerNumber("123.456y")._num)

        self.assertAlmostEqual(12.3456, EngineerNumber("123.456h")._num)
        self.assertEqual("12.346k", str(EngineerNumber("123.456h")))
        self.assertAlmostEqual(1.23456, EngineerNumber("123.456da")._num)
        self.assertEqual("1.235k", str(EngineerNumber("123.456da")))

        self.assertAlmostEqual(12.3456, EngineerNumber("123.456d")._num)
        self.assertEqual("12.346", str(EngineerNumber("123.456d")))
        self.assertAlmostEqual(1.23456, EngineerNumber("123.456c")._num)
        self.assertEqual("1.235", str(EngineerNumber("123.456c")))

    def test__exponent10(self):
        self.assertEqual(24, EngineerNumber("1Y")._exponent10)
        self.assertEqual(21, EngineerNumber("1Z")._exponent10)
        self.assertEqual(18, EngineerNumber("1E")._exponent10)
        self.assertEqual(15, EngineerNumber("1P")._exponent10)
        self.assertEqual(12, EngineerNumber("1T")._exponent10)
        self.assertEqual(9, EngineerNumber("1G")._exponent10)
        self.assertEqual(6, EngineerNumber("1M")._exponent10)
        self.assertEqual(3, EngineerNumber("1k")._exponent10)
        self.assertEqual(0, EngineerNumber("1h")._exponent10)
        self.assertEqual(0, EngineerNumber("1da")._exponent10)
        self.assertEqual(0, EngineerNumber("1")._exponent10)
        self.assertEqual(-3, EngineerNumber("1d")._exponent10)
        self.assertEqual(-3, EngineerNumber("1c")._exponent10)
        self.assertEqual(-3, EngineerNumber("1m")._exponent10)
        self.assertEqual(-6, EngineerNumber("1u")._exponent10)
        self.assertEqual(-9, EngineerNumber("1n")._exponent10)
        self.assertEqual(-12, EngineerNumber("1p")._exponent10)
        self.assertEqual(-15, EngineerNumber("1f")._exponent10)
        self.assertEqual(-18, EngineerNumber("1a")._exponent10)
        self.assertEqual(-21, EngineerNumber("1z")._exponent10)
        self.assertEqual(-24, EngineerNumber("1y")._exponent10)

    def test_as_str(self):
        self.assertEqual("123.457Y", str(EngineerNumber("123.4567Y")))
        self.assertEqual("123.456Y", str(EngineerNumber("123.456Y")))
        self.assertEqual("123.456Z", str(EngineerNumber("123.456Z")))
        self.assertEqual("123.456E", str(EngineerNumber("123.456E")))
        self.assertEqual("123.456P", str(EngineerNumber("123.456P")))
        self.assertEqual("123.456T", str(EngineerNumber("123.456T")))
        self.assertEqual("123.456G", str(EngineerNumber("123.456G")))
        self.assertEqual("123.456M", str(EngineerNumber("123.456M")))
        self.assertEqual("123.456k", str(EngineerNumber("123.456k")))
        self.assertEqual("12.346k", str(EngineerNumber("123.456h")))
        self.assertEqual("1.235k",  str(EngineerNumber("123.456da")))
        self.assertEqual("123.456", str(EngineerNumber("123.456")))
        self.assertEqual("12.346",  str(EngineerNumber("123.456d")))
        self.assertEqual("1.235",   str(EngineerNumber("123.456c")))
        self.assertEqual("123.456m", str(EngineerNumber("123.456m")))
        self.assertEqual("123.456u", str(EngineerNumber("123.456u")))
        self.assertEqual("123.456n", str(EngineerNumber("123.456n")))
        self.assertEqual("123.456p", str(EngineerNumber("123.456p")))
        self.assertEqual("123.456f", str(EngineerNumber("123.456f")))
        self.assertEqual("123.456a", str(EngineerNumber("123.456a")))
        self.assertEqual("123.456z", str(EngineerNumber("123.456z")))
        self.assertEqual("123.456y", str(EngineerNumber("123.456y")))

    def test_feed_empty_value(self):
        self.assertAlmostEqual(0, EngineerNumber())
        self.assertAlmostEqual(0, EngineerNumber(""))

    def test_as_abnormal_number(self):
        self.assertEqual(1.0, EngineerNumber("1."))
        self.assertEqual(0.1, EngineerNumber(".1"))
        self.assertEqual(1000.0, EngineerNumber("1.k"))
        self.assertEqual(100.0, EngineerNumber(".1k"))

        self.assertEqual(0.89, EngineerNumber(".89"))
        self.assertEqual(89000.0, EngineerNumber("89.k"))
        self.assertEqual(890.0, EngineerNumber(".89k"))

        self.assertEqual(28.9, EngineerNumber("2.89da"))
        self.assertEqual(2890.0, EngineerNumber("289da"))

    def test_simple(self):
        M3_3 = EngineerNumber(3.3, MEGA)
        # kilo must be "k". K means kelbin.
        k47 = EngineerNumber(47, KILO)
        mili47 = EngineerNumber(47, MILLI)
        mcr3_3 = EngineerNumber(3.3, MICRO)

        # __str__()
        self.assertEqual("3.300M", str(M3_3))
        self.assertEqual(3, k47._exponent10)
        self.assertEqual("47.000k", str(k47))
        self.assertEqual("47.000m", str(mili47))
        self.assertEqual("3.300u", str(mcr3_3))

        # mul
        self.assertEqual("155.100G", str(k47 * M3_3))
        self.assertEqual("155.100n", str(mili47 * mcr3_3))
        self.assertEqual("2.209k", str(k47 * mili47))
        self.assertEqual("10.890", str(M3_3 * mcr3_3))
        self.assertEqual("155.100m", str(k47 * mcr3_3))
        self.assertEqual("155.100k", str(M3_3 * mili47))

        self.assertEqual("100.000n", EngineerNumber("10p") * 10 ** 4)
        self.assertEqual("100.000n", EngineerNumber("10p", 4))

        # add, sub
        self.assertEqual("3.347M", str(M3_3 + k47))
        self.assertEqual("3.253M", str(M3_3 - k47))
        self.assertEqual("47.003m", str(mili47 + mcr3_3))
        self.assertEqual("46.997m", str(mili47 - mcr3_3))
        # big and small, ignored small
        self.assertEqual("3.300M", str(M3_3 + mili47))

    def test_over_range_for_big(self):
        # TOO BIG
        # in_YOTTA = 4 * 10 ** 26 = 400 * 10 ** 24
        in_YOTTA = EngineerNumber(4, 16) * EngineerNumber(1, 10)
        over_YOTTA = in_YOTTA * 10

        self.assertEqual("400.000Y", str(in_YOTTA))
        self.assertEqual("4" + "0" * 27, str(over_YOTTA))

        # over_YOTTA = 4 * 10 ** 29 = 400 * 10 ** 27
        over_YOTTA_i = EngineerNumber(4, 5) * EngineerNumber(1, 24)
        over_YOTTA_f = EngineerNumber(4, 5) * EngineerNumber(1.0, 24)

        self.assertEqual("4" + "0" * 29, str(over_YOTTA_i))
        self.assertEqual("4e+29", str(over_YOTTA_f))

        # in ZETTA
        T10 = EngineerNumber(10, TERA)
        G40 = EngineerNumber(40, GIGA)
        self.assertEqual("10.000T", str(T10))
        self.assertEqual("40.000G", str(G40))
        BIG400 = T10 * G40
        self.assertEqual("400.000Z", str(BIG400))

    def test_over_range_for_small(self):
        # too small
        # over_yocto = 0.04 * 10 ** -27 = 4 * 10 ** -29
        over_yocto_i = EngineerNumber(4, -5) * EngineerNumber(1, -24)
        over_yocto_f = EngineerNumber(4, -5) * EngineerNumber(1.0, -24)

        self.assertEqual("4e-29", str(over_yocto_i))
        self.assertEqual("4e-29", str(over_yocto_f))

        over_yocto_f *= 10
        self.assertEqual("4e-28", str(over_yocto_f))

        over_yocto_f *= 10
        self.assertEqual("4e-27", str(over_yocto_f))

        over_yocto_f *= 10
        self.assertEqual("4e-26", str(over_yocto_f))

        over_yocto_f *= 10
        self.assertEqual("4e-25", str(over_yocto_f))

        in_yocto_f = over_yocto_f * 10
        self.assertEqual("4.000y", str(in_yocto_f))

        # in yocto
        f1 = EngineerNumber(1, FEMTO)
        n4 = EngineerNumber(4, NANO)
        self.assertEqual("1.000f", str(f1))
        self.assertEqual("4.000n", str(n4))
        small4 = f1 * n4
        self.assertEqual("4.000y", str(small4))

    def test_honest_convert(self):
        self.assertEqual("987.000m", str(EngineerNumber(0.987)))
        self.assertEqual("1.000k", str(EngineerNumber(1000, ONE)))
        self.assertEqual("1.040k", str(EngineerNumber(1040, ONE)))
        self.assertEqual("999.000", str(EngineerNumber(999, ONE)))
        self.assertEqual("999.200", str(EngineerNumber(999.2, ONE)))
        self.assertEqual("2.000", str(EngineerNumber(2, ONE)))
        self.assertEqual("1.001", str(EngineerNumber(1.001, ONE)))
        self.assertEqual("1.000", str(EngineerNumber(1, ONE)))

    def test_same_value_different_argument(self):
        # same result
        self.assertEqual("1.000m", str(EngineerNumber(0.001, ONE)))
        self.assertEqual("1.000m", str(EngineerNumber(1, MILLI)))
        self.assertEqual("1.000m", str(EngineerNumber(1000, MICRO)))

    def test_as_number(self):
        u1 = EngineerNumber(1, MICRO)
        n4 = EngineerNumber(4, NANO)
        self.assertRaises
        self.assertEqual("1.004u", str(u1 + n4))
        self.assertEqual("996.000n", str(u1 - n4))
        self.assertEqual("250.000", str(u1 / n4))
        self.assertEqual("249.000", str(u1 // n4))
        self.assertEqual("4.000n", str(u1 % n4))
        div, mod = divmod(u1, n4)
        self.assertEqual("249.000", str(div))
        self.assertEqual("4.000n", str(mod))

    def test_round(self):
        self.assertEqual( "999.999m", str(EngineerNumber("0.9999994")))
                                                        #      123
        self.assertEqual("1000.000m", str(EngineerNumber("0.9999995")))

        u1 = EngineerNumber(1, MICRO)
        n4 = EngineerNumber(4, NANO)
        self.assertEqual("1000.000m", str(pow(u1, n4))) # 0.9999999447379593
        self.assertEqual("999.981m", str(pow(n4, u1)))  # 0.9999806632154822
        self.assertEqual(0.9999999447379593, pow(u1, n4.num))

    def test_zero_neg_pos(self):
        self.assertEqual(0, EngineerNumber("0"))

        neg1 = EngineerNumber(-1, ONE)
        self.assertEqual("-1.000", str(neg1))
        u1 = EngineerNumber(1, MICRO)
        self.assertEqual("0.000", str(EngineerNumber(0)))
        self.assertEqual(-0.000001, -u1)
        self.assertEqual(0.000001, math.fabs(-u1))

    def test_basic_calc(self):
        u1 = EngineerNumber(1, MICRO)
        self.assertEqual("2.000", str(EngineerNumber(16) % EngineerNumber(7)))
        self.assertEqual("2.000", str(16 % EngineerNumber(7)))
        self.assertEqual("2.000", str(EngineerNumber(16) % 7))

        self.assertEqual("9.000", str(EngineerNumber(16) - EngineerNumber(7)))
        self.assertEqual("9.000", str(16 - EngineerNumber(7)))
        self.assertEqual("9.000", str(EngineerNumber(16) - 7))

        self.assertEqual("128.000", str(EngineerNumber(2) ** EngineerNumber(7)))
        self.assertEqual("128.000", str(2 ** EngineerNumber(7)))
        self.assertEqual("128.000", str(EngineerNumber(2) ** 7))

        self.assertEqual("2.286", str(EngineerNumber(16) / EngineerNumber(7)))
        self.assertEqual("2.286", str(16 / EngineerNumber(7)))
        self.assertEqual("2.286", str(EngineerNumber(16) / 7))

        self.assertEqual("2.000", str(EngineerNumber(16) // EngineerNumber(7)))
        self.assertEqual("2.000", str(16 // EngineerNumber(7)))
        self.assertEqual("2.000", str(EngineerNumber(16) // 7))

        self.assertEqual("2.286M", str(EngineerNumber(16, MEGA) / EngineerNumber(7)))
        self.assertEqual("2.286M", str(16 / EngineerNumber(7, MICRO)))
        self.assertEqual("2.286M", str(EngineerNumber(16, MEGA) / 7))

        self.assertEqual("1.000u", str(EngineerNumber(u1)))

    def test_121_484(self):
        self.assertEqual("121.484m", str(EngineerNumber("121.484m")))
        self.assertEqual(121.484, EngineerNumber("121.484").num)
        self.assertEqual(121.484, EngineerNumber("121.484"))
        self.assertEqual(EngineerNumber("121.484"), 121.484)
        self.assertEqual("121.484", str(EngineerNumber("121.484")))
        self.assertEqual("121.484E", str(EngineerNumber("121.484E")))

        self.assertEqual("121.488p", str(EngineerNumber(121.488, PICO)))
        self.assertEqual("121.488p", str(EngineerNumber(0.121488, NANO)))

    def test_num_dived_by_enm(self):
        self.assertIsInstance(math.sqrt(EngineerNumber("150p")), float)
        self.assertIsInstance(2 * math.pi * math.sqrt(EngineerNumber("150p")), float)
        self.assertIsInstance(EngineerNumber(1) / (2 * math.pi * math.sqrt(EngineerNumber("150p") * EngineerNumber("600u"))), EngineerNumber)

    def test_equal_different_value_and_factor(self):
        self.assertEqual(EngineerNumber(121.484, KILO), EngineerNumber(0.121484, MEGA))
        self.assertEqual(EngineerNumber(121.484, MILLI), EngineerNumber(0.121484, ONE))
        self.assertEqual(EngineerNumber(121.484, PICO), EngineerNumber(0.121484, NANO))
        self.assertEqual(str(EngineerNumber(121.488, PICO)), str(EngineerNumber(0.121488, NANO)))

    def test_equal_with_number(self):
        self.assertEqual(121484000000000000000, EngineerNumber("121.484E").num)
        self.assertEqual(121484000000000000000, EngineerNumber("121.484E"))

    def test_compare_with_same_instance(self):
        self.assertGreater(EngineerNumber("1.000"), EngineerNumber("0.999"))
        self.assertGreaterEqual(EngineerNumber("1.000"), EngineerNumber("0.999"))
        self.assertGreaterEqual(EngineerNumber("1.000"), EngineerNumber("1.000"))

        self.assertLess(EngineerNumber("0.999"), EngineerNumber("1.000"))
        self.assertLessEqual(EngineerNumber("0.999"), EngineerNumber("0.999"))
        self.assertLessEqual(EngineerNumber("1"), EngineerNumber("1.000"))

    def test_around_yotta(self):
        yotta999999 = EngineerNumber("999.999Y")
        self.assertEqual("999.999Y", str(yotta999999))

        # over yotta a little
        yotta = EngineerNumber(1, YOTTA)
        self.assertEqual("1.000Y", str(yotta))
        yotta1 = yotta + 1
        self.assertEqual("1.000Y", str(yotta1))
        self.assertEqual("1000000000000000000000001", str(yotta1.num))

    def test___si2exponent10(self):
        self.assertEqual(0, EngineerNumber._si2exponent10(""))
        self.assertEqual(3, EngineerNumber._si2exponent10("k"))
        self.assertEqual(24, EngineerNumber._si2exponent10("Y"))
        self.assertEqual(-24, EngineerNumber._si2exponent10("y"))

    def test__si2exponent10_wrong(self):
        expected_header_en = "SI prefix symbol must be in ("
        expected_header_ja = \
            _("SI 接頭辞の記号は、次のいずれかでなければなりません。{}")
        symbols = (\
             '("Y", "Z", "E", "P", "T", "G", "M", "k", "h", "da", '
             '"", '
             '"d", "c", "%", "m", "u", "n", "p", "f", "a", "z", "y")'
        )
        expected_message = \
            expected_header_en + symbols + "."
        expected_message = \
            expected_header_ja.format(symbols)

        with self.assertRaises(KeyError) as raiz:
            EngineerNumber._si2exponent10("Q")
        self.assertEqual(expected_message, raiz.exception.args[0])

        with self.assertRaises(KeyError) as raiz:
            EngineerNumber._si2exponent10("K")
        self.assertEqual(expected_message, raiz.exception.args[0])

        with self.assertRaises(KeyError) as raiz:
            EngineerNumber._si2exponent10("GG")
        self.assertEqual(expected_message, raiz.exception.args[0])

        with self.assertRaises(KeyError) as raiz:
            EngineerNumber._si2exponent10(" ")
        self.assertEqual(expected_message, raiz.exception.args[0])

    def test_e_expression(self):
        self.assertAlmostEqual(float("4e-28"), EngineerNumber("4e-28"))
        self.assertAlmostEqual(float("4e-28"), EngineerNumber("4E-28"))
        self.assertEqual("4e-28", str(EngineerNumber("4e-28")))
        self.assertEqual("4e-28", str(EngineerNumber("4E-28")))

    def test_unknown_symbol(self):
        unknown_symbols = """!@#$^&*(){}[]+-=|_~`'"?<>,/\;:"""
        for unknown_symbol in unknown_symbols:
            with self.assertRaises(KeyError) as raiz:
                try:
                    EngineerNumber("10{}".format(unknown_symbol))
                except ValueError as e:
                    print("unknown_symbol = \"{}\"".format(unknown_symbol))

    def test_percent(self):
        self.assertEqual(EngineerNumber(0.1), EngineerNumber("10%"))
        self.assertEqual(EngineerNumber("0.1"), EngineerNumber("10%"))
        self.assertEqual("100.000m", str(EngineerNumber("10%")))
        self.assertAlmostEqual(0.1, EngineerNumber("10%"))

    def test_over_100_percent(self):
        self.assertEqual(EngineerNumber(1.1), EngineerNumber("110%"))
        self.assertEqual(EngineerNumber("1.1"), EngineerNumber("110%"))
        self.assertAlmostEqual(1.1, EngineerNumber("110%"))
        self.assertEqual("1.100", str(EngineerNumber("110%")))

    def test_compare_with_number(self):
        # swap
        self.assertGreater(EngineerNumber("1.000"), 0.999)
        self.assertGreaterEqual(EngineerNumber("1.000"), 0.999)
        self.assertGreaterEqual(EngineerNumber("1.000"), 1.000)
        self.assertGreater(1.0, EngineerNumber("0.999"))
        self.assertGreaterEqual(1.0, EngineerNumber("0.999"))
        self.assertGreaterEqual(1.0, EngineerNumber("1.000"))
        self.assertGreater(EngineerNumber("1.000"), 0)
        self.assertGreaterEqual(EngineerNumber("1.000"), 0)
        self.assertGreaterEqual(EngineerNumber("1.000"), 1)
        self.assertGreater(1, EngineerNumber("0.999"))
        self.assertGreaterEqual(1, EngineerNumber("0.999"))
        self.assertGreaterEqual(1, EngineerNumber("1.000"))

        self.assertLess(0.999, EngineerNumber("1.000"))
        self.assertLessEqual(0.999, EngineerNumber("0.999"))
        self.assertLessEqual(1, EngineerNumber("1.000"))

    def test_bool(self):
        self.assertTrue(EngineerNumber("1.000"))
        self.assertTrue(EngineerNumber("1.000p"))
        self.assertTrue(EngineerNumber(1, PICO))
        self.assertFalse(EngineerNumber("0.000"))

    def test_si_prefix_symbol_error(self):
        with self.assertRaises(KeyError) as raiz:
            EngineerNumber("100K")
      # message = ("cannot accept "K" as SI prefix symbol. "
      #            "please use "k" as prefix if you hope to describe kilo."
      #            "Because "K" means Kelbin celcius.")
        message = _('"K" を SI 接頭辞の記号として使用することは出来ません。\n'
                   'kilo を表現したい場合、 "K" ではなく、小文字の "k" を'
                   'お使い下さい。\n'
                   'なぜならば、"K" は、Kelvin 温度を表現するための'
                   '単位記号だからです。')
        self.assertEqual(message, raiz.exception.args[0])

    def test_force(self):
        one = EngineerNumber("1")
        self.assertEqual("1.000", str(one))
        self.assertEqual("1000.000m", one._force("m"))
        self.assertEqual("0.001k", one._force("k"))
        self.assertEqual("1000.000m", one["m"])
        self.assertEqual("0.001k", one["k"])
        self.assertEqual("1.000", one[""])

        m1 = EngineerNumber("1m")
        self.assertEqual("1.000m", str(m1))
        self.assertEqual("1000.000u", m1._force("u"))
        self.assertEqual("1000.000u", m1["u"])
        self.assertEqual("0.001", m1[""])
        self.assertEqual("1000000.000n", m1["n"])

        k1 = EngineerNumber("123.456k")
        self.assertEqual("123.456k", k1["k"])
        self.assertEqual("123456.000", k1[""])
        self.assertEqual("123456000000000000.000p", k1["p"])

        m1234567 = EngineerNumber("1.234567m")
        self.assertEqual("1.235m", str(m1234567))
        self.assertEqual("1234.567u", m1234567._force("u"))
        self.assertEqual("1234.567u", m1234567["u"])
        self.assertEqual("0.001", m1234567[""])

        m1534567 = EngineerNumber("1.534567m")
        self.assertEqual("0.002", m1534567[""])
        self.assertEqual("1.535m", str(m1534567))
        self.assertEqual("1534.567u", m1534567._force("u"))
        self.assertEqual("1534.567u", m1534567["u"])

    def test_si_units(self):
        # base
        one_meter = EngineerNumber("1")
        one_deca = EngineerNumber("1da")
        one_hecto_pascal = EngineerNumber("1h")

        one_little = EngineerNumber("1")
        one_deci_little = EngineerNumber("1d")
        one_centi_meter = EngineerNumber("1c")

        self.assertEqual(one_meter, 100 * one_centi_meter)
        self.assertEqual(one_little, 10 * one_deci_little)

        self.assertEqual(EngineerNumber("0.1k"), one_hecto_pascal)
        self.assertEqual(1, one_deca / 10)

    def test_error_and_warning(self):
        n1 = EngineerNumber("0.1m")
      # message = "abs\(number\(={}\)\) in range\(0, 1\) convert to int.".format(n1)
        message = _("0 < abs(number(={})) < 1 を満たす数字を "
                    "int に変換しようとしました。").format(n1)

        with self.assertRaises(UserWarning) as warn1:
            int(n1)
        self.assertEqual(message, warn1.exception.args[0])

        n2 = EngineerNumber("-0.1m")
      # message = "abs\(number\(={}\)\) in range\(0, 1\) convert to int.".format(n2)
        message = _("0 < abs(number(={})) < 1 を満たす数字を "
                    "int に変換しようとしました。").format(n2)
        with self.assertRaises(UserWarning) as warn2:
            int(n2)
        self.assertEqual(message, warn2.exception.args[0])

    def test_math(self):
        two = EngineerNumber("2")
        root2 = math.sqrt(2)

        sqrt2 = two.sqrt()
        self.assertEqual(2, two)
        self.assertEqual(root2, sqrt2)
        self.assertIsInstance(sqrt2, EngineerNumber)

    def test_error(self):
        # base
        k1000 = EngineerNumber("1.000k")

        # in error
        k1001 = EngineerNumber("1.001k")
        k1010 = EngineerNumber("1.010k")

        # eq error
        k1050 = EngineerNumber("1.050k")

        # out error
        k1051 = EngineerNumber("1.051k")
        k1100 = EngineerNumber("1.100k")
        k2000 = EngineerNumber("2.000k")

        self.assertTrue(k1000.in_tolerance_error(k1000, TOLERANCE_ERROR))
        self.assertTrue(k1000.in_tolerance_error(k1010, TOLERANCE_ERROR))

        self.assertTrue(k1000.in_tolerance_error(k1050, TOLERANCE_ERROR))

        self.assertFalse(k1000.in_tolerance_error(k1051, TOLERANCE_ERROR))
        self.assertFalse(k1000.in_tolerance_error(k1100, TOLERANCE_ERROR))
        self.assertFalse(k1000.in_tolerance_error(k2000, TOLERANCE_ERROR))

    def test_wire_instance_as_tuple(self):
        self.assertIsInstance(WIRE["0000"], tuple)

    def test_wire_instance_as_EngineerNumber(self):
        self.assertIsInstance(SWG["0"], EngineerNumber)
        self.assertIsInstance(AWG[10], EngineerNumber)

    def test_wire_as_EngineerNumber(self):
        self.assertEqual(EngineerNumber("10.2m"), WIRE["0000"][SWG_])
        self.assertEqual(EngineerNumber("1.024m"), WIRE[18][AWG_])
        self.assertEqual(EngineerNumber("8.23m"), SWG["0"])
        self.assertEqual(EngineerNumber("2.588m"), AWG[10])

    def test_wire_as_float(self):
        self.assertAlmostEqual(0.0102, WIRE["0000"][SWG_])
        self.assertAlmostEqual(0.001024, WIRE[18][AWG_])
        self.assertAlmostEqual(0.00823, SWG["0"])
        self.assertAlmostEqual(0.002588, AWG[10])

if __name__ == "__main__":
  # gc.set_debug(gc.DEBUG_LEAK)
    unittest.main()
