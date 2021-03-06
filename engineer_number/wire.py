# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

from .lib import _build_up_to_EngineerNumber
from ._wire import WIRE

__all__ = [
    "SWG", "AWG", "SWG_", "AWG_", "WIRE",
]

SWG = {}
AWG = {}
# SWG["0"] == 0.00823
#  AWG[10] == 0.002588

SWG_ = 0
AWG_ = 1

# WIRE["0000"][SWG_] == 0.0102
# WIRE[18][AWG_] == 0.001024

_build_up_to_EngineerNumber(WIRE, (SWG, AWG), (SWG_, AWG_))

# print("WIRE = {}".format(WIRE))
# print("SWG = {}".format(SWG))
# print("AWG = {}".format(AWG))
