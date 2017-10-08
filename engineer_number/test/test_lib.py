# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

import os
import sys
import unittest
from test import support

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from engineer_number import *
from engineer_number.constants import *
from engineer_number.lib import get_resistors, make_all_combinations, close_values

class TestEngineerNumberUtil(unittest.TestCase):
    def test_make_all_combinations(self):
        exponent10s = range(ONE, MEGA + 1)
        combs = make_all_combinations("E12", exponent10s)
        tup_combs = tuple(str(x) for x in combs)
        expected = (
            "1.000", "1.200", "1.500", "1.800", "2.200", "2.700", "3.300",
            "3.900", "4.700", "5.600", "6.800", "8.200", "10.000", "12.000",
            "15.000", "18.000", "22.000", "27.000", "33.000", "39.000",
            "47.000", "56.000", "68.000", "82.000", "100.000", "120.000",
            "150.000", "180.000", "220.000", "270.000", "330.000", "390.000",
            "470.000", "560.000", "680.000", "820.000", "1.000k", "1.200k",
            "1.500k", "1.800k", "2.200k", "2.700k", "3.300k", "3.900k",
            "4.700k", "5.600k", "6.800k", "8.200k", "10.000k", "12.000k",
            "15.000k", "18.000k", "22.000k", "27.000k", "33.000k", "39.000k",
            "47.000k", "56.000k", "68.000k", "82.000k", "100.000k", "120.000k",
            "150.000k", "180.000k", "220.000k", "270.000k", "330.000k",
            "390.000k", "470.000k", "560.000k", "680.000k", "820.000k",
            "1.000M", "1.200M", "1.500M", "1.800M", "2.200M", "2.700M",
            "3.300M", "3.900M", "4.700M", "5.600M", "6.800M", "8.200M")
        for x in combs:
            self.assertIsInstance(x, EngineerNumber)
        self.assertEqual(expected, tup_combs)

    def test_make_resistors(self):
        resistors = get_resistors("E12", ORDERS_RESISTOR)

        resistors_ = tuple(str(x) for x in resistors)
        expected = (
            "1.000", "1.200", "1.500", "1.800", "2.200", "2.700", "3.300",
            "3.900", "4.700", "5.600", "6.800", "8.200", "10.000", "12.000",
            "15.000", "18.000", "22.000", "27.000", "33.000", "39.000",
            "47.000", "56.000", "68.000", "82.000", "100.000", "120.000",
            "150.000", "180.000", "220.000", "270.000", "330.000", "390.000",
            "470.000", "560.000", "680.000", "820.000", "1.000k", "1.200k",
            "1.500k", "1.800k", "2.200k", "2.700k", "3.300k", "3.900k",
            "4.700k", "5.600k", "6.800k", "8.200k", "10.000k", "12.000k",
            "15.000k", "18.000k", "22.000k", "27.000k", "33.000k", "39.000k",
            "47.000k", "56.000k", "68.000k", "82.000k", "100.000k", "120.000k",
            "150.000k", "180.000k", "220.000k", "270.000k", "330.000k",
            "390.000k", "470.000k", "560.000k", "680.000k", "820.000k",
            "1.000M", "1.200M", "1.500M", "1.800M", "2.200M", "2.700M",
            "3.300M", "3.900M", "4.700M", "5.600M", "6.800M", "8.200M",
            "10.000M")

        for x in resistors:
            self.assertIsInstance(x, EngineerNumber)

        self.assertEqual(expected, resistors_)

    def test_close_values_eq_up(self):
        resistors = get_resistors("E24", ORDERS_RESISTOR)

        k15 = EngineerNumber(15, 3)
        self.assertEqual(EngineerNumber(15, 3), close_values(k15, "up", resistors))

    def test_close_values_eq_down(self):
        resistors = get_resistors("E24", ORDERS_RESISTOR)
        k15 = EngineerNumber(15, 3)
        self.assertEqual(EngineerNumber(15, 3), close_values(k15, "down", resistors))

    def test_close_values_same_exponent(self):
        k47 = EngineerNumber(47, 3)
        k50 = EngineerNumber(50, 3)
        k56 = EngineerNumber(56, 3)

        resistors = get_resistors("E12", ORDERS_RESISTOR)
        self.assertEqual(k56, close_values(k50, "up", resistors))
        self.assertEqual(k47, close_values(k50, "down", resistors))

    def test_close_values_transfer_next_exponent(self):
        resistors = get_resistors("E12", ORDERS_RESISTOR)

        r83  = EngineerNumber(8.3, 1)
        r100 = EngineerNumber(1.0, 2)
        self.assertEqual(r100, close_values(r83, "up", resistors))

        k094 = EngineerNumber(0.94, 3)
        r820 = EngineerNumber(8.2,  2)
        self.assertEqual(r820, close_values(k094, "down", resistors))

    def test_close_values_out_of_range(self):
        resistors = get_resistors("E12", ORDERS_RESISTOR)
        r0_9 = EngineerNumber(0.9, ONE)
        M101 = EngineerNumber(10.1, MEGA)

        self.assertIsNone(close_values(r0_9, "down", resistors))
        self.assertIsNone(close_values(M101, "up", resistors))

    def test_close_values_at_limit(self):
        resistors = get_resistors("E12", ORDERS_RESISTOR)
        r0_9 = EngineerNumber(0.9, ONE)
        M101 = EngineerNumber(10.1, MEGA)

        self.assertEqual(EngineerNumber(1), close_values(r0_9, "up", resistors))
        self.assertEqual(EngineerNumber("10M"), close_values(M101, "down", resistors))

if __name__ == "__main__":
    unittest.main()
