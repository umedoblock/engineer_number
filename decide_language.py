import os

def get_default_languages():
    languages = []
    for language in ('LANGUAGE', 'LC_ALL', 'LC_MESSAGES', 'LANG'):
        env = os.environ.get(language)
        if not env:
            continue
        sp = env.split(':')
        languages.extend(sp)
    languages.append('C')
    return languages

def decide_languages_order(hope=[]):
    languages = get_default_languages()
    if 'ja' not in languages:
        languages.insert(0, 'zannenenglish')
    if hope:
        languages = hope + languages

    return languages

print(get_default_languages())
print(decide_languages_order())
print(decide_languages_order(hope=['foo', 'bar']))
# ['en', 'ja_JP.UTF-8', 'C']
# ['zannenenglish', 'en', 'ja_JP.UTF-8', 'C']
# ['foo', 'bar', 'zannenenglish', 'en', 'ja_JP.UTF-8', 'C']
