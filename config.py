# -*- coding: utf-8 -*-
__descriptions__ = """
* Auhtor: lujianxin@magexiot.com
* Env: py3.6.5 
* Time: 19-1-16 下午5:52
* IDE: PyCharm
* Purpose: ---文件作用描述---
    gunicorn 部署文件
"""
# config.py
import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

# debug = True
loglevel = 'debug'
bind = "127.0.0.1:8080"
pidfile = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/debug.log"
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()*2 + 1
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'


if __name__ == "__main__":
    pass
