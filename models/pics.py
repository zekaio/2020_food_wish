# -*- coding: utf-8 -*-
from . import db


class Pics(db.Model):
    __tablename__ = 'pics'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
