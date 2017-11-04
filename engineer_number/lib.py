# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

import bisect

from . import EngineerNumber
from .constants import *

def make_all_combinations(e_series_name, orders):
    if e_series_name in ("E6", "E12", "E24"):
        adjust = 0
    else:
        adjust = 1

    combination = []
    for order in orders:
        values = [EngineerNumber(n, order - adjust) for n in E_SERIES_VALUES[e_series_name]]
        combination.extend(values)
    return combination

def close_values(value, updown, values, tolerance_error=-1.0):
    index = bisect.bisect(values, value)
#   print("values[index-1]={}".format(values[index-1]))
#   print("values[index]={}".format(values[index]))
#   print("values[index+1]={}".format(values[index+1]))

    if updown == "up":
        # value is up
        if index >= len(values):
          return None
          # raise ValueError("cannot choise greater than {}.".format(values[index]))
        if value == values[index-1]:
            candidate = values[index-1]
        else:
            candidate = values[index]
    elif updown == "down":
        # value is down
        if index == 0:
          return None
          # raise ValueError("cannot choise lesser than {}.".format(values[0]))
        candidate = values[index-1]
    else:
        raise ValueError("unknown updown={}".format(updown))

    if tolerance_error < 0:
        return candidate

    if value.in_tolerance_error(candidate, tolerance_error):
        return candidate
    else:
        return None

_resistors = {}
def _make_resistors(e_series_name, orders):
    if hasattr(_resistors, e_series_name):
        return _resistor[e_series_name]
    _resistors[e_series_name] = \
        make_all_combinations(e_series_name, orders)
    if orders[-1] == MEGA:
        _resistors[e_series_name].append(EngineerNumber("10M"))

    return _resistors

def get_resistors(e_series_name, orders):
    if not hasattr(_resistors, e_series_name):
        _make_resistors(e_series_name, orders)

    return _resistors[e_series_name]

_capacitors = {}
def _make_capacitors(e_series_name, orders):
    if hasattr(_capacitors, e_series_name):
        return _capacitors[e_series_name]

    _capacitors[e_series_name] = \
        make_all_combinations(e_series_name, orders)
    return _capacitors

def get_capacitors(e_series_name, orders):
    if not hasattr(_capacitors, e_series_name):
        _make_capacitors(e_series_name, orders)

    return _capacitors[e_series_name]

def _build_up_to_EngineerNumber(regulation, muscles, muscles_names):
    print("regulation={}".format(regulation))
    print("muscles={}".format(muscles))
    print("muscles_names={}".format(muscles_names))
    for name, index in muscles_names.items():
        print("name={}, index={}".format(name, index))
        d = muscles[index]
        for No, L in regulation.items():
            print("No={}, L={}, name={}, index={}".format(No, L, name, index))
            try:
                v = L[index]
            except IndexError as e:
                continue
            enm = EngineerNumber(v)
            regulation[No][index] = enm
            print("d =", d)
            d[No] = enm

    for No, L in regulation.items():
        tup = tuple(L)
        regulation[No] = tup
