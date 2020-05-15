# -*- coding: utf-8 -*-
from flask import session, request
from flask_restful import Resource
from common.database import get_posts, send_post


class Square(Resource):
    # 广场页面，获取帖子
    def get(self):
        limit = request.args.get('limit') if request.args.get('limit') else 5
        offset = request.args.get('offset') if request.args.get('offset') else 0
        return get_posts(offset, limit)

    # 广场，发帖
    def post(self):
        data = request.get_json(force=True)
        if data.get('pics_id'):
            # 下载图片
            pass
        send_post(dict(open_id=session['open_id'], name=data['name'], content=data['content']), data.get('pics_id'))
        return
