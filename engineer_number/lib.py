import bisect

from . import EngineerNumber
from engineer_number.constants import *

def make_all_combinations(e_series_name, exponent10s):
    if e_series_name in ("E6", 'E12', "E24"):
        adjust = 0
    else:
        adjust = 1

    combination = []
    for exponent10 in exponent10s:
        values = [EngineerNumber(n, exponent10 - adjust) for n in E_SERIES_VALUES[e_series_name]]
        combination.extend(values)
    return combination

def close_e_series(value, to, e_series_name, tolerance_error=-1.0):
    resistors = get_resistors(e_series_name)
    index = bisect.bisect(resistors, value)
    if to == "up":
        # value is up
        if index >= len(resistors):
          return None
          # raise ValueError("cannot choise greater than {}.".format(resistors[index]))
        candidate = resistors[index]
    elif to == "down":
        # value is down
        if index == 0:
          return None
          # raise ValueError("cannot choise lesser than {}.".format(resistors[0]))
        candidate = resistors[index-1]
    else:
        raise ValueError("unknown to={}".format(to))

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

    return _resistors[e_series_name]