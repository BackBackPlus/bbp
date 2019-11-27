from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config as cg

from config import config



db = SQLAlchemy()


def create_app(config_name):

    # 实例化实现了wsgi接口功能的flask对象
    app = Flask(__name__)
    # 增加app系统配置
    app.config.from_object(cg[config_name])
    cg[config_name].init_app(app)
    from config import config



    # 实例化实现了wsgi接口功能的flask对象
    app = Flask(__name__)
    # 首先从config[config_name]中加载配置信息
    app.config.from_object(config[config_name])
    # app.init
    config[config_name].init_app(app)

    db.init_app(app)

    # 插入数据
    with app.test_request_context():
        db.create_all()
        from app import insert_word
        insert_word.cet4()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
