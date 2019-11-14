from flask import Flask


def create_app() -> Flask:
    from config import BaseConfig
    # 实例化实现了wsgi接口功能的flask对象
    app = Flask(__name__)
    # 增加app系统配置
    app.config.from_object(BaseConfig)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app