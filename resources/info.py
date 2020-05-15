# -*- coding: utf-8 -*-
from flask_restful import Resource


class Info(Resource):
    # 获取用户信息
    def get(self):
        return "get info"
