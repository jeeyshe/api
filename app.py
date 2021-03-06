# coding: utf-8

from flask import Flask

from settings import *
from apps.webhook.routers import app as webhook_app
from apps.tools.routers import app as tools_app
from root import handler
from root.routers import app as root_app

app = Flask(__name__)
app.config.update(
    SERVER_NAME=SERVER_NAME,
    SECRET_KEY=SECRET_KEY,
)

# --------------------------------------------- #
#       蓝图注册,模块拆分
# --------------------------------------------- #
# 根目录模块
app.register_blueprint(blueprint=root_app)
# webhook服务
app.register_blueprint(blueprint=webhook_app, url_prefix='/webhook')
# 一些工具
app.register_blueprint(blueprint=tools_app, url_prefix='/tools')

# --------------------------------------------- #
# 添加错误处理响应
# --------------------------------------------- #
for e in ERRORS:
    app.register_error_handler(e, handler(ERRORS[e]))

if __name__ == '__main__':
    app.run(debug=True)
