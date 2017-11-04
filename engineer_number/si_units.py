# see: https://www.nmij.jp/library/units/si/R8/SI8J.pdf
# 国際文書 SI 第 8 版日本語版
# The International System of Units (SI) - 8th edition - 2006
# 原書コード ： ISBN 92-822-2213-6
# page 38

# NO COPYRIGHT
# copied by 梅濁酒(umedoblock)

from .core import EngineerNumber

# SI との併用が認められている 単位
# エネルギー 電子ボルト eV
eV = EngineerNumber(1.60217653, -19)
# 質量 ダルトン
Da = EngineerNumber(1.66053886, -27)
u = Da
# 長さ 天文単位
ua = EngineerNumber(1.49597870691, 11)

# 自然単位系 （n.u.）
# 速さの自然単位 m/s （定義値） （真空中の光の速さ）
c0 = EngineerNumber(299792458)
# 作用の自然単位( J s) （換算プランク定数）
h_nu = EngineerNumber(1.05457168, -34)
# 質量の自然単位 kg （電子質量）
me_nu = EngineerNumber(9.1093826, -31)
# 時間の自然単位 s, h / (me * c0 ** 2)
s_nu = EngineerNumber(1.2880886677, -21)

# 原子単位系(a.u.)
# 電荷の原子単位 C
e = EngineerNumber(1.60217653, -19)
# 質量の原子単位 kg （電子質量）
me_au = EngineerNumber(9.1093826, -31)
# 作用の原子単位 J s （換算プランク定数）
h_au = EngineerNumber(1.05457168, -34)
# 長さの原子単位 m （ボーア半径）
a0 = EngineerNumber(0.5291772108, -10)
# エネルギーの原子単位 J （ハートリーエネルギー）
Eh = EngineerNumber(4.35974417, -18)
# 時間の原子単位 h/Eh
s_au = EngineerNumber(2.418884326, -17)
