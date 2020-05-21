# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource, abort
from common.utils import check_tel
from common.database import make_wish


class Wish(Resource):
    # 许愿页面，许愿
    def post(self):
        data: dict = request.get_json(force=True)
        tel = data.get('tel') if data.get('tel') else ''
        wechat = data.get('wechat') if data.get('wechat') else ''
        if not data.get('content'):
            abort(412, message='请填写许愿内容')
        if not (tel or wechat):
            abort(412, message="请填写手机号或微信号")
        if tel:
            check_tel(tel)
        make_wish(dict(open_id=session['open_id'], tel=tel, wechat=wechat, content=data.get('content'),
                       paper=data.get('paper'), name=data.get('name')))
        return
