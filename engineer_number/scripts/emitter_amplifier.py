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

def _make_all_combination(series='E12'):
    if series != 'E12':
        raise ValueError(_('series must be "E12".'))
    #                         k                    M
    factor_big = (1, 10, 100, 1000, 10000, 100000, 1000000)
    combination = []
    for factor in factor_big:
        for n in getattr(constants, series):
            v = EngineerNumber(factor * n)
            combination.append(v)
    return combination

def look_for_optimized_gain(gain, ic, Vcc, hfe=200, series="E12"):
    if not series in ("E12",):
        raise ValueError("series must be in E12, E24, E48, E96 or E192.")
    print("series =", series)
    Rs = _make_all_combination(series)
    Rs.append(10 * MEGA)

    parameters = []
    for Rc in Rs:
        ie = ic
        ie = ic + ic / hfe

        Vc = Rc * ic   # 6
        Ve = Vc / gain
        Re = Ve / ie

      # Vc = Rc * ic   # 6
      # Re = Rc / gain # 5
      # Ve = ie * Re

        # 注意
        # must be Vc + Ve <= Vcc
        if Vc + Ve > Vcc:
          # raise ValueError("invalid Vc and Ve combination compare Vcc.")
            print("invalid Vc={} and Ve={} combination compare Vcc={}.".format(Vcc, Vc, Ve, Vcc))
            continue

        Vce = Vcc - (Vc + Ve) # 7

        Pce = Vce * ic        # 8
        # Pce は小さきこと。
        # 2SC1815 の場合，
        # Pce < 400mW(=PD)

        Vb = Ve + 0.6 # 9
        # hfe = 200 # 10
        ib = ic / hfe # ?
        ibias = 10 * ib # 11

        Rb2 = Vb / ibias # 12
        Vcb = Vcc - Vb
        Rb1 = Vcb / ibias # 13

        Rb2_ = Rb2 # E12 にあわす
        Rb1_ = Rb1 # E12 にあわす
        Radd = Rb1_ + Rb2_

        ibias_ = Vcc / Radd

        tup = (Rb1_, Rb2_, Rc, Re, ic, gain, Vcc, Vc, Ve, Vb, Vce, ib, ibias, Pce)
        parameters.append(tup)

    parameters.sort(key=lambda x: math.fabs(x[-1]))
    return parameters

def view_apmlifiered(gained, top=-1):
    fmt = ", ".join(["{!s:>8s}"] * 14)
    print(fmt.format("Rb1_", "Rb2_", "Rc", "Re", "ic", "gain", "Vcc", "Vc", "Ve", "Vb", "Vce", "ib", "ibias", "Pce"))
    for Rb1_, Rb2_, Rc, Re, ic, gain, Vcc, Vc, Ve, Vb, Vce, ib, ibias, Pce in parameters[:top]:
        print(fmt.format(Rb1_, Rb2_, Rc, Re, ic, gain, Vcc, Vc, Ve, Vb, Vce, ib, ibias, Pce))

def parse_args():
    parser = argparse.ArgumentParser(description=_('look for optimized Hz.'))

    parser.add_argument('--gain', metavar='N', dest='gain',
                       type=float, nargs='?', default=5,
                       help='gain default: 5')
    parser.add_argument('--Vcc', metavar='N', dest='Vcc',
                       type=float, nargs='?', default=5.0,
                       help='Vcc default: 5.0')
    parser.add_argument('--ic', metavar='N', dest='ic',
                       nargs='?', default=EngineerNumber("0.8m"),
                       help='collect i default: 0.8m')
    parser.add_argument("--series", metavar="N", dest="series",
                       nargs="?", default="E12",
                       help="series default: E12")
    parser.add_argument('--hfe', metavar='N', dest='hfe',
                       type=int, nargs='?', default=200,
                       help='hfe default: 200')
    parser.add_argument('--top', metavar='N', dest='top',
                       type=int, nargs='?', default=10,
                       help='ranking default: 10')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

    ic = EngineerNumber(args.ic)
    Vcc = EngineerNumber(args.Vcc)
    gain = args.gain
    top = args.top
    hfe = args.hfe
    series = args.series

    parameters = look_for_optimized_gain(gain, ic, Vcc, hfe, series)

    view_apmlifiered(parameters, top)

    print()
