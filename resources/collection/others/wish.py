# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource
from common.database import get_my_help, giveup_wish, helper_confirm_complete


class Wish(Resource):
    # 我的助愿，获取所有愿望
    def get(self):
        return dict(wishes=get_my_help(session['open_id']))

    # 我的助愿，我已实现/放弃
    def post(self):
        data = request.get_json(force=True)
        if int(data['status']):
            helper_confirm_complete(data['id'], session['open_id'])
        else:
            giveup_wish(data['id'], session['open_id'])
        return
