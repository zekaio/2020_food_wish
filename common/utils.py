# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import abort
import requests
import json
from config import config
import datetime


def check_tel(tel: str) -> bool:
    s = str(tel)
    return s.isdigit() and len(s) == 11 and s[0] == '1'


def check_wechat_login() -> str:
    if 'open_id' not in session:
        phpsessid = request.cookies.get('PHPSESSID')
        if phpsessid is not None:
            res = requests.get('https://hemc.100steps.net/2017/wechat/Home/Index/getUserInfo',
                               cookies={'PHPSESSID': phpsessid}, timeout=10)
            try:
                data = json.loads(res.text)
                if 'openid' in data:
                    session['open_id'] = data['openid']
            except:
                pass
    if 'open_id' not in session:
        abort(401, message="请先绑定微信")
    return session['open_id']


def is_ongoing() -> bool:
    begin = datetime.datetime.strptime(config.BASECONFIG.BEGIN, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(config.BASECONFIG.END, '%Y-%m-%d %H:%M:%S')
    now = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    if now < begin:
        abort(410, message="活动还未开始")
        return False
    elif now > end:
        abort(410, message="活动已结束")
        return False
    else:
        return True
