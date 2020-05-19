# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource
from common.database import get_posts, send_post


class Square(Resource):
    # 广场页面，获取帖子
    def get(self):
        offset = request.args.get('offset')
        limit = request.args.get('limit') or 5
        return dict(posts=get_posts(offset, limit))

    # 广场，发帖
    def post(self):
        data: dict = request.get_json(force=True)
        send_post(session['open_id'], data)
        return
