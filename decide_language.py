import os, re

def get_default_languages():
    languages = []
    for language in ('LANGUAGE', 'LC_ALL', 'LC_MESSAGES', 'LANG'):
        env = os.environ.get(language)
        if not env:
            print("{} is missing.".format(language))
            continue
        print("{}={}".format(language, env))
        sp = env.split(':')
        languages.extend(sp)
    print()

    if not languages:
        languages.append('C')
    return languages

def decide_languages_order(hope=[]):
    # first is overwrited by second.
    # so should be hope=['lower-important', 'higher-important']
    languages = get_default_languages()
    if not re.search(r'ja', ",".join(languages)) or languages[0].startswith("en_"):
        languages.insert(0, 'zannenenglish')
    languages.extend(hope)

    return languages

# LANG=en_US.UTF-8
# LANGUAGE=en_US:en
# echo ${LANG}
# echo ${LANGUAGE}
# print(get_default_languages())
# print(decide_languages_order())
language_priority = decide_languages_order(hope=['lower-important', 'higher-important'])
print("show you language priority.")
print(language_priority)
print("first language is {}".format(language_priority[0]))
# $ export LANGUAGE=en:ja
# ['en', 'ja_JP.UTF-8', 'C']
# ['zannenenglish', 'en', 'ja_JP.UTF-8', 'C']
# ['foo', 'bar', 'zannenenglish', 'en', 'ja_JP.UTF-8', 'C']
