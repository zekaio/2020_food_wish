# -*- coding: utf-8 -*-
from flask import session
from flask_restful import Resource, abort


class Wish(Resource):
    # 我的助愿，获取所有愿望
    def get(self):
        pass


    # 我的助愿，我已实现/放弃
    def post(self):
        pass
