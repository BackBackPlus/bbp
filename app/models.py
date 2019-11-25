from flask_sqlalchemy import SQLAlchemy
from flasky import app
from . import db

db = SQLAlchemy(app)


class Wrod(db.Model):
    __tablename__ = 'bbplus'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    word = db.Column(db.VARCHAR(64), unique=True)
    sw = db.Column(db.VARCHAR(64))
    phonetic = db.Column(db.VARCHAR(64))
    definition = db.Column(db.Text())
    translation = db.Column(db.Text())
    pos = db.Column(db.VARCHAR(16))
    collins = db.Column(db.Integer, default=0)
    oxford = db.Column(db.Integer, default=0)
    tag = db.Column(db.VARCHAR(64))
    bnc = db.Column(db.Integer)
    frq = db.Column(db.Integer)
    exchange = db.Column(db.Text())
    detail = db.Column(db.Text())
    audio = db.Column(db.Text())
