import collections

# 見れば分かると思われる為、特に説明はない。
__all__ = [
    "GROUP_OF_DIGITS", "TOLERANCE_ERROR",
    "YOTTA", "ZETTA", "EXA", "PETA", "TERA", "GIGA", "MEGA", "KILO",
    "HECTO", "DECA",
    "ONE",
    "DECI", "CENTI",
    "MILLI", "MICRO", "NANO", "PICO", "FEMTO", "ATTO", "ZEPTO", "YOCTO",
    "ORDERS_GIGA", "ORDERS_KILO", "ORDERS_MEGA", "ORDERS_ONE", "ORDERS_MILLI",
    "ORDERS_MICRO", "ORDERS_NANO", "ORDERS_PICO",
    "ORDERS_RESISTOR", "ORDERS_CAPASITOR",
    "EXPONENTS", "d_SYMBOL_EXPONENT", "d_EXPONENT_SYMBOL",
    "E_SERIES_NAMES", "E_SERIES_VALUES",
]

GROUP_OF_DIGITS = 3

TOLERANCE_ERROR = 0.05

YOTTA = 24
ZETTA = 21
EXA = 18 # means 10 ** 18
PETA = 15
TERA = 12
GIGA = 9
MEGA = 6
KILO = 3
HECTO = 2
DECA = 1
ONE = 0
DECI = -1
CENTI = -2
MILLI = -3
MICRO = -6
NANO = -9
PICO = -12
FEMTO = -15
ATTO = -18
ZEPTO = -21
YOCTO = -24

EXPONENT_BIG = (YOTTA, ZETTA, EXA, PETA, TERA, GIGA, MEGA, KILO, HECTO, DECA)
EXPONENT_SMALL = (DECI, CENTI, MILLI, MICRO, NANO, PICO, FEMTO, ATTO, ZEPTO, YOCTO)
EXPONENTS = EXPONENT_BIG + (ONE,) + EXPONENT_SMALL

ORDERS_GIGA=range(GIGA, GIGA+3)
ORDERS_KILO=range(KILO, KILO+3)
ORDERS_MEGA=range(MEGA, MEGA+3)
ORDERS_ONE=range(ONE, ONE+3)
ORDERS_MILLI=range(MILLI, MILLI+3)
ORDERS_MICRO=range(MICRO, MICRO+3)
ORDERS_NANO=range(NANO, NANO+3)
ORDERS_PICO=range(PICO, PICO+3)

ORDERS_RESISTOR=range(ONE, MEGA + 1)
ORDERS_CAPASITOR=range(PICO, MICRO + 3)

d_SYMBOL_EXPONENT = collections.OrderedDict((
    ("Y", YOTTA),
    ("Z", ZETTA),
    ("E", EXA),
    ("P", PETA),
    ("T", TERA),
    ("G", GIGA),
    ("M", MEGA),
    ("k", KILO),
    ("h", HECTO),
    ("da", DECA),
     ("", ONE),
    ("d", DECI),
    ("c", CENTI),
    ("m", MILLI),
    ("u", MICRO),
    ("n", NANO),
    ("p", PICO),
    ("f", FEMTO),
    ("a", ATTO),
    ("z", ZEPTO),
    ("y", YOCTO),
))

d_EXPONENT_SYMBOL = \
    dict(zip(d_SYMBOL_EXPONENT.values(), d_SYMBOL_EXPONENT.keys()))

E_SERIES_NAMES = ("E6", "E12", "E24", "E48", "E96", "E192")

