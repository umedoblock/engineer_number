import os

def get_default_languages():
    languages = []
    for language in ('LANGUAGE', 'LC_ALL', 'LC_MESSAGES', 'LANG'):
        env = os.environ.get(language)
        if not env:
            continue
        sp = env.split(':')
        languages.extend(sp)
    if not languages:
        languages.append('C')
    return languages

def decide_languages_order(hope=[]):
    # first is overwrited by second.
    # so should be hope=['lower-important', 'higher-important']
    languages = get_default_languages()
    if 'ja' not in languages:
        languages.insert(0, 'zannenenglish')
    languages.extend(hope)

    return languages

# LANG=en_US.UTF-8
# LANGUAGE=en_US:en
# echo ${LANG}
# echo ${LANGUAGE}
print(get_default_languages())
print(decide_languages_order())
print(decide_languages_order(hope=['lower-important', 'higher-important']))
# $ export LANGUAGE=en:ja
# ['en', 'ja_JP.UTF-8', 'C']
# ['zannenenglish', 'en', 'ja_JP.UTF-8', 'C']
# ['foo', 'bar', 'zannenenglish', 'en', 'ja_JP.UTF-8', 'C']
