import os
import sys
import math, argparse

import lib
lib.init_engineer_number()

from engineer_number import EngineerNumber
from engineer_number.constants import *
from engineer_number.lib import get_resistors, close_e_series

def look_for_optimized_gain(gain, ic, Vcc, hfe=200, e_series="E12"):
    resistors = get_resistors(e_series)

    parameters = []
#   print("resistors =", resistors)
    for Rc in resistors:
        ie = ic
        ie = ic + ic / hfe

        Vc = Rc * ic   # 6
        Ve = Vc / gain
        Re = Ve / ie

        Re_ = close_e_series(Re, "up", e_series, EngineerNumber.COMPONENT_ERROR)
#       print("Re={}, Re_={}".format(Re, Re_))
#       if Re_:
#           print("Re.error(Re_)={}".format(Re.error(Re_)))
        if not Re_:
            continue

        Re = Re_
        Ve = Re * ie
#       if Vc / Ve < gain:
#           continue

      # Vc = Rc * ic   # 6
      # Re = Rc / gain # 5
      # Ve = ie * Re

        # 注意
        # must be Vc + Ve <= Vcc
        if Vc + Ve > Vcc:
          # raise ValueError("invalid Vc and Ve combination compare Vcc.")
          # print("added(Vc={}, Ve={})={} is greater ghan Vcc={}.".format(Vc, Ve, Vc + Ve, Vcc))
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

        Rb2_ = close_e_series(Rb2, "up", e_series, EngineerNumber.COMPONENT_ERROR) # E12 にあわす
        Rb1_ = close_e_series(Rb1, "up", e_series, EngineerNumber.COMPONENT_ERROR) # E12 にあわす
        if (not Rb2_) or (not Rb1_):
            print("Rb2={}, Rb2_={}, Rb2.error(Rb2_)={}".format(Rb2, Rb2_, Rb2.error(Rb2_)))
            print("Rb1={}, Rb1_={}, Rb1.error(Rb1_)={}".format(Rb1, Rb1_, Rb1.error(Rb1_)))
            continue
        Radd = Rb1_ + Rb2_
      # print("Radd =", Radd)

        ibias_ = Vcc / Radd

        tup = (Rb1_, Rb2_, Rc, Re, ic, gain, Vcc, Vc, Ve, Vb, Vce, ib, ibias_, Pce)
        parameters.append(tup)

    parameters.sort(key=lambda x: math.fabs(x[-1]))
    return parameters

def view_apmlifiered(gained, top=-1):
    fmt = ", ".join(["{!s:>8s}"] * 14)
    print(fmt.format("Rb1_", "Rb2_", "Rc", "Re", "ic", "gain", "Vcc", "Vc", "Ve", "Vb", "Vce", "ib", "ibias", "Pce"))
    for Rb1_, Rb2_, Rc, Re, ic, gain, Vcc, Vc, Ve, Vb, Vce, ib, ibias, Pce in gained[:top]:
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
    parser.add_argument("--e_series", metavar="N", dest="e_series",
                       nargs="?", default="E12",
                       help="e_series default: E12")
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
    e_series = args.e_series

    parameters = look_for_optimized_gain(gain, ic, Vcc, hfe, e_series)

    view_apmlifiered(parameters, top)

    print()
