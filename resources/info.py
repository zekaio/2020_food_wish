# -*- coding: utf-8 -*-
from flask import session
from flask_restful import Resource
from common.database import get_user_info


class Info(Resource):
    # 获取用户信息
    def get(self):
        return get_user_info(session['open_id'])
