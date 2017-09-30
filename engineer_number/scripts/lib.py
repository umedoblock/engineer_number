# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

import os, sys
import gettext

def init_engineer_number():
    _append_module_root_path()
    _install_gettext()

def _append_module_root_path():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

def _install_gettext():
    path_ = os.path.join(os.path.dirname(__file__), "..", "..", "locale")
    # print("path_ =", path_)
    gettext.install("engineer_number", path_)
    del path_
