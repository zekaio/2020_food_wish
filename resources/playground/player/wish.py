# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource, abort
from common.utils import check_tel
from common.database import make_wish


class Wish(Resource):
    # 许愿页面，许愿
    def post(self):
        data: dict = request.get_json(force=True)
        if not (data.get('tel') or data.get('wechat')):
            abort(412, message="请填写手机号或微信号")
        if data.get('tel'):
            check_tel(data['tel'])
        data['open_id'] = session['open_id']
        make_wish(data)
        return
