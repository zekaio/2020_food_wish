# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource
from common.utils import check_tel
from common.database import make_wish


class Wish(Resource):
    # 许愿页面，许愿
    def post(self):
        data = request.get_json(force=True)
        check_tel(data['tel'])
        data['open_id'] = session['open_id']
        make_wish(data)
        return
