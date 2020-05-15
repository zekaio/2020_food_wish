# -*- coding: utf-8 -*-
from . import db
import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.Text, nullable=False)
    update_day = db.Column(db.Date, default=datetime.date.today())
    help = db.Column(db.Integer, nullable=False, default=3)
    wish = db.Column(db.Integer, nullable=False, default=3)
    lottery = db.Column(db.Integer, nullable=False, default=0)
    post = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self):
        return dict(
            help=self.help,
            wish=self.wish,
            lottery=self.lottery,
            post=self.post
        )
