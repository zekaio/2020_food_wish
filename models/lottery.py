# -*- coding: utf-8 -*-
from . import db


class Lottery(db.Model):
    __tablename__ = 'lottery'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.Text, nullable=False)
