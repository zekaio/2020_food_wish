# -*- coding: utf-8 -*-
from flask import session, request, current_app
from flask_restful import Resource, abort
from common.database import get_posts, send_post
import json
import base64
import hashlib
import requests
import traceback
from config import config


class Square(Resource):
    # 广场页面，获取帖子
    def get(self):
        limit = request.args.get('limit') if request.args.get('limit') else 5
        offset = request.args.get('offset') if request.args.get('offset') else 0
        return dict(posts=get_posts(offset, limit))

    # 广场，发帖
    def post(self):
        data: dict = request.get_json(force=True)
        pics_path = data.get('pics_id') or []
        # pics_path = list()
        # if data.get('pics_id'):
        #     for pic_id in data['pics_id']:
        #         try:
        #             res = requests.get(
        #                 'https://hemc.100steps.net/2017/wechat/Home/Public/getMedia?media_id=%s' % pic_id, timeout=30)
        #             t = json.loads(res.text)
        #         except:
        #             current_app.logger.error(traceback.format_exc())
        #             abort(412, message="上传图片失败")
        #             return
        #         if t['status'] == 0:
        #             try:
        #                 pic_path = config.BASECONFIG.IMG_DIR + hashlib.md5(
        #                     str(pic_id).encode('utf-8')).hexdigest() + '.jpg'
        #                 pics_path.append(pic_path)
        #                 with open(pic_path, 'wb') as f:
        #                     f.write(base64.b64decode(t['data']))
        #             except Exception:
        #                 current_app.logger.error(traceback.format_exc())
        #                 abort(412, message="服务器保存图片失败")
        #                 return
        #         else:
        #             current_app.logger.error(t['errMsg'])
        #             abort(412, message="服务器下载图片失败")
        #             return
        send_post(dict(open_id=session['open_id'], content=data['content']), pics_path)
        return
