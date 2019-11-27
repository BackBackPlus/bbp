import os

from app import create_app

# 如果已经定义了环境变量FLASK_CONFIG，则从中读取配置名；
# 否则使用默认配置。
app = create_app(os.getenv('FLASK_CONFIG') or 'default')


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
