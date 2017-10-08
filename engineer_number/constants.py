import bisect, collections

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
    "ORDERS_RESISTOR", "ORDERS_CAPACITOR",
    "EXPONENTS", "d_SYMBOL_EXPONENT", "d_EXPONENT_SYMBOL",
    "E_SERIES_NAMES", "E_SERIES_VALUES",
    "SWG", "AWG", "BWG", "SWG_", "AWG_", "BWG_", "WIRE",
]

GROUP_OF_DIGITS = 3

TOLERANCE_ERROR = 0.05
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
ORDERS_CAPACITOR=range(PICO, MICRO + 3)

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

    # calc "E48", "E96", "E192".
}

esv = E_SERIES_VALUES
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
  esv[e_series_name] =  tuple(L)

###############################################################################
# WIRE SECTION
SWG_ = 0
AWG_ = 1
BWG_ = 2

WIRE_NAMES= {
    "SWG": SWG_,
    "AWG": AWG_,
    "BWG": BWG_,
}

# SWG:   Standard Wire Gauge
# AWG:   American Wire Gauge
# BWG: Birmingham Wire Gauge
# 線番 | SWG    | AWG    | BWG    || 線番  | SWG    | AWG    |  BWG   |
# (No.)| 径[mm] | 径[mm] | 経[mm] || (No.) | 経[mm] | 経[mm] | 経[mm] |
WIRE = {
 "0000":  (10.16,   11.68,  11.53),    "19":   (1.02,    0.91,   1.07),
  "000":   (9.45,   10.41,  10.80),    "20":   (0.92,    0.81,   0.89),
   "00":   (8.84,    9.27,   9.65),    "21":   (0.81,    0.72,   0.81),
    "0":   (8.23,    8.25,   8.64),    "22":   (0.71,    0.64,   0.71),
    "1":   (7.62,    7.35,   7.62),    "23":   (0.61,    0.57,   0.64),
    "2":   (7.01,    6.54,   7.21),    "24":   (0.56,    0.51,   0.56),
    "3":   (6.40,    5.83,   6.58),    "25":   (0.51,    0.45,   0.51),
    "4":   (5.89,    5.19,   6.05),    "26":   (0.46,    0.40,   0.46),
    "5":   (5.38,    4.62,   5.59),    "27":   (0.41,    0.36,   0.41),
    "6":   (4.88,    4.11,   5.16),    "28":   (0.38,    0.32,   0.356),
    "7":   (4.47,    3.66,   4.57),    "29":   (0.35,    0.29,   0.33),
    "8":   (4.06,    3.26,   4.19),    "30":   (0.305,   0.25,   0.305),
    "9":   (3.66,    2.90,   3.76),    "31":   (0.29,    0.23,   0.254),
   "10":   (3.25,    2.59,   3.40),    "32":   (0.27,    0.20,   0.299),
   "11":   (2.95,    2.30,   3.05),    "33":   (0.254,   0.18,   0.203),
   "12":   (2.64,    2.05,   2.77),    "34":   (0.229,   0.16,   0.178),
   "13":   (2.34,    1.83,   2.41),    "35":   (0.203,   0.14,   0.127),
   "14":   (2.03,    1.63,   2.11),    "36":   (0.178,   0.13,   0.102),
   "15":   (1.83,    1.45,   1.83),    "37":   (0.17,    0.11),
   "16":   (1.63,    1.29,   1.65),    "38":   (0.15,    0.10),
   "17":   (1.42,    1.15,   1.47),    "39":   (0.127,   0.08),
   "18":   (1.22,    1.02,   1.24),
}
# WIRE["0000"][SWG_] == 10.16
# WIRE["18"][AWG_] == 1.02
# WIRE["36"][BWG_] == 0.102

SWG = {}
AWG = {}
BWG = {}
# SWG["0"] == 8.23
# AWG["10"] == 2.59
# BWG["20"] == 0.89
for wire_name, wire_value_ in WIRE_NAMES.items():
    d = locals()[wire_name]
    for No, tup in WIRE.items():
        if No in ("37", "38", "39") and wire_value_ == BWG_:
            continue
        d[No] = tup[wire_value_]
# print("SWG = {}".format(SWG))
# print("AWG = {}".format(AWG))
# print("BWG = {}".format(BWG))
