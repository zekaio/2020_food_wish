# -*- coding: utf-8 -*-
from . import db


class Wishes(db.Model):
    __tablename__ = 'wishes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.Text, nullable=False, comment='许愿者openid')
    helper_openid = db.Column(db.Text, comment='助愿人openid')
    name = db.Column(db.Text, nullable=False, comment='许愿者姓名')
    tel = db.Column(db.String(11), default="", comment='许愿者手机号')
    wechat = db.Column(db.Text, comment='许愿者微信')
    content = db.Column(db.Text, nullable=False, comment='许愿内容')
    paper = db.Column(db.Integer, nullable=False, comment='信纸id')
    status = db.Column(db.Integer, default=0, comment='愿望状态，0未被领取，1已领取未完成，2已完成未确认，3完成并确认')

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            tel=self.tel,
            wechat=self.wechat,
            content=self.content,
            paper=self.paper,
            status=self.status
        )
