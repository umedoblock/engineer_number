Þ    /                          W     Õ  q  -   G  ?   u  P   µ       (     %   F  $   l  %     )   ·  )   á  ,     (   8  +   a  .     (   ¼  (   å  )   	  (   8	  (   a	  )   	  )   ´	  (   Þ	  )   
  )   1
  )   [
  *   
  -   °
  *   Þ
  /   	  *   9  *   d  +     *   »  *   æ  .     )   @  )   j  -     :   Â  P   ý  â  N  º  1  O   ì  L  <       B   
    M  -   Ý  0        <     \      s          ²     Ï  !   í  !     $   1      V  #   w  &         Â      ã  !         &      G  !   h  !         ¬  !   Í  !   ï  !     "   3  %   V  "   |  '     "   Ç  "   ê  #     "   1  "   T  &   w  !     !   À  %   â  %     X   .  <    z  Ä   .   ?$   "K" ã SI æ¥é ­è¾ã®è¨å·ã¨ãã¦ä½¿ç¨ãããã¨ã¯åºæ¥ã¾ããã
kilo ãè¡¨ç¾ãããå ´åã "K" ã§ã¯ãªããå°æå­ã® "k" ããä½¿ãä¸ããã
ãªããªãã°ã"K" ã¯ãKelvin æ¸©åº¦ãè¡¨ç¾ããããã®åä½è¨å·ã ããã§ãã 0 < abs(number(={})) < 1 ãæºããæ°å­ã int ã«å¤æãããã¨ãã¾ããã EngineerNumber.num ã®å¤ããã_num, _exponent10 ãæ­£è¦åããã
        num, _num, _exponent10 ã®è¨ç®æ¹æ³ã¯ãç°¡åã«ä»¥ä¸ã®éãã

        _exponent10 = log10(num) // group_of_digits(=3)
        _num = num // (10 ** _exponent10)
        num =(å¤§ä½åããapproximately equal to) _num * 10 ** _exponent10

        _exponent10 ã¯ SI æ¥é ­è¾ã¨é£åããããã
        group_of_digits(=3) ã®æ´æ°åã«ãªã£ã¦ãããã¨ã«æ³¨æã SI æ¥é ­è¾ã«ããæå¹æ°å­ãå¤æã SI æ¥é ­è¾ã«å¯¾å¿ããã10 ã®ä¹æ°å¤ãè¿ãã¾ãã SI æ¥é ­è¾ã®è¨å·ã¯ãæ¬¡ã®ããããã§ãªããã°ãªãã¾ããã{} look for optimized Hz. math.__ceil__() ã® help ãèª­ãã§ã math.floor() ã® help ãèª­ãã§ã math.sqrt() ã® help ãèª­ãã§ã math.trunc() ã® help ãèª­ãã§ã object.__abs__() ã® help ãèª­ãã§ã object.__add__() ã® help ãèª­ãã§ã object.__divmod__() ã® help ãèª­ãã§ã object.__eq__() ã® help ãèª­ãã§ã object.__float__() ã® help ãèª­ãã§ã object.__floordiv__() ã® help ãèª­ãã§ã object.__ge__() ã® help ãèª­ãã§ã object.__gt__() ã® help ãèª­ãã§ã object.__int__() ã® help ãèª­ãã§ã object.__le__() ã® help ãèª­ãã§ã object.__lt__() ã® help ãèª­ãã§ã object.__mod__() ã® help ãèª­ãã§ã object.__mul__() ã® help ãèª­ãã§ã object.__ne__() ã® help ãèª­ãã§ã object.__neg__() ã® help ãèª­ãã§ã object.__pos__() ã® help ãèª­ãã§ã object.__pow__() ã® help ãèª­ãã§ã object.__radd__() ã® help ãèª­ãã§ã object.__rdivmod__() ã® help ãèª­ãã§ã object.__repr__() ã® help ãèª­ãã§ã object.__rfloordiv__() ã® help ãèª­ãã§ã object.__rmod__() ã® help ãèª­ãã§ã object.__rmul__() ã® help ãèª­ãã§ã object.__round__() ã® help ãèª­ãã§ã object.__rpow__() ã® help ãèª­ãã§ã object.__rsub__() ã® help ãèª­ãã§ã object.__rtruediv__() ã® help ãèª­ãã§ã object.__str__() ã® help ãèª­ãã§ã object.__sub__() ã® help ãèª­ãã§ã object.__truediv__() ã® help ãèª­ãã§ã self[si_prefix] ã¨ãã¦ãSI æ¥é ­è¾å¤æãè¡ãã ä¸»ã« debug ç¨ã
        github ã¸ã®ç§»è¡ãæã«ï¼éå¬éã¨ããã æ°ãã EngineerNumber object ãä½ãã¾ãã
    EngineerNumber object ã®ç²¾åº¦ã¯ï¼Python3 ã® float object ã«ä¾å­ãã¾ãã
    Python3 ã§ã¯ float object ã C è¨èªã® double åã®å¤æ°(=ob_fval) ã¨ãã¦å®ç¾©
    ãã¦ãã¾ãããã£ã¦ï¼ EngineerNumber object ã®ç²¾åº¦ã¯ï¼C è¨èªã® double åã«
    ä¾å­ãã¾ãã

    'value' ã¯ï¼æµ®åå°æ°ç¹æ°ï¼æ´æ°ï¼æå­åï¼ã¾ãã¯ä»ã® EngineerNumber object
    ãå¼æ°ã«åºæ¥ã¾ããä½ãã®å¤ãä¸ããããªããã°ï¼ EngineerNumber('0') ãè¿ã
    ã¾ãã
    'exponent10' ãå¼æ°ã¨åºæ¥ãã®ã¯æ´æ°ã®ã¿ã§ãã

    value * 10 ** exponent10
    ã®è¨ç®çµæã EngineerNumber object ã®å¤ã¨ãã¾ãã
     æå¹æ°å¤ã¨ 10 ã®ä¹æ°å¤ãæå®ãã¾ãã
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
         æå¹æ°å­ã®æ°å¤ã¨ 10 ã®ä¹æ°å¤ããtuple ã«è©°ãã¦è¿ãã¾ãã Project-Id-Version: 1.0.5
