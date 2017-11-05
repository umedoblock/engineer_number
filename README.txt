# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

This software is released under the MIT License, see LICENSE.txt.
（このソフトウェアは、MITライセンスのもとで公開されています。
  LICENSE.txt or LICENSE.ja.txt をご覧下さい。）

本 module では、工学的な数値の計算を容易に行うことを目的としています。
例えば、 以下のような場合に役に立ちます。

1. 470 nano って 何 micro だっけ？
2. このコンデンサーには、 "104" って書いてあるけど、容量は何マイクロだっけ？
3. 1GB のHDDに 103MB の、このファイル何個入れれる？
4. VCCは 5V で 47k の抵抗を使って、
   Ibeo が、、、hfeは 140だから、
   Iceoは、、、で、結局 Io は、、、mA で、
   Aで考えると絶対最大定格を下回るから。。。
5. 抵抗のカラーコードが、黄紫赤金で、数字にすると472xだから、、、
   47 * (10 ** 2) でえっと、、、
6. 絶対最大定格30mAに対して17mA流すと余裕ってどれくらい？
   という場面で必要になる % の計算など。

ええーい、ややこしい！

などなど、工学的な数値計算にお悩みのあなた。
そこで、EngineerNumber module の出番です。
簡単に計算しましょう。

0.
>>> from engineer_number import EngineerNumber as ENM #  recommended stands for

1.
>>> nano470 = ENM("470n")
>>> nano470
EngineerNumber("470.000n")
>>> nano470["u"]
'0.470u'

2.
>>> c104 = ENM("10p") * 10 ** 4
>>> c104 = ENM("10p", 4) # equal to above line
>>> c104
EngineerNumber("100.000n")
>>> c104["u"]
'0.100u'
>>> c104["n"]
'100.000n'

3.
>>> G1 = ENM('1G')
>>> M103 = ENM('103M')
>>> G1 / M103
EngineerNumber("9.709")

4.
>>> Vcc = 5
>>> k47 = ENM("47k")
>>> Ibeo = Vcc / k47
>>> Ibeo
EngineerNumber("106.383u")
>>> Ibeo["m"]
'0.106m'
>>> Iceo = Ibeo * 140
>>> Iceo["m"]
'14.894m'
>>> Io = Ibeo + Iceo
>>> Io
EngineerNumber("15.000m")
>>> Io[""]
'0.015'

5.
>>> kx = ENM("47", 2)
>>> kx
EngineerNumber("4.700k")
>>> kx[""]
'4700.000'

6.
>>> ENM("1%")
EngineerNumber("10.000m")
>>> ENM("1")["%"]
'100.000%'
>>> ENM("1%")[""]
'0.010'
>>> (ENM("17m") / ENM("30m"))["%"]
'56.667%'

このように，計算がとても楽になります。

how to make pot file.
$ pygettext.py -d engineer_number \
    --docstrings --no-location \
    --output-dir=engineer_number/locale \
    `find ./engineer_number -name '*.py'`

how to make mo file.
$ msgfmt.py \
    --output-file=engineer_number/locale/zannenenglish/LC_MESSAGES/engineer_number.mo \
    engineer_number/locale/engineer_number.zannenenglish.po
