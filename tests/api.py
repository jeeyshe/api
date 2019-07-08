#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
# FileName: api.py
# Desc: ***
# Author: lujianxin
# Email: jianxin.lu@woqutech.com
# HomePage: www.woqutech.com
# Version: 7.0.0
# Created: 2019/7/8 上午10:14
#=============================================================================
"""

import json
import requests


def echo():
    url = 'http://127.0.0.1:5000/tools/echo'

    data = {
        'name': 'xxx',
        'pwd': 'ccc',
        'message': '你发啥我就回复啥'
    }

    print(requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'}).json())


if __name__ == '__main__':
    echo()
