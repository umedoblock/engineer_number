# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

# coding: utf-8

import os, re
import gettext

from . import constants
from .core import EngineerNumber

__version__ = "1.0.5"
__all__ = ["EngineerNumber", "constants", "si_units", "wire"]

__author__ = "umedoblock <umedoblock@gmail.com>"

def _get_default_languages():
    languages = []
    for language in ("LANG", "LANGUAGE"):
        env = os.environ.get(language)
        if not env:
            continue
        languages.append(env)
    if not languages:
        languages.append("C")
    return languages

def _decide_languages_order(hope=[]):
    languages = _get_default_languages()
    if languages[0].startswith("en_"):
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
_I18N(EngineerNumber)
for attr in EngineerNumber.__dict__.values():
    _I18N(attr)

del attr, path_
