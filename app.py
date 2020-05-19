# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from config import config
from models import db
from resources import base_api, playground_api, collection_api
from middleware import before_request

app = Flask(__name__)
app.config.from_object(config.APPCONFIG)
CORS(app, supports_credentials=True)

db.init_app(app)

base_api.init_app(app)
playground_api.init_app(app)
collection_api.init_app(app)

app.before_request(before_request)

"""
for test
"""


@app.route('/set_open_id', methods=['post'])
def openid():
    from flask import session, request
    session['open_id'] = request.get_json(force=True)['openid']
    return str(session['open_id'])


if __name__ == '__main__':
    app.run()
