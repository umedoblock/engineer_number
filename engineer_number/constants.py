# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

from ._constants import *

# separate general expression and original expression.
__all__ = [
    "GROUP_OF_DIGITS", "TOLERANCE_ERROR",
    "YOTTA", "ZETTA", "EXA", "PETA", "TERA", "GIGA", "MEGA", "KILO",
    "HECTO", "DECA",
    "ONE",
    "DECI", "CENTI", "PERCENT",
    "MILLI", "MICRO", "NANO", "PICO", "FEMTO", "ATTO", "ZEPTO", "YOCTO",
    "ORDERS_GIGA", "ORDERS_KILO", "ORDERS_MEGA", "ORDERS_ONE", "ORDERS_MILLI",
    "ORDERS_MICRO", "ORDERS_NANO", "ORDERS_PICO",
    "ORDERS_RESISTOR", "ORDERS_CAPACITOR",
    "EXPONENTS", "d_SYMBOL_EXPONENT", "d_EXPONENT_SYMBOL",
    "E_SERIES_NAMES", "E_SERIES_VALUES",
]

TOLERANCE_ERROR = 0.05

ORDERS_RESISTOR=range(ONE, MEGA + 1)
ORDERS_CAPACITOR=range(PICO, MICRO + 3)

d_EXPONENT_SYMBOL = \
    dict(zip(d_SYMBOL_EXPONENT.values(), d_SYMBOL_EXPONENT.keys()))
