# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource
from common.database import get_lottery_process, lottery, set_info
from common.utils import check_tel


class Lottery(Resource):
    # 抽奖--图鉴页面，获取抽奖进度
    def get(self):
        return get_lottery_process(session['open_id'])

    # 抽奖页面，抽奖按钮
    def post(self):
        return lottery(session['open_id'])

    # 抽奖页面，集齐后填写个人信息
    def put(self):
        data = request.get_json(force=True)
        check_tel(data.get('tel'))
        set_info(open_id=session['open_id'], data=data)
        return
