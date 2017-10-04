import bisect

from . import EngineerNumber
from engineer_number.constants import *

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

def close_e_series(value, to, e_series_name, orders, tolerance_error=-1.0):
    resistors = get_resistors(e_series_name, orders)
    index = bisect.bisect(resistors, value)
#   print("resistors[index-1]={}".format(resistors[index-1]))
#   print("resistors[index]={}".format(resistors[index]))
#   print("resistors[index+1]={}".format(resistors[index+1]))

    if to == "up":
        # value is up
        if index >= len(resistors):
          return None
          # raise ValueError("cannot choise greater than {}.".format(resistors[index]))
        if value == resistors[index-1]:
            candidate = resistors[index-1]
        else:
            candidate = resistors[index]
    elif to == "down":
        # value is down
        if index == 0:
          return None
          # raise ValueError("cannot choise lesser than {}.".format(resistors[0]))
        candidate = resistors[index-1]
    else:
        raise ValueError("unknown to={}".format(to))

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
def _make_capacitors(e_series_name):
    if hasattr(_capacitors, e_series_name):
        return _capacitors[e_series_name]
    orders_ = range(PICO, PICO + 1)
    # Max capacitance is 6.8 uF in e_series_name="E6"
    _capacitors[e_series_name] = \
        make_all_combinations(e_series_name, orders_)
    return _capacitors

def get_capacitors(e_series_name, orders):
    if not hasattr(_capacitors, e_series_name):
        _make_capacitors(e_series_name, orders)

    return _capacitors[e_series_name]
