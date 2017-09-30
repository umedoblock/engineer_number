# coding: utf-8

import os
import gettext

from engineer_number import constants
from engineer_number.core import EngineerNumber

__version__ = "1.0.5"
__all__ = ["EngineerNumber", "constants"]

__author__ = "umedoblock <umedoblock@gmail.com>"

def _get_default_languages():
    languages = []
    for language in ("LANGUAGE", "LC_ALL", "LC_MESSAGES", "LANG"):
        env = os.environ.get(language)
        if not env:
            continue
        sp = env.split(":")
        languages.extend(sp)
    if not languages:
        languages.append("C")
    return languages

def _decide_languages_order(hope=[]):
    # first is overwrited by second.
    # so should be hope=["lower-important", "higher-important"]
    languages = _get_default_languages()
    if "ja" not in languages:
        languages.insert(0, "zannenenglish")
    languages.extend(hope)

    return languages

def _gettext_install(domain,
                     localedir=None,
                     languages=[],
                     codeset=None,
                     names=None):
    t = gettext.translation(domain, localedir,
                            languages=languages,
                            fallback=True,
                            codeset=codeset)
    t.install(names)

path_ = os.path.join(os.path.dirname(__file__), "locale")
# print("path_ =", path_)
_gettext_install("engineer_number",
                  path_,
                  languages=_decide_languages_order())

def _I18N(attr):
    """attr.__doc__ を gettext() にて翻訳する。

    attr() として attr を呼び出し可能であれば、
    attr に結び付く __doc__ 属性を msgid とし、
    以下を実行する。
    msgstr = gettext(msgid)
    実行後、attr に結びつく __doc__ 属性の値を、msgstr で上書きする。

    attr() として attr を呼び出し可能でない場合、何も実行しない。
    """

    if callable(attr):
        msgid = getattr(attr, "__doc__")
        msgstr = _(msgid)
        setattr(attr, "__doc__", msgstr)

_I18N(_I18N)
for attr in EngineerNumber.__dict__.values():
    _I18N(attr)

del attr, path_
