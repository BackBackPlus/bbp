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
    # sw = db.Column(db.VARCHAR(64))
    phonetic = db.Column(db.VARCHAR(64))
    definition = db.Column(db.Text())
    translation = db.Column(db.Text())
    # pos = db.Column(db.VARCHAR(16))
    # collins = db.Column(db.Integer, default=0)
    # oxford = db.Column(db.Integer, default=0)
    tag = db.Column(db.VARCHAR(64))
    # bnc = db.Column(db.Integer)
    # frq = db.Column(db.Integer)
    # exchange = db.Column(db.Text())
    # detail = db.Column(db.Text())
    # audio = db.Column(db.Text())

    @staticmethod
    def insert_words(csv_file_path, table_name, database):
        """批量添加单词数据到词库"""
        pass



class User(db.Model):
    """用户背单词数据表"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)


class Plan(db.Model):
    __tablename__ = 'plans'
    id = db.Column(db.Integer, primary_key=True)
