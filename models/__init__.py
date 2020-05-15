# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
import types

db = SQLAlchemy()

from .lottery import Lottery
from .pics import Pics
from .posts import Posts
from .wishes import Wishes
from .user import User
