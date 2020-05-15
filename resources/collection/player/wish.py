# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource
from common.database import get_my_wishes, wisher_confirm_complete


class Wish(Resource):
    # 我的许愿，获取所有愿望
    def get(self):
        return get_my_wishes(session['open_id'])

    # 我的许愿，确认愿望已被完成
    def post(self):
        wish_id = request.get_json(force=True)['id']
        wisher_confirm_complete(wish_id, session['open_id'])
        return
