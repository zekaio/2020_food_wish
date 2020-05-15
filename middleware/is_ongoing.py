# -*- coding: utf-8 -*-
from flask_restful import abort
import datetime
from config import config


def is_ongoing() -> None:
    begin = datetime.datetime.strptime(config.BASECONFIG.BEGIN, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(config.BASECONFIG.END, '%Y-%m-%d %H:%M:%S')
    now = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    if now < begin:
        abort(410, message="活动还未开始")
    elif now > end:
        abort(410, message="活动已结束")
