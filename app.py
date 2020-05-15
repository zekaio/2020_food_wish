# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from config import config
from models import db
from resources import api, playground_bp, collection_bp

app = Flask(__name__)
app.config.from_object(config.APPCONFIG)
CORS(app, supports_credentials=True)

db.init_app(app)
api.init_app(app)
app.register_blueprint(playground_bp, url_prefix='/playground')
app.register_blueprint(collection_bp, url_prefix='/collection')

if __name__ == '__main__':
    app.run()
