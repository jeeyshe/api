# coding: utf-8
"""
    Created by Lu Jianxin at 2019/02/26 09:57, for any questions contact me with jeeysie@gmail.com.
    Purpose of the file:
        0. 应用根模块
"""

import json

from flask import Response


# ---------------错误响应闭包

def handler(dic):
    def response(e):
        return Response(json.dumps(dic), content_type='application/json')

    return response
