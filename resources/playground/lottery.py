# -*- coding: utf-8 -*-
from flask import session
from flask_restful import Resource
from common.database import get_lottery_process, lottery


class Lottery(Resource):
    # 抽奖--图鉴页面，获取抽奖进度
    def get(self):
        return dict(progress=get_lottery_process(session['open_id']))

    # 抽奖页面，抽奖按钮
    def post(self):
        return dict(section=lottery(session['open_id']))
