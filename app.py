# coding: utf-8
import json
import requests

from flask import Flask, request, Response, render_template, redirect, url_for, Blueprint

from settings import *

app = Flask(__name__)
app.config['SERVER_NAME'] = SERVER_NAME
app.secret_key = SECRET_KEY


# --------------------------------------------- #
#       蓝图注册,模块拆分
# --------------------------------------------- #
from apps.webhook.views import app_webhook


# webhook服务
app.register_blueprint(blueprint=app_webhook, url_prefix='/webhook')


# --------------------------------------------- #
# 添加错误处理响应
# --------------------------------------------- #
@app.errorhandler
def bad_request(e):
    return Response(json.dumps(MSG_FOR_400))


@app.errorhandler(401)
def permission_denied(e):
    return Response(json.dumps(MSG_FOR_401))


@app.errorhandler(403)
def forbidden_handler(e):
    return Response(json.dumps(MSG_FOR_403))


@app.errorhandler(404)
def not_found(e):
    return Response(json.dumps(MSG_FOR_404))


@app.errorhandler(405)
def method_not_allowed(e):
    return Response(json.dumps(MSG_FOR_405))


@app.errorhandler(500)
def internal_error(e):
    return Response(json.dumps(MSG_FOR_500))


# ------------------------------------------------- #
# 首页的视图,响应
# ------------------------------------------------- #
@app.route('/index.html', endpoint='index')
def index():
    return render_template('index.html')


@app.route('/index')
def go_to_index_0():
    return redirect(url_for('index'))


@app.route('/')
def go_to_index_1():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
