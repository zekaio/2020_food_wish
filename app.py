# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from config import config
from models import db
from resources import api, playground_bp, collection_bp
from middleware import before_request

app = Flask(__name__)
app.config.from_object(config.APPCONFIG)
CORS(app, supports_credentials=True)

db.init_app(app)
api.init_app(app)
app.register_blueprint(playground_bp, url_prefix='/playground')
app.register_blueprint(collection_bp, url_prefix='/collection')
app.before_request(before_request)

"""
for test
"""


@app.route('/openid')
def set_open_id():
    from flask import session
    session['open_id'] = 1
    return str(session['open_id'])


@app.route('/set_open_id', methods=['post'])
def openid():
    from flask import session, request
    session['open_id'] = request.get_json(force=True)['openid']
    return str(session['open_id'])


if __name__ == '__main__':
    app.run()
