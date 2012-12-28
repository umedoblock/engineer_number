import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), 'engineer'))
from engineer import *
from engineer.constants import *

class TestEngineer(unittest.TestCase):
    def test_simple_but_too_long(self):
        M3_3 = Number(3.3, MEGA)
        # kilo must be 'k'. K means kelbin.
        k47 = Number(47, KILO)
        mili47 = Number(47, MILLI)
        mcr3_3 = Number(3.3, MICRO)

        # __str__()
        self.assertEqual('3.300M', str(M3_3))
        self.assertEqual('47.000k', str(k47))
        self.assertEqual('47.000m', str(mili47))
        self.assertEqual('3.300u', str(mcr3_3))

        # mul
        self.assertEqual('155.100G', str(k47 * M3_3))
        self.assertEqual('155.100n', str(mili47 * mcr3_3))
        self.assertEqual('2.209k', str(k47 * mili47))
        self.assertEqual('10.890', str(M3_3 * mcr3_3))
        self.assertEqual('155.100m', str(k47 * mcr3_3))
        self.assertEqual('155.100k', str(M3_3 * mili47))

        # add, sub
        self.assertEqual('3.347M', str(M3_3 + k47))
        self.assertEqual('3.253M', str(M3_3 - k47))
        self.assertEqual('47.003m', str(mili47 + mcr3_3))
        self.assertEqual('46.997m', str(mili47 - mcr3_3))
        # big and small, ignored small
        self.assertEqual('3.300M', str(M3_3 + mili47))

        # TOO BIG
        T10 = Number(10, TERA)
        G40 = Number(40, GIGA)
        self.assertEqual('10.000T', str(T10))
        self.assertEqual('40.000G', str(G40))
        BIG400 = T10 * G40
        self.assertEqual('400000000000000000000000', str(BIG400))

        # 'over ekusa'
        #                   10 ** 9, 10 ** 18
        over_ekusa = Number(1000000000, EXA)
        self.assertEqual('1000000000000000000000000000', str(over_ekusa))

        # too small
        u1 = Number(1, MICRO)
        n4 = Number(4, NANO)
        self.assertEqual('1.000u', str(u1))
        self.assertEqual('4.000n', str(n4))
        small4 = u1 * n4
        self.assertEqual('4e-15', str(small4))

        self.assertEqual('987.000m', str(Number(0.987)))
        self.assertEqual('1.000k', str(Number(1000, ONE)))
        self.assertEqual('1.040k', str(Number(1040, ONE)))
        self.assertEqual('999.000', str(Number(999, ONE)))
        self.assertEqual('999.200', str(Number(999.2, ONE)))
        self.assertEqual('2.000', str(Number(2, ONE)))
        self.assertEqual('1.001', str(Number(1.001, ONE)))
        self.assertEqual('1.000', str(Number(1, ONE)))

        # same result
        self.assertEqual('1.000m', str(Number(0.001, ONE)))
        self.assertEqual('1.000m', str(Number(1, MILLI)))
        self.assertEqual('1.000m', str(Number(1000, MICRO)))

        self.assertRaises
        self.assertEqual('1.004u', str(u1 + n4))
        self.assertEqual('996.000n', str(u1 - n4))
        self.assertEqual('250.000', str(u1 / n4))
        self.assertEqual('249.000', str(u1 // n4))
        self.assertEqual('4.000n', str(u1 % n4))
        div, mod = divmod(u1, n4)
        self.assertEqual('249.000', str(div))
        self.assertEqual('4.000n', str(mod))

        self.assertEqual('1000.000m', str(pow(u1, n4))) # 0.9999999447379593
        self.assertEqual('999.981m', str(pow(n4, u1))) # 0.9999806632154822
        self.assertEqual(0.9999999447379593, pow(u1.num, n4.num))
        neg1 = Number(-1, ONE)
        self.assertEqual('-1.000', str(neg1))

        self.assertEqual('0.000', str(Number(0)))
        math.fabs(u1)
        with self.assertRaises(RuntimeError) as raiz:
            int(u1)
        self.assertEqual('no meaning: convert to integer.',
                          raiz.exception.args[0])

        self.assertEqual('2.000', str(Number(16) % Number(7)))
        self.assertEqual('2.000', str(16 % Number(7)))
        self.assertEqual('2.000', str(Number(16) % 7))

        self.assertEqual('9.000', str(Number(16) - Number(7)))
        self.assertEqual('9.000', str(16 - Number(7)))
        self.assertEqual('9.000', str(Number(16) - 7))

        self.assertEqual('128.000', str(Number(2) ** Number(7)))
        self.assertEqual('128.000', str(2 ** Number(7)))
        self.assertEqual('128.000', str(Number(2) ** 7))

        self.assertEqual('2.286', str(Number(16) / Number(7)))
        self.assertEqual('2.286', str(16 / Number(7)))
        self.assertEqual('2.286', str(Number(16) / 7))

        self.assertEqual('2.000', str(Number(16) // Number(7)))
        self.assertEqual('2.000', str(16 // Number(7)))
        self.assertEqual('2.000', str(Number(16) // 7))

        self.assertEqual('2.286M', str(Number(16, MEGA) / Number(7)))
        self.assertEqual('2.286M', str(16 / Number(7, MICRO)))
        self.assertEqual('2.286M', str(Number(16, MEGA) / 7))

if __name__ == '__main__':
  # gc.set_debug(gc.DEBUG_LEAK)
    unittest.main()
