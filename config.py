import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 追踪对象的修改

    @staticmethod
    def init_app(app):
        pass


# 添加开发、测试和生产环境的数据库配置信息
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:123456@localhost/bbplus'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'mysql://用户名:密码@localhost/test_数据库名'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql://用户名:密码@localhost/数据库名'


# config 字典中注册了不同的配置环境，而且还注册了一个默认配置
# 分别作用于开发、测试、生成环境
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
