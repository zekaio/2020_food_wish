# -*- coding: utf-8 -*-
from . import db


class Lottery(db.Model):
    __tablename__ = 'lottery'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.Text, nullable=False)
    food1 = db.Column(db.Integer, nullable=False, default=0)
    food2 = db.Column(db.Integer, nullable=False, default=0)
    food3 = db.Column(db.Integer, nullable=False, default=0)
    food4 = db.Column(db.Integer, nullable=False, default=0)
    food5 = db.Column(db.Integer, nullable=False, default=0)
    food6 = db.Column(db.Integer, nullable=False, default=0)
    food7 = db.Column(db.Integer, nullable=False, default=0)
    food8 = db.Column(db.Integer, nullable=False, default=0)

    def to_list(self) -> list:
        return [self.food1, self.food2, self.food3, self.food4, self.food5, self.food6, self.food7, self.food8]

    def get_incomplete(self) -> dict:
        d = {}
        for i, val in enumerate(self.to_list()):
            if val != 3:
                d[i] = val
        return d
