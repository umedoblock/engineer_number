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
"0000":["10.16m","11.68m","11.53m"],  "19": ["1.02m", "0.91m", "1.07m"],
 "000": ["9.45m","10.41m","10.80m"],  "20": ["0.92m", "0.81m", "0.89m"],
  "00": ["8.84m", "9.27m", "9.65m"],  "21": ["0.81m", "0.72m", "0.81m"],
   "0": ["8.23m", "8.25m", "8.64m"],  "22": ["0.71m", "0.64m", "0.71m"],
   "1": ["7.62m", "7.35m", "7.62m"],  "23": ["0.61m", "0.57m", "0.64m"],
   "2": ["7.01m", "6.54m", "7.21m"],  "24": ["0.56m", "0.51m", "0.56m"],
   "3": ["6.40m", "5.83m", "6.58m"],  "25": ["0.51m", "0.45m", "0.51m"],
   "4": ["5.89m", "5.19m", "6.05m"],  "26": ["0.46m", "0.40m", "0.46m"],
   "5": ["5.38m", "4.62m", "5.59m"],  "27": ["0.41m", "0.36m", "0.41m"],
   "6": ["4.88m", "4.11m", "5.16m"],  "28": ["0.38m", "0.32m", "0.356m"],
   "7": ["4.47m", "3.66m", "4.57m"],  "29": ["0.35m", "0.29m", "0.33m"],
   "8": ["4.06m", "3.26m", "4.19m"],  "30": ["0.305m","0.25m", "0.305m"],
   "9": ["3.66m", "2.90m", "3.76m"],  "31": ["0.29m", "0.23m", "0.254m"],
  "10": ["3.25m", "2.59m", "3.40m"],  "32": ["0.27m", "0.20m", "0.299m"],
  "11": ["2.95m", "2.30m", "3.05m"],  "33": ["0.254m","0.18m", "0.203m"],
  "12": ["2.64m", "2.05m", "2.77m"],  "34": ["0.229m","0.16m", "0.178m"],
  "13": ["2.34m", "1.83m", "2.41m"],  "35": ["0.203m","0.14m", "0.127m"],
  "14": ["2.03m", "1.63m", "2.11m"],  "36": ["0.178m","0.13m", "0.102m"],
  "15": ["1.83m", "1.45m", "1.83m"],  "37": ["0.17m", "0.11m"],
  "16": ["1.63m", "1.29m", "1.65m"],  "38": ["0.15m", "0.10m"],
  "17": ["1.42m", "1.15m", "1.47m"],  "39": ["0.127m","0.08m"],
  "18": ["1.22m", "1.02m", "1.24m"],
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

from .core import EngineerNumber

def _build_up_to_EngineerNumber():
    for wire_name, wire_value_ in WIRE_NAMES.items():
        d = globals()[wire_name]
        for No, L in WIRE.items():
            if No in ("37", "38", "39") and wire_value_ == BWG_:
                continue
            enm = EngineerNumber(L[wire_value_])
          # print("wire_name={}, wire_value_={}, No={}, enm={}".format(wire_name, wire_value_, No, enm))
            WIRE[No][wire_value_] = enm
            d[No] = enm

    for No, L in WIRE.items():
        tup = tuple(L)
        WIRE[No] = tup # NEVER CHANGE PLEASE.

_build_up_to_EngineerNumber()

# print("WIRE = {}".format(WIRE))
# print("SWG = {}".format(SWG))
# print("AWG = {}".format(AWG))
# print("BWG = {}".format(BWG))
