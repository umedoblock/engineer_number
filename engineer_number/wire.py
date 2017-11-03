# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

import bisect, collections

from engineer_number.core import EngineerNumber

# 見れば分かると思われる為、特に説明はない。
__all__ = [
    "SWG", "AWG", "BWG", "SWG_", "AWG_", "BWG_", "WIRE",
]

# SWG:   Standard Wire Gauge
# AWG:   American Wire Gauge
# BWG: Birmingham Wire Gauge

SWG_ = 0
AWG_ = 1
BWG_ = 2

WIRE_NAMES= {
    "SWG": SWG_,
    "AWG": AWG_,
    "BWG": BWG_,
}

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
