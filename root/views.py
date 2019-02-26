# coding: utf-8
"""
    Created by Lu Jianxin at 2019/02/26 09:57, for any questions contact me with jeeysie@gmail.com.
    Purpose of the file:
        0. 
"""

from flask import render_template, redirect, url_for


# ------------------------------------------------- #
# 首页的视图,响应
# ------------------------------------------------- #
def index_view():
    return render_template('index.html')


def go_to_index():
    return redirect(url_for('root.index'))
