# -*- coding: utf-8 -*-
__descriptions__ = """
* Auhtor: lujianxin@magexiot.com
* Env: py3.6.5 
* Time: 19-1-17 下午2:21
* IDE: PyCharm
* Purpose: ---文件作用描述---
    钉钉机器人的一些消息格式。
"""

import json
import requests

from settings import API_DINGTALK, HEADERS


def send_text(access_token, content, at_mobiles=None, is_at_all=True):
    """
    发送文本消息
    """
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": at_mobiles if isinstance(at_mobiles, list) else [],
            "isAtAll": is_at_all
        }
    }

    result = requests.post(url=API_DINGTALK.format(access_token), data=json.dumps(data), headers=HEADERS)

    return result.json()


def send_md(access_token, title, md, at_mobiles=None, is_at_all=True):
    """
    发送markdown
    """
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": md,
        },
        "at": {
            "atMobiles": at_mobiles if isinstance(at_mobiles, list) else [],
            "isAtAll": is_at_all
        }
    }
    result = requests.post(url=API_DINGTALK.format(access_token), data=json.dumps(data), headers=HEADERS)

    return result.json()


def send_link(access_token, title, text, message_url, pic_url=''):
    """
    发送链接
    """
    data = {
        "msgtype": "link",
        "link": {
            "text": text,
            "title": title,
            "picUrl": pic_url,
            "messageUrl": message_url
        }
    }
    result = requests.post(url=API_DINGTALK.format(access_token), data=json.dumps(data), headers=HEADERS)

    return result.json()


if __name__ == "__main__":
    pass
