# -*- coding: utf-8 -*-
__descriptions__ = """
* Auhtor: lujianxin@magexiot.com
* Env: py3.6.5 
* Time: 19-1-17 上午9:39
* IDE: PyCharm
* Purpose: ---文件作用描述---
    测试
"""

import json
import requests

from settings import *


def t1():
    url = 'http://127.0.0.1:5000/tencent-to-dingtalk/send?access_token=ce458b07441ec6281e40f32629d7011971cc48143dbdc34e5a4d40c5166cf23e'
    # url = 'http://io.isee.one/tencent-to-dingtalk/send?access_token=123456'
    json_data = {
        'name': 'lujianxin',
        'opts': {
            'x': 100,
            'y': 200
        }
    }
    res = requests.post(url, json=json.dumps(json_data))
    try:
        print(res.json())
    except:
        print(res.status_code)


def message():
    url = API_DINGTALK.format('ce458b07441ec6281e40f32629d7011971cc48143dbdc34e5a4d40c5166cf23e')
    json_data = json.dumps(LINK_TEMPLATE)
    headers = {
        'content-type': 'application/json;'
    }
    res = requests.post(url, data=json_data, headers=headers)
    try:
        print(res.json())
    except:
        print(res.status_code)


if __name__ == "__main__":
    # t1()
    message()
    pass
