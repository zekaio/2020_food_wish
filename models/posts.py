# -*- coding: utf-8 -*-
from . import db


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    pics = db.relationship('Pics', backref='post')

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            content=self.content
        )
