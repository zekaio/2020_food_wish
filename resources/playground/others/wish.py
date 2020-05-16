# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource
from common.database import get_random_wish, help_wish


class Wish(Resource):
    # 助愿页面，抽取愿望
    def get(self):
        limit = request.args.get('limit')
        ret = get_random_wish(session['open_id'], limit) if limit else get_random_wish(session['open_id'])
        return dict(wishes=ret)

    # 助愿页面，选择帮助TA
    def post(self):
        wish_id = request.get_json(force=True)['id']
        help_wish(wish_id, session['open_id'])
        return
