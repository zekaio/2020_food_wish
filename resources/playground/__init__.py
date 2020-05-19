# -*- coding: utf-8 -*-
from flask_restful import Api

playground_api = Api(prefix='/playground')

from . import others, player
from .lottery import Lottery
from .square import Square

playground_api.add_resource(Lottery, '/lottery')
playground_api.add_resource(Square, '/square')
playground_api.add_resource(others.Wish, '/others/wish', endpoint='/playground/others/wish')
playground_api.add_resource(player.Wish, '/player/wish', endpoint='/playground/player/wish')