E_SERIES_VALUES = {
    "E6":  (1.0, 1.5, 2.2, 3.3, 4.7, 6.8),

    "E12": (1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2),

    "E24": (1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0,
            3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1),

    "E48":
     (10.0, 10.5, 11.0, 11.5, 12.1, 12.7, 13.3, 14.0, 14.7, 15.4, 16.2, 16.9,
      17.8, 18.7, 19.6, 20.5, 21.5, 22.6, 23.7, 24.9, 26.1, 27.4, 28.7, 30.1,
      31.6, 33.2, 34.8, 36.5, 38.3, 40.2, 42.2, 44.2, 46.4, 48.7, 51.1, 53.6,
      56.2, 59.0, 61.9, 64.9, 68.1, 71.5, 75.0, 78.7, 82.5, 86.6, 90.9, 95.3),

    "E96":
     (10.0, 10.2, 10.5, 10.7, 11.0, 11.3, 11.5, 11.8, 12.1, 12.4, 12.7, 13.0,
      13.3, 13.7, 14.0, 14.3, 14.7, 15.0, 15.4, 15.8, 16.2, 16.5, 16.9, 17.4,
      17.8, 18.2, 18.7, 19.1, 19.6, 20.0, 20.5, 21.0, 21.5, 22.1, 22.6, 23.2,
      23.7, 24.3, 24.9, 25.5, 26.1, 26.7, 27.4, 28.0, 28.7, 29.4, 30.1, 30.9,
      31.6, 32.4, 33.2, 34.0, 34.8, 35.7, 36.5, 37.4, 38.3, 39.2, 40.2, 41.2,
      42.2, 43.2, 44.2, 45.3, 46.4, 47.5, 48.7, 49.9, 51.1, 52.3, 53.6, 54.9,
      56.2, 57.6, 59.0, 60.4, 61.9, 63.4, 64.9, 66.5, 68.1, 69.8, 71.5, 73.2,
      75.0, 76.8, 78.7, 80.6, 82.5, 84.5, 86.6, 88.7, 90.9, 93.1, 95.3, 97.6),

    "E192":
      (10.0, 10.1, 10.2, 10.4, 10.5, 10.6, 10.7, 10.9, 11.0, 11.1, 11.3, 11.4,
       11.5, 11.7, 11.8, 12.0, 12.1, 12.3, 12.4, 12.6, 12.7, 12.9, 13.0, 13.2,
       13.3, 13.5, 13.7, 13.8, 14.0, 14.2, 14.3, 14.5, 14.7, 14.9, 15.0, 15.2,
       15.4, 15.6, 15.8, 16.0, 16.2, 16.4, 16.5, 16.7, 16.9, 17.2, 17.4, 17.6,
       17.8, 18.0, 18.2, 18.4, 18.7, 18.9, 19.1, 19.3, 19.6, 19.8, 20.0, 20.3,
       20.5, 20.8, 21.0, 21.3, 21.5, 21.8, 22.1, 22.3, 22.6, 22.9, 23.2, 23.4,
       23.7, 24.0, 24.3, 24.6, 24.9, 25.2, 25.5, 25.8, 26.1, 26.4, 26.7, 27.1,
       27.4, 27.7, 28.0, 28.4, 28.7, 29.1, 29.4, 29.8, 30.1, 30.5, 30.9, 31.2,
       31.6, 32.0, 32.4, 32.8, 33.2, 33.6, 34.0, 34.4, 34.8, 35.2, 35.7, 36.1,
       36.5, 37.0, 37.4, 37.9, 38.3, 38.8, 39.2, 39.7, 40.2, 40.7, 41.2, 41.7,
       42.2, 42.7, 43.2, 43.7, 44.2, 44.8, 45.3, 45.9, 46.4, 47.0, 47.5, 48.1,
       48.7, 49.3, 49.9, 50.5, 51.1, 51.7, 52.3, 53.0, 53.6, 54.2, 54.9, 55.6,
       56.2, 56.9, 57.6, 58.3, 59.0, 59.7, 60.4, 61.2, 61.9, 62.6, 63.4, 64.2,
       64.9, 65.7, 66.5, 67.3, 68.1, 69.0, 69.8, 70.6, 71.5, 72.3, 73.2, 74.1,
       75.0, 75.9, 76.8, 77.7, 78.7, 79.6, 80.6, 81.6, 82.5, 83.5, 84.5, 85.6,
       86.6, 87.6, 88.7, 89.8, 90.9, 92.0, 93.1, 94.2, 95.3, 96.5, 97.6, 98.8),
}
