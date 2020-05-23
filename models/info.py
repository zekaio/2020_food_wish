from . import db


class Info(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    tel = db.Column(db.String(11), nullable=False)
    address = db.Column(db.Text, nullable=False)
