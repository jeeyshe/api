# coding: utf-8
"""
    Created by Lu Jianxin at 2019/02/25 16:36, for any questions contact me with jeeysie@gmail.com.
    Purpose of the file:
        0. 
"""

from flask import Blueprint

from apps.link import views

app = Blueprint('link', __name__)

app.add_url_rule(rule='/zip/', endpoint='zip', view_func=views.LinkZip.as_view('zip'), methods=['GET', 'POST'])
