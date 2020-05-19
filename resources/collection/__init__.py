# -*- coding: utf-8 -*-
from flask_restful import Api

collection_api = Api(prefix='/collection')

from . import others, player

collection_api.add_resource(others.Wish, '/others/wish', endpoint='/collection/others/wish')
collection_api.add_resource(player.Wish, '/player/wish', endpoint='/collection/player/wish')
