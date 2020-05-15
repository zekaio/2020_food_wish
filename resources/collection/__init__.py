# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

collection_bp = Blueprint('collection', __name__)
collection_api = Api(collection_bp)

from . import others, player

collection_api.add_resource(others.Wish, '/others/wish', endpoint='/collection/others/wish')
collection_api.add_resource(player.Wish, '/player/wish', endpoint='/collection/player/wish')
