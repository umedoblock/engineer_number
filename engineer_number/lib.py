import bisect

from . import EngineerNumber
from engineer_number.constants import *

def make_all_combinations(e_series_name, exponent10s):
#   print("make_all_combinations(e_series_name={}, exponent10s={})".format(e_series_name, exponent10s))
    # exponent10s must be asc order.
    if e_series_name in ("E6", 'E12', "E24"):
        adjust = 0
    else:
        adjust = 1
#   print("make_all_combinations(adjust={})".format(adjust))

    combination = []
#   print("E_SERIES_VALUES[e_series_name={}] = {}".format(e_series_name, E_SERIES_VALUES[e_series_name]))
    for exponent10 in exponent10s:
        values = [EngineerNumber(n, exponent10 - adjust) for n in E_SERIES_VALUES[e_series_name]]
        combination.extend(values)
    return combination

def close_e_series(value, to, e_series_name, tolerance_error):
    resistors = get_resistors(e_series_name)
    index = bisect.bisect(resistors, value)
#   print("index={} >= len(resistors)={}".format(index, len(resistors)))
    # value < E12[index]
    if to == "up":
        # value is up
        if index >= len(resistors):
          return None
          # raise ValueError("cannot choise greater than {}.".format(resistors[-1]))
        candidate = resistors[index]
    elif to == "down":
        # value is down
        if index == 0:
          return None
          # raise ValueError("cannot choise lesser than {}.".format(resistors[0]))
        candidate = resistors[index-1]
    else:
        raise ValueError("unknown to={}".format(to))
#   print("value={}, to={}, index={}, resistors[index-1]={}, resistors[index]={}, resistors[index+1]={}".format(value, to, index,  resistors[index-1], resistors[index], resistors[index+1]))

#   print("value={}, candidate={}, value.error(candidate)={}".format(value, candidate, value.error(candidate)))
    return candidate
    if value.in_tolerance_error(candidate, tolerance_error):
        return candidate
    else:
        return None

_resistors = {}
def _make_resistors():
    if _resistors:
        return _resistors
    # exponent10s must be asc order.
    exponent10s_ = range(ONE, MEGA + 1)
    for e_series_name in E_SERIES_VALUES.keys():
        _resistors[e_series_name] = \
            make_all_combinations(e_series_name, exponent10s_)
        _resistors[e_series_name].append(EngineerNumber("10M"))
    return _resistors

def get_resistors(e_series_name):
    if not _resistors:
        _make_resistors()

#   for name, values in _resistors.items():
#       print("name =", name)
#       print("values =", values)
#       print()

#   print("get_resistors(e_series_name={})".format(e_series_name))

    return _resistors[e_series_name]

