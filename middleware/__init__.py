# -*- coding: utf-8 -*-
from .is_ongoing import *
from .check_wechat_login import *


def before_request():
    is_ongoing()
    check_wechat_login()
