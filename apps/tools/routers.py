# coding: utf-8
"""
    Created by Lu Jianxin at 2019/02/25 16:36, for any questions contact me with jeeysie@gmail.com.
    Purpose of the file:
        0. 
"""

from flask import Blueprint

from apps.tools import views

app = Blueprint('tools', __name__)

app.add_url_rule('/echo', endpoint='echo', view_func=views.http_echo_view, methods=['POST'])
