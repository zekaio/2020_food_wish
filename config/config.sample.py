# -*- coding: utf-8 -*-
class DATABASE(object):
    USERNAME = ''  # 用户名
    PASSWORD = ''  # 密码
    HOST = 'localhost'
    PORT = 3306
    DBNAME = '2020_food_wish'


class BASECONFIG(object):
    IMG_DIR = './square/'  # 图片位置，相对前端根目录
    BEGIN = "2020-5-23 0:00:00"  # 活动开始时间
    END = "2020-5-30 0:00:00"  # 活动结束时间


class APPCONFIG(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        DATABASE.USERNAME, DATABASE.PASSWORD, DATABASE.HOST, DATABASE.PORT, DATABASE.DBNAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = ''  # 密钥
