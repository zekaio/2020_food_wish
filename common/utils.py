# -*- coding: utf-8 -*-
from flask import current_app
from flask_restful import abort
import json
import base64
import hashlib
import requests
import traceback
from config import config


def check_tel(tel: str) -> None:
    s = str(tel)
    if not (s.isdigit() and len(s) == 11 and s[0] == '1'):
        abort(412, message="手机号错误")
    return


def download_images(pics_id: list) -> list:
    pics_path = []
    for pic_id in pics_id:
        try:
            res = requests.get(
                'https://hemc.100steps.net/2017/wechat/Home/Public/getMedia?media_id=%s' % pic_id, timeout=30)
            t = json.loads(res.text)
        except:
            current_app.logger.error(traceback.format_exc())
            abort(412, message="上传图片失败")
            return []
        if t['status'] == 0:
            try:
                pic_path = config.BASECONFIG.IMG_DIR + hashlib.md5(
                    str(pic_id).encode('utf-8')).hexdigest() + '.jpg'
                with open('.' + pic_path, 'wb') as f:
                    f.write(base64.b64decode(t['data']))
                pics_path.append(pic_path)
            except:
                current_app.logger.error(traceback.format_exc())
                abort(412, message="服务器保存图片失败")
                return []
        else:
            current_app.logger.error(t['errMsg'])
            abort(412, message="服务器下载图片失败")
            return []
    return pics_path