POT-Creation-Date: 2013-02-17 08:02+JST
PO-Revision-Date: 2017-11-03 11:35+0900
Last-Translator: æ¢æ¿é(umedoblock) umedoblock@gmail.com
Language-Team: Japanese umedoblock@gmail.com
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
 cannot accept "K" as SI prefix symbol. please use "k" as prefix if you hope to describe kilo.Because "K" means Kelbin celcius.') trying to convert Integer that satisfied 0 < abs(number(={})) < 1. normalize _num, _exponent10 from EngineerNumber.num.        Instantly show you below how to calculate num, _num, _exponent10.

        _exponent10 = log10(num) // group_of_digits(=3)
        _num = num // (10 ** _exponent10)
        num =(approximately equal to) _num * 10 ** _exponent10

        Pay attention to _exponent10.
        _exponent10 is three-fold to associated with SI prerix.
         convert significant digits through SI prefix. return ten multiplier value injective SI prefix. SI prefix symbol must be in {}. look for optimized Hz. please see math.__ceil__() help. please see math.floor() help. please see math.sqrt() help. please see math.trunc() help. please see object.__abs__() help. please see object.__add__() help. please see object.__divmod__() help. please see object.__eq__() help. please see object.__float__() help. please see object.__floordiv__() help. please see object.__ge__() help. please see object.__gt__() help. please see object.__int__() help. please see object.__le__() help. please see object.__lt__() help. please see object.__mod__() help. please see object.__mul__() help. please see object.__ne__() help. please see object.__neg__() help. please see object.__pos__() help. please see object.__pow__() help. please see object.__radd__() help. please see object.__rdivmod__() help. please see object.__repr__() help. please see object.__rfloordiv__() help. please see object.__rmod__() help. please see object.__rmul__() help. please see object.__round__() help. please see object.__rpow__() help. please see object.__rsub__() help. please see object.__rtruediv__() help. please see object.__str__() help. please see object.__sub__() help. please see object.__truediv__() help. convert SI prefix as self[si_prefix]. mainly-purpose is debug.        self._detail() became unpublish to move github.
         Construct a new EngineerNumber object.
    EngineerNumber accuracy depends on Python3 float object accuracy. Python3 define float object as C language double type variant(=ob_fval). Therefore EngineerNumber object accuracy depends on C language double type variant.
    'value' can be a float, integer, string or another EngineerNumber object. If no value is given, return EngineerNumber('0').
    The 'exponent10' describe multiplying factor of 10. It can take just integer as argument.
    
    Return below result as EngineerNumber object.
    value * 10 ** exponent10
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