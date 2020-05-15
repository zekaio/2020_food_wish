# -*- coding: utf-8 -*-
from flask import session
from flask_restful import Resource, abort


class Wish(Resource):
    # 我的许愿，获取所有愿望
    def get(self):
        pass

    # 我的许愿，确认愿望已被完成
    def post(self):
        pass
