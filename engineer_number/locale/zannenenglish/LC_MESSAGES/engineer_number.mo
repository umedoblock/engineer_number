Þ    1      ¤              ,    -  W   9      ¹  ¤  -   ^  ?     P   Ì          ¾  (   Õ  %   þ  $   $  %   I  )   o  )     ,   Ã  (   ð  +     .   E  (   t  (     )   Æ  (   ð  (     )   B  )   l  (     )   ¿  )   é  )     *   =  -   h  *     /   Á  *   ñ  *     +   G  *   s  *     .   É  )   ø  )   "  -   L  :   z     µ  ô   Ë  º  À  O   {$  Q  Ë$     &  B   &  Ò  á&    ´3  -   :5  0   h5     5  U   ¹5     6      &6     G6     e6     6  !    6  !   Â6  $   ä6      	7  #   *7  &   N7      u7      7  !   ·7      Ù7      ú7  !   8  !   =8      _8  !   8  !   ¢8  !   Ä8  "   æ8  %   	9  "   /9  '   R9  "   z9  "   9  #   À9  "   ä9  "   :  &   *:  !   Q:  !   s:  %   :  %   »:     á:  ½   ÷:  z  µ;  .   0?   "K" ã SI æ¥é ­è¾ã®è¨å·ã¨ãã¦ä½¿ç¨ãããã¨ã¯åºæ¥ã¾ããã
kilo ãè¡¨ç¾ãããå ´åã "K" ã§ã¯ãªããå°æå­ã® "k" ããä½¿ãä¸ããã
ãªããªãã°ã"K" ã¯ãKelvin æ¸©åº¦ãè¡¨ç¾ããããã®åä½è¨å·ã ããã§ãã 0 < abs(number(={})) < 1 ãæºããæ°å­ã int ã«å¤æãããã¨ãã¾ããã EngineerNumber class ã¯ãSIæ¥é ­è¾ã®å¤æã»ç°ãªãSIæ¥é ­è¾åå£«ã®
    è¨ç®ãå®¹æã«ãã¾ããä½¿ç¨å¯è½ãªSIæ¥é ­è¾ã¯ãæå¾ã«èª¬æãã¾ãã

    EngineerNumber instance(ã¤ã³ã¹ã¿ã³ã¹) ã«å¯¾ãã
    ä»»æã®SIæ¥é ­è¾ã KEY ã«ãããã¨ã§ã
    ä»»æã®SIæ¥é ­è¾ã«æç®ããå¤ãç¥ããã¨ãåºæ¥ã¾ãã
    SI æ¥é ­è¾å¤æçµæã¨ãã¦è¿ãããæå­åã EngineerNumber() ã«æ¸¡ãã
    æ°ããª EngineerNumber instance ãçæåºæ¥ã¾ãã

    EngineerNumber.num å±æ§ã¯ãæ°å¤å object ã§ãã
    EngineerNumber class ã«ã__add__() ç­ã® method ãå®ç¾©ãã
    æ¼ç®ã®å¯¾è±¡ã EngineerNumber.num ã¨ãããã¨ã§ã
    EngineerNumber instance ã¯ãæ°å¤å object äºæã«ãªã£ã¦ãã¾ãã
    æ°å¤å object äºæã«ããæ¹æ³ã¯ã
    PEP 3141, numbers class ç­ããè¦§ä¸ããã

    ä»¥ä¸ãä½¿ãããã®æé ãç°¡åã«ç´¹ä»ãã¾ãã
    >>> from engineer_number import EngineerNumber

    KILO, MEGA, ...ç­ãã® SI æ¥é ­è¾åãä½¿ããªãå ´åã
    ä»¥ä¸ã®è¡ã¯å¿è¦ããã¾ããã
    >>> from engineer_number.constants import *

    ä»¥ä¸ã®ãNo.1, 2, 3 ã§ã¯ã 10 * 1000 ã®å¤ãå¾ãæ¹æ³ã¨ã
    SI æ¥é ­è¾å¤æã®æ¹æ³ãèª¬æãã¾ãã

    No.1: æå¹å¤ã®æå­åã¨ãSI æ¥é ­è¾ãé£çµãã
    10 kilo ã®å¤ãå¾ãæ¹æ³ã§ãã
    >>> r1 = EngineerNumber('10k')       # No.1
    >>> r1
    10.000k

    10 kilo ã Mega ã§è¨ç®ããSI æ¥é ­è¾å¤æãè¡ãã¾ãã
    >>> r1['M']
    '0.010M'

    No.2: æå¹å¤ã¨ãSI æ¥é ­è¾åã§ 10 kilo ã®å¤ãå¾ãæ¹æ³ã§ãã
    >>> r2 = EngineerNumber(10, KILO)    # No.2
    >>> r2 = EngineerNumber('10', KILO)  # No.2
    >>> r2
    10.000k

    10 kilo ã« SI æ¥é ­è¾å¤æãè¡ããæ°å¤ã«å¤æãã¾ãã
    10 ã®ä¹æ°ã 0 ã®å ´åã
    ç©ºæå­åã SI æ¥é ­è¾ã¨ãã¦ãããã¨ã«æ³¨æãã¦ä¸ããã
    >>> r2['']
    '10000.000'

    No.3: æå¹å¤ã¨ 10 ã®ä¹æ°ã§ 10 kilo ã®å¤ãå¾ãæ¹æ³ã§ãã
    æµæã®ã«ã©ã¼ã³ã¼ãããæµæå¤ãæ±ããäºãæ³å®ãã¦ãã¾ãã
    >>> r3 = EngineerNumber(10, 3)       # No.3
    >>> r3 = EngineerNumber('10', 3)     # No.3
    >>> r3
    10.000k

    10 kilo ã kilo ã§è¨ç®ããããªãã¡ãã£ã¦ SI æ¥é ­è¾å¤æãè¡ãã¾ãã
    èªåã§ãå¿è¦ãªãã¨ã¯æããã§ãããã©ãæµãä¸ãæ¸ãã¾ããã
    >>> r3['k']
    '10.000k'

    ä»¥ä¸ã®ãNo.4, 5 ã§ã¯ãã³ã³ãã³ãµä¸ã®è¡¨ç¤ºããã
    ã³ã³ãã³ãµã®å®¹éå¤ãæ±ããæ¹æ³ãç´¹ä»ãã¾ãã
    "p" ãæå¹æ°å¤ã®å¾ã«ä»ãã¦ãããã¨ã«æ³¨æãã¦ä¸ããã

    No.4: ã³ã³ãã³ãµã®è¡¨ç¤º "104" ããå®¹éå¤ãæ±ãã¾ãã
    >>> c4 = EngineerNumber('10p', 4)    # No.4
    >>> c4
    100.000n

    ãã¤ã¯ã­ã»ããã»ãã³ãè¨ç®ããæãªã©ã
    ããé ­ãããããããã¾ããã­ã
    >>> c4['u']
    '0.100u'

    No.5: ã³ã³ãã³ãµã®è¡¨ç¤º "202" ããå®¹éå¤ãæ±ãã¾ãã
    >>> c5 = EngineerNumber('20p', 2)    # No.5
    >>> c5
    2.000n

    ãã¤ã¯ã­ã»ããã»ãã³ãè¨ç®ããæãªã©ã
    ããé ­ãããããããã¾ããã­ã
    >>> c5['p']
    '2000.000p'

    ããã ãã®è©±ï¼
    ãã¤ã¯ã­ã»ããã»ãã³ã®å¤æãå¤§å¤ã§ãããããã¦ã
    ããééãã¦å°ãã®ã§ããã® EngineerNumber ãä½æãã¾ããã
    æµæã®ã«ã©ã¼ã³ã¼ãã«ãä½¿ããã¨åãã£ãæã«ã¯ã
    æ¬å½ã«ä¾¿å©ã ãªã¼ãã¨èªåã§ãæãã¾ãã

    ä½¿ç¨ä¾ããããå°ãç¥ãããæ¹ã¯ "README.txt" ããè¦§ä¸ããã

    SI æ¥é ­è¾ã¨ãã¦ç¨æãã¦ããã®ã¯ãä»¥ä¸ã®éãã§ãã
    ('Y', YOTTA),
    ('Z', ZETTA),
    ('E', EXA),
    ('P', PETA),
    ('T', TERA),
    ('G', GIGA),
    ('M', MEGA),
    ('k', KILO),
     ('', ONE),
    ('m', MILLI),
    ('u', MICRO),
    ('n', NANO),
    ('p', PICO),
    ('f', FEMTO),
    ('a', ATTO),
    ('z', ZEPTO),
    ('y', YOCTO),
     EngineerNumber.num ã®å¤ããã_value, _exponent10 ãæ­£è¦åããã
        num, _value, _exponent10 ã®è¨ç®æ¹æ³ã¯ãç°¡åã«ä»¥ä¸ã®éãã

        _exponent10 = log10(num) // 3
        _value = num // (10 ** _exponent10)
        num =(å¤§ä½åããapproximately equal to) _value * 10 ** _exponent10

        _exponent10 ã¯ SI æ¥é ­è¾ã¨é£åããããã
        3 ã®æ´æ°åã«ãªã£ã¦ãããã¨ã«æ³¨æã SI æ¥é ­è¾ã«ããæå¹æ°å­ãå¤æã SI æ¥é ­è¾ã«å¯¾å¿ããã10 ã®ä¹æ°å¤ãè¿ãã¾ãã SI æ¥é ­è¾ã®è¨å·ã¯ãæ¬¡ã®ããããã§ãªããã°ãªãã¾ããã{} attr.__doc__ ã gettext() ã«ã¦ç¿»è¨³ããã

    attr() ã¨ãã¦ attr ãå¼ã³åºãå¯è½ã§ããã°ã
    attr ã«çµã³ä»ã __doc__ å±æ§ã msgid ã¨ãã
    ä»¥ä¸ãå®è¡ããã
    msgstr = gettext(msgid)
    å®è¡å¾ãattr ã«çµã³ã¤ã __doc__ å±æ§ã®å¤ããmsgstr ã§ä¸æ¸ãããã

    attr() ã¨ãã¦ attr ãå¼ã³åºãå¯è½ã§ãªãå ´åãä½ãå®è¡ããªãã
     look for optimized Hz. math.__ceil__() ã® help ãèª­ãã§ã math.floor() ã® help ãèª­ãã§ã math.sqrt() ã® help ãèª­ãã§ã math.trunc() ã® help ãèª­ãã§ã object.__abs__() ã® help ãèª­ãã§ã object.__add__() ã® help ãèª­ãã§ã object.__divmod__() ã® help ãèª­ãã§ã object.__eq__() ã® help ãèª­ãã§ã object.__float__() ã® help ãèª­ãã§ã object.__floordiv__() ã® help ãèª­ãã§ã object.__ge__() ã® help ãèª­ãã§ã object.__gt__() ã® help ãèª­ãã§ã object.__int__() ã® help ãèª­ãã§ã object.__le__() ã® help ãèª­ãã§ã object.__lt__() ã® help ãèª­ãã§ã object.__mod__() ã® help ãèª­ãã§ã object.__mul__() ã® help ãèª­ãã§ã object.__ne__() ã® help ãèª­ãã§ã object.__neg__() ã® help ãèª­ãã§ã object.__pos__() ã® help ãèª­ãã§ã object.__pow__() ã® help ãèª­ãã§ã object.__radd__() ã® help ãèª­ãã§ã object.__rdivmod__() ã® help ãèª­ãã§ã object.__repr__() ã® help ãèª­ãã§ã object.__rfloordiv__() ã® help ãèª­ãã§ã object.__rmod__() ã® help ãèª­ãã§ã object.__rmul__() ã® help ãèª­ãã§ã object.__round__() ã® help ãèª­ãã§ã object.__rpow__() ã® help ãèª­ãã§ã object.__rsub__() ã® help ãèª­ãã§ã object.__rtruediv__() ã® help ãèª­ãã§ã object.__str__() ã® help ãèª­ãã§ã object.__sub__() ã® help ãèª­ãã§ã object.__truediv__() ã® help ãèª­ãã§ã self[si_prefix] ã¨ãã¦ãSI æ¥é ­è¾å¤æãè¡ãã series must be "E12". ä¸»ã« debug ç¨ã
        æ¬å½ã¯éå¬éã«ãããã£ãããå¬éã¨ãã¦ãã¾ã£ãçºã
        ä»æ´ãéå¬éã«åºæ¥ãªãã¦å°ã£ã¦ããã
        åºæ¥ããã¨ãªããä»ããã§ãéå¬éã«ãããããã æå¹æ°å¤ã¨ 10 ã®ä¹æ°å¤ãæå®ãã¾ãã
        value ããäºã¤ã®æ¹æ³ã«ããæå®ã§ãã¾ãã
        ä¸ã¤ç®ã¯ãæå¹æ°å¤ãæ´æ°å¤ãæµ®åå°æ°å¤ã¨ãã¦æå®ããæ¹æ³ã§ãã
        äºã¤ç®ã¯ãæå¹æ°å¤ã®æå­åã¨ SI æ¥é ­è¾ãé£çµããæå­åã¨ãã¦
        æå®ããæ¹æ³ã§ãã

        exponent10 ã¯ãç¡æå®ã§ããã°ã0 ã¨ãã¦åãæ±ãã¾ãã
        ä»¥ä¸ã®è¨ç®å¼ã«ãããvalue, exponent10 ã®å¤ããã
        EngineerNumber.num å±æ§ã®å¤ãè¨ç®ãã¾ãã
        num = value * 10 ** exponent10

        ã¤ã¾ããexponent10 ãæå®ããªããã°ã
        num å±æ§ã®å¤ã¨ãã¦ãvalue ã®å¤ãããã®ã¾ã¾ä»£å¥ãããã¨ã«ãªãã¾ãã
        num = value * 10 ** 0 = value * 1 = value
        num å±æ§ã®å¤ã®ç¯å²ã¯ã -24 <= num <= 24 ã§ããããã¤ã
        num å±æ§ã®å¤ã¯ã3 ã®æ´æ°åã¨ãªãã¾ãã

        è©³ããä½¿ãæ¹ã¯ãEngineerNumber class ã® docstring ããè¦§ä¸ããã
        ä¾ 1 ã 5 ç­ãåããããããã¨æãã¾ãã
        æ´ãªãæå ±ã¯ãå°ãã ãã"README.txt" ã«æ¸ãã¦ãã¾ãã
         æå¹æ°å­ã®æ°å¤ã¨ 10 ã®ä¹æ°å¤ããtuple ã«è©°ãã¦è¿ãã¾ãã Project-Id-Version: 1.0.4
