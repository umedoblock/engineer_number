import os
import sys
import math
import argparse
import gettext

from engineer_number import *
from engineer_number.constants import *

path_ = os.path.join(os.path.dirname(__file__), '..', 'locale')
# print('path_ =', path_)
gettext.install('engineer_number', path_)
del path_

def look_for_optimized_gain(amp_n, ic, vcc, series="E12"):
    pass

def view_apmlifiered(gaind, top):
    pass

def parse_args():
    parser = argparse.ArgumentParser(description=_('look for optimized Hz.'))

    parser.add_argument('--gain', metavar='N', dest='gain',
                       type=float, nargs='?', default=5,
                       help='gain default: 5')
    parser.add_argument('--vcc', metavar='N', dest='vcc',
                       type=float, nargs='?', default=0.8,
                       help='vcc default: 5.0')
    parser.add_argument('--ic', metavar='N', dest='ic',
                       type=float, nargs='?', default=0.8,
                       help='collect i default: 0.8')
    parser.add_argument("--series", metavar="N", dest="series",
                       nargs="?", default="E12",
                       help="series default: E12")
    parser.add_argument('--top', metavar='N', dest='top',
                       type=int, nargs='?', default=10,
                       help='ranking default: 10')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

    ic = EngineerNumber(args.ic)
    vcc = args.vcc
    gain = args.gain
    top = args.top

    params = look_for_optimized_gain(gain, ic, vcc)

    view_apmlifiered(params, top)

    print()
