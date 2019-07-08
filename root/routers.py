# coding: utf-8
"""
    Created by Lu Jianxin at 2019/02/26 09:58, for any questions contact me with jeeysie@gmail.com.
    Purpose of the file:
        0. 
"""

from flask import Blueprint

from root import views

app = Blueprint('root', __name__)  # 此处的root是一个命名空间, 配合endpoint组合指定反向url, 例如root.index

# --------------------------------------------- #
# 首页视图
# --------------------------------------------- #

app.add_url_rule(rule='/index.html', endpoint='index', view_func=views.index_view)
app.add_url_rule('/', view_func=views.go_to_index)
app.add_url_rule('/index', view_func=views.go_to_index)
