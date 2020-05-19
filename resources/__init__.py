# -*- coding: utf-8 -*-
from flask_restful import Api

base_api = Api()

from .info import Info

base_api.add_resource(Info, '/info')

from .playground import playground_api
from .collection import collection_api
