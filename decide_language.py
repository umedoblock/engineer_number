import os, re

import engineer_number
# LANG=en_US.UTF-8
# LANGUAGE=en_US:en
# echo ${LANG}
# echo ${LANGUAGE}

language_priority = engineer_number._decide_languages_order()
print("show you language priority.")
print(language_priority)
print("first language is {}".format(language_priority[0]))
# $ export LANGUAGE=en:ja
# ['en', 'ja_JP.UTF-8', 'C']
# ['zannenenglish', 'en', 'ja_JP.UTF-8', 'C']
# ['foo', 'bar', 'zannenenglish', 'en', 'ja_JP.UTF-8', 'C']
