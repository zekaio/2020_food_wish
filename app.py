# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from config import config
from models import db
from resources import api

app = Flask(__name__)
CORS(app, supports_credentials=True)
db.init_app(app)
api.init_app(app)

app.config.from_object(config.APPCONFIG)

if __name__ == '__main__':
    app.run()
