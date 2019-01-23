# -*- coding: utf-8 -*-
__descriptions__ = """
* Auhtor: lujianxin@magexiot.com
* Env: py3.6.5 
* Time: 19-1-23 下午2:17
* IDE: PyCharm
* Purpose: ---文件作用描述---
    视图
"""

import json
from flask import Blueprint, request, Response

from apps.webhook.parse import parse_json_data

app_webhook = Blueprint('app_webhook', __name__)


@app_webhook.route('/tencent-to-dingtalk/send', methods=['POST', 'HEADER', 'GET'])
def tencent_to_dingtalk():
    """
    腾讯云开发者平台和钉钉的webhook转发服务器
    - 平台没有提供钉钉的格式，直接发送钉钉接不到。
    """
    access_token = request.args.get('access_token', '')
    data = request.get_json()
    result = parse_json_data(access_token, data)
    return Response(json.dumps({'errmsg': 'OK', 'errcode': 10000, 'result': result}))


if __name__ == "__main__":
    pass
