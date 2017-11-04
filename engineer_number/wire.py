# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

import bisect, collections

from .core import EngineerNumber
from ._wire import WIRE

__all__ = [
    "SWG", "AWG", "SWG_", "AWG_", "WIRE",
]

SWG_ = 0
AWG_ = 1

WIRE_NAMES= {
    "SWG": SWG_,
    "AWG": AWG_,
}

# WIRE["0000"][SWG_] == 0.0102
# WIRE[18][AWG_] == 0.001024

SWG = {}
AWG = {}
# SWG["0"] == 0.00823
#  AWG[10] == 0.002588

def _build_up_to_EngineerNumber():
    for wire_name, wire_value in WIRE_NAMES.items():
        d = globals()[wire_name]
        for No, L in WIRE.items():
            try:
                v = L[wire_value]
            except IndexError as e:
                continue
            enm = EngineerNumber(v)
            WIRE[No][wire_value] = enm
            d[No] = enm

    for No, L in WIRE.items():
        tup = tuple(L)
        WIRE[No] = tup

_build_up_to_EngineerNumber()

# print("WIRE = {}".format(WIRE))
# print("SWG = {}".format(SWG))
# print("AWG = {}".format(AWG))
