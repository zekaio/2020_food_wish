# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

api = Api()

from .info import Info

api.add_resource(Info, '/info')

from .playground import playground_bp
from .collection import collection_bp