POT-Creation-Date: 2013-02-17 08:02+JST
PO-Revision-Date: 2013-02-17 08:02+JST
Last-Translator: æ¢ã©ã¶ãã(umedoblock) umedoblock@gmail.com
Language-Team: Japanese umedoblock@gmail.com
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
 cannot accept "K" as SI prefix symbol. please use "k" as prefix if you hope to describe kilo.Because "K" means Kelbin celcius.') trying to convert Integer that satisfied 0 < abs(number(={})) < 1. EngineerNumber class can easily calculate to change SI prefix and
    to calculate with another SI prefix. List up last part to be
    available SI prefix.

    You can find out arbitrary resulted value in new SI prefix
    to use KEY as arbitrary SI prefix.
    New EngineerNumber instance is created to convert SI prefix
    to new SI prefix which gives to EngineerNumber().
    string.

    EngineerNumber.num attribute is numeric object.
    EngineerNumber instance can use as numeric object to define
    num attribute in it class.
    How to give numeric object compatibility to arbitrary object ?
    Please see PEP3141 and numbers class.
    
    Below show what need way to use a EngineerNumber class instance.
    >>> from engineer_number import EngineerNumber

    No need to write a below sentence if don't use SI prefix name
    like a KILO, MEGA, ... etc.
    >>> from engineer_number.constants import *

    Explain a way in case1, case2, case3 that 
    how to get 10 * 1000 value and
    how to convert arbitrary SI prerix.

    case1: A way that combine significant digits string and SI prefix
    to get 10 kilo value.
    >>> r1 = EngineerNumber('10k')       # No.1
    >>> r1
    10.000k

    SI prefix converting after calculate 10 kilo as Mega.
    >>> r1['M']
    '0.010M'

    case2: A way that using significant digits and SI prefix to get
    10 kilo value.
    >>> r2 = EngineerNumber(10, KILO)    # No.2
    >>> r2 = EngineerNumber('10', KILO)  # No.2
    >>> r2
    10.000k

    Converting to number after 10 kilo is converted by SI prefix.
    Pay attention to use empty string as SI prefix if 10 multiple value
    is zero.
    >>> r2['']
    '10000.000'

    case3: A way that to get 10 kilo using significant digits and
    ten multiple value.
    Expected scenario to calculate an R-value from color code
    on resistance.
    >>> r3 = EngineerNumber(10, 3)       # No.3
    >>> r3 = EngineerNumber('10', 3)     # No.3
    >>> r3
    10.000k

    Do SI prefix converting to convert 10 kilo use kilo.
    No need it me too thinking, but atmosphere hope to write it.
    >>> r3['k']
    '10.000k'

    case4, case5 explain that how to calculate a capacitance
    on capacitor string.
    Pay attention to add "p" after significant digits.

    case4: To get a capacitance from a display on capacitor.
    >>> c4 = EngineerNumber('10p', 4)    # No.4
    >>> c4
    100.000n

    Often confusing when to calculate MICRO, NANO, PICO...
    >>> c4['u']
    '0.100u'

    case5: To get a capacitor capacitance from "202" on capacitance
    >>> c5 = EngineerNumber('20p', 2)    # No.5
    >>> c5
    2.000n

    Often confusing when to calculate MICRO, NANO, PICO...
    >>> c5['p']
    '2000.000p'

    coffee break:
    Please study æ¥æ¬èª and read ç§ãæ¥æ¬èªã§æ¸ãã docstring
    if you hope to a secret story in development of this module.

    Please read "README.txt" if you hope to get more using way.

    SI prefixes are below lines.
    ('Y', YOTTA),
    ('Z', ZETTA),
    ('E', EXA),
    ('P', PETA),
    ('T', TERA),
    ('G', GIGA),
    ('M', MEGA),
    ('k', KILO),
     ('', ONE),
    ('m', MILLI),
    ('u', MICRO),
    ('n', NANO),
    ('p', PICO),
    ('f', FEMTO),
    ('a', ATTO),
    ('z', ZEPTO),
    ('y', YOCTO),
     normalize _value, _exponent10 from EngineerNumber.num.        Instantly show you below how to calculate num, _value, _exponent10.

        _exponent10 = log10(num) // 3
        _value = num // (10 ** _exponent10)
        num =(approximately equal to) _value * 10 ** _exponent10

        Pay attention to _exponent10.
        _exponent10 is three-fold to associated with SI prerix.
         convert significant digits through SI prefix. return ten multiplier value injective SI prefix. SI prefix symbol must be in {}. attr.__doc__ = gettext(attr.__doc__)
     convert and translate to use gettext().     look for optimized Hz. please see math.__ceil__() help. please see math.floor() help. please see math.sqrt() help. please see math.trunc() help. please see object.__abs__() help. please see object.__add__() help. please see object.__divmod__() help. please see object.__eq__() help. please see object.__float__() help. please see object.__floordiv__() help. please see object.__ge__() help. please see object.__gt__() help. please see object.__int__() help. please see object.__le__() help. please see object.__lt__() help. please see object.__mod__() help. please see object.__mul__() help. please see object.__ne__() help. please see object.__neg__() help. please see object.__pos__() help. please see object.__pow__() help. please see object.__radd__() help. please see object.__rdivmod__() help. please see object.__repr__() help. please see object.__rfloordiv__() help. please see object.__rmod__() help. please see object.__rmul__() help. please see object.__round__() help. please see object.__rpow__() help. please see object.__rsub__() help. please see object.__rtruediv__() help. please see object.__str__() help. please see object.__sub__() help. please see object.__truediv__() help. convert SI prefix as self[si_prefix]. series must be "E12". mainly-purpose is debug.        now, I have a bother thing that
        In fact hope to no public method, but public method.
        If apologize you to hide, I hide it from now...
         assign significant digits and ten multiplier.
        value is assigned by two ways.
        first way, significant digits as integer or float.
        second way, join significant digits string and SI prefix like a
        as string

        exponent10 default is ten.
        calculate EngineerNumber.num attribute value to use a below
        calculating formula.
        num = value * 10 ** exponent10

        In short, if don't assign exponent10,
        directly assign value as num attribute value.
        num = value * 10 ** 0 = value * 1 = value
        num attribute value range is -24 <= num <= 24 and
        num attribute value three-fold value.

        If you hope to get a more detail, please see EngineerNumber class
        docstring.
        I anticipated that case 1 -> case 5 is your friendly.
        It exists a little bit more information in "README.txt".
         significant digit and ten multiplier in tuple. 