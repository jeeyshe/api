# coding: utf-8
"""
    Created by Lu Jianxin at 2019/02/25 17:01, for any questions contact me with jeeysie@gmail.com.
    Purpose of the file:
        0. 路由
"""

from flask import Blueprint

from apps.webhook import views

app = Blueprint('webhook', __name__)

app.add_url_rule(rule='/tencent-to-dingtalk/send', view_func=views.tencent_to_dingtalk, methods=['GET', 'POST'])
