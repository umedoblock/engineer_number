# NO COPYRIGHT

import bisect, collections

GROUP_OF_DIGITS = 3

ERROR_E6 = 0.20
ERROR_E12 = 0.10
ERROR_E24 = 0.05
ERROR_E96 = 0.01

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
PERCENT = -2
MILLI = -3
MICRO = -6
NANO = -9
PICO = -12
FEMTO = -15
ATTO = -18
ZEPTO = -21
YOCTO = -24

EXPONENT_BIG = (YOTTA, ZETTA, EXA, PETA, TERA, GIGA, MEGA, KILO, HECTO, DECA)
EXPONENT_SMALL = (DECI, CENTI, PERCENT, MILLI, MICRO, NANO, PICO, FEMTO, ATTO, ZEPTO, YOCTO)
EXPONENTS = EXPONENT_BIG + (ONE,) + EXPONENT_SMALL

ORDERS_GIGA=range(GIGA, GIGA+3)
ORDERS_KILO=range(KILO, KILO+3)
ORDERS_MEGA=range(MEGA, MEGA+3)
ORDERS_ONE=range(ONE, ONE+3)
ORDERS_MILLI=range(MILLI, MILLI+3)
ORDERS_MICRO=range(MICRO, MICRO+3)
ORDERS_NANO=range(NANO, NANO+3)
ORDERS_PICO=range(PICO, PICO+3)

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
    ("%", PERCENT),
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

E_SERIES_VALUES = {
    "E6":  (1.0, 1.5, 2.2, 3.3, 4.7, 6.8),

    "E12": (1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2),

    "E24": (1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0,
            3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1),

    # calc "E48", "E96", "E192".
}

_esv = E_SERIES_VALUES
# >>> set(esv["E6"]).issubset(set(esv["E12"]))
# True
# >>> set(esv["E12"]).issubset(set(esv["E24"]))
# True
# >>> set(esv["E48"]).issubset(set(esv["E96"]))
# True
# >>> set(esv["E96"]).issubset(set(esv["E192"]))
# True

# tup = (6, 12, 24)
# for n in tup:
#   for i in range(n):
#     v = round(pow(10, i / n), 1)
#     print("10 ** ({} / {}) = {}".format(i, n, v))
#   print()
# 概ね一致するものの，3.2, 4.6 とかが駄目。

tup = (48, 96, 192)
for n in tup:
  L = []
  for i in range(n):
    v = round(pow(10, i / n + 1), 1)
    L.append(v)
  e_series_name = "E{}".format(n)
  if e_series_name == "E192":
    L.remove(91.9)
    v = 92.0
    index = bisect.bisect(L, v)
    L.insert(index, v)
  _esv[e_series_name] =  tuple(L)

E_SERIES_NAMES = ("E6", "E12", "E24", "E48", "E96", "E192")
