# -*- coding: utf-8 -*-
__descriptions__ = """
* Auhtor: lujianxin@magexiot.com
* Env: py3.6.5 
* Time: 19-1-16 下午3:49
* IDE: PyCharm
* Purpose: ---文件作用描述---
    一些配置
"""

import os
import sys

BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, BASE_DIR)

DEBUG = True

SERVER_NAME = 'api.xoo.site' if not DEBUG else '127.0.0.1:5000'

SECRET_KEY = '2019/01/19-start-webhook-server-use-this-key'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# 错误处理
ERRORS = {
    400: {'code': 400, 'msg': 'bad request, invalid params maybe'},
    401: {'code': 401, 'msg': 'permission denied'},
    403: {'code': 403, 'msg': 'action forbidden'},
    404: {'code': 404, 'msg': 'url not found'},
    405: {'code': 405, 'msg': 'method not allowed'},
    500: {'code': 500, 'msg': 'server error occurred'},
}

# 转发给钉钉的api
API_DINGTALK = 'https://oapi.dingtalk.com/robot/send?access_token={}'

# 默认请求头
HEADERS = {
    'content-type': 'application/json;'
}

# 测试消息模板
PING = '{}在[{}]项目发送了一条测试消息: 我欲乘风归去,又恐琼楼玉宇, 高处不胜寒.起舞弄清影,何似在人间.'

# 提交代码
COMMIT = """
### 有人提交代码啦
- 项目: {project}\n
- 分支: {branch}\n
- 作者: {author}\n
- 链接: [{link_txt}]({link})\n
- 说明: {desc}
"""

# 代码变动标题
PUSH_TITLE = '代码库变动提醒'

# 任务变动标题
TASK_TITLE_FINISH = 'Nice，任务完成啦！'
TASK_TITLE_CREATE = 'Look，有新的任务！'
TASK_TITLE_LABEL = 'Look，任务标签有变化！'
TASK_TITLE_ASSIGN = 'Look，分配任务啦！'
TASK_TITLE_DELETE = 'Nice，任务被删掉一个哦！'
TASK_TITLE_UPDATE = 'Look，任务内容有变动！'
TASK_TITLE_REOPEN = 'Fuck，有一个任务重启了！'
TASK_TITLE_WATCHER_ADD = 'Look，赶紧看看你是不是任务关注者！'
TASK_TITLE_WATCHER_RM = 'Nice，你可能少了一个任务！'

# 任务变动描述
TASK_FINISH = '[{user}]完成了任务:{task}'
TASK_CREATE = '[{user}]创建了任务:{task},将任务分配给[{worker}]'
TASK_LABEL = '[{user}]给任务:{task},添加了新标签'
TASK_ASSIGNED = '[{user}]将任务:{task},分配给了[{worker}]'
TASK_DELETE = '[{user}]删除了任务:{task}'
TASK_UPDATE = '[{user}]更新了任务:{task}'
TASK_REOPEN = '[{user}]重启了任务:{task}'
TASK_WATCHER_ADD = '[{user}]给任务[{task}]添加了新的关注者'
TASK_WATCHER_DEL = '[{user}]给任务[{task}]移除了关注者'

# 文件变更标题
FILE_TITLE_UPLOAD = '有新文件上传啦'
FILE_TITLE_RENAME = '文件被重新命名'
FILE_TITLE_REMOVE = '有文件被删除！'

# 文件变动描述
FILE_UPLOAD = '[{user}]上传了文件:{file}'
FILE_RENAME = '[{user}]将一个文件重命名为[{new}]'
FILE_REMOVE = '[{user}]删除了文件:{file}'

AUTH_TOKEN = {
    'Auth-Token': 'api.xoo.site',
}
