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
    "SWG", "AWG", "SWG_", "AWG_", "WIRE",
]

# SWG:   Standard Wire Gauge
# AWG:   American Wire Gauge

SWG_ = 0
AWG_ = 1

WIRE_NAMES= {
    "SWG": SWG_,
    "AWG": AWG_,
}

#       GAUGE|  SWG    |  AWG    || GAUGE |  SWG     | AWG    |
#       (No.)|  径[mm] |  径[mm] || (No.) |  経[mm]  | 経[mm] |
WIRE = {
    "0000000": ["12.7m"],
     "000000": ["11.8m"],
      "00000": ["11.0m"],
       "0000": ["10.2m", "11.684m"],
        "000": ["9.45m", "10.404m"],
         "00": ["8.84m",  "9.266m"],
          "0": ["8.23m",  "8.252m"],
            1: ["7.62m",  "7.348m"],    26: ["0.457m", "0.405m"],
            2: ["7.01m",  "6.544m"],    27: ["0.417m", "0.361m"],
            3: ["6.40m",  "5.827m"],    28: ["0.376m", "0.321m"],
            4: ["5.89m",  "5.189m"],    29: ["0.345m", "0.286m"],
            5: ["5.38m",  "4.621m"],    30: ["0.315m", "0.255m"],
            6: ["4.88m",  "4.115m"],    31: ["0.295m", "0.227m"],
            7: ["4.47m",  "3.665m"],    32: ["0.274m", "0.202m"],
            8: ["4.06m",  "3.264m"],    33: ["0.254m", "0.180m"],
            9: ["3.66m",  "2.906m"],    34: ["0.234m", "0.160m"],
           10: ["3.25m",  "2.588m"],    35: ["0.213m", "0.143m"],
           11: ["2.95m",  "2.305m"],    36: ["0.193m", "0.127m"],
           12: ["2.64m",  "2.053m"],    37: ["0.173m", "0.113m"],
           13: ["2.34m",  "1.828m"],    38: ["0.152m", "0.101m"],
           14: ["2.03m",  "1.628m"],    39: ["0.132m", "0.0897m"],
           15: ["1.83m",  "1.450m"],    40: ["0.122m", "0.0799m"],
           16: ["1.63m",  "1.291m"],    41: ["0.112m"],
           17: ["1.42m",  "1.150m"],    42: ["0.102m"],
           18: ["1.22m",  "1.024m"],    43: ["0.091m"],
           19: ["1.02m",  "0.912m"],    44: ["0.081m"],
           20: ["0.914m", "0.812m"],    45: ["0.071m"],
           21: ["0.813m", "0.723m"],    46: ["0.061m"],
           22: ["0.711m", "0.644m"],    47: ["0.050m"],
           23: ["0.610m", "0.573m"],    48: ["0.040m"],
           24: ["0.559m", "0.511m"],    49: ["0.030m"],
           25: ["0.508m", "0.455m"],    50: ["0.025m"],
}

# WIRE["0000"][SWG_] == 10.2
# WIRE[18][AWG_] == 1.024

SWG = {}
AWG = {}
# SWG["0"] == 0.00823
#  AWG[10] == 0.002588

def _build_up_to_EngineerNumber():
    for wire_name, wire_value_ in WIRE_NAMES.items():
        d = globals()[wire_name]
        for No, L in WIRE.items():
            try:
                v = L[wire_value_]
            except IndexError as e:
                continue
            enm = EngineerNumber(v)
            WIRE[No][wire_value_] = enm
            d[No] = enm

    for No, L in WIRE.items():
        tup = tuple(L)
        WIRE[No] = tup # NEVER CHANGE PLEASE.

_build_up_to_EngineerNumber()

# print("WIRE = {}".format(WIRE))
# print("SWG = {}".format(SWG))
# print("AWG = {}".format(AWG))
