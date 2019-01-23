#!/bin/sh
#chkconfig: 2345 80 90
#description: auto_run
# 配置webhook服务开机自启
source /root/venvs/webhook/bin/activate
cd /root/apps/robot/
gunicorn -c config.py app:app
