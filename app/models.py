from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flasky import app
from . import db



class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    word = db.Column(db.VARCHAR(64), unique=True)
    phonetic = db.Column(db.VARCHAR(64))
    definition = db.Column(db.Text())
    translation = db.Column(db.Text())
    tag = db.Column(db.VARCHAR(64))
    #
    # @staticmethod
    # def insert_words(csv_file_path, table_name, database):
    #     """批量添加单词数据到词库"""
    #     import pandas as pd
    #     df = pd.read_csv(csv_file_path, keep_default_na=False, encoding='utf-8')
    #     values = df.values.tolist()
    pass


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(20))


class Plan(db.Model):
    __tablename__ = 'plans'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    tag = db.Column(db.VARCHAR(20))
    word_pos = db.Column(db.Integer)
    last_time = db.Column(db.DateTime(), default=datetime.utcnow)
