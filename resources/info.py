# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource
from common.database import get_user_info, set_username


class Info(Resource):
    # 获取用户信息
    def get(self):
        return get_user_info(session['open_id'])

    def post(self):
        data = request.get_json(force=True)
        set_username(data['username'], session['open_id'])
        return
