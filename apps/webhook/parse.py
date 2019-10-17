# -*- coding: utf-8 -*-
__descriptions__ = """
* Auhtor: jeeyshe@gmail.com
* Env: py3.6.5 
* Time: 19-1-17 下午3:31
* IDE: PyCharm
* Purpose: ---文件作用描述---
    解析json数据
"""

from apps.webhook.send import send_link, send_md, send_text
from settings import *


def parse_json_data(access_token, data=None):
    """解析coding发来的数据"""
    if data is None:
        return {}

    result = None
    if 'zen' in data:
        # 测试消息---------------------------------------------------
        return send_text(
            access_token=access_token,
            content=PING.format(data['sender']['name'], data['repository']['name']),
            is_at_all=False,
        )
    elif 'task' in data:
        # 任务消息-------------------------------------------------
        if data['action'] == 'closed':
            # 完成任务
            return send_link(
                access_token=access_token,
                title=TASK_TITLE_FINISH,
                text=TASK_FINISH.format(
                    user=data['task']['user']['name'],
                    task=data['task']['title']
                ),
                message_url=data['task']['html_url']
            )
        if data['action'] == 'opened':
            # 创建任务
            return send_link(
                access_token=access_token,
                title=TASK_TITLE_CREATE,
                text=TASK_CREATE.format(
                    user=data['task']['user']['name'],
                    task=data['task']['title'],
                    worker=data['task']['assignee']['name']
                ),
                message_url=data['task']['html_url']
            )
        if data['action'] == 'labeled':
            # 给任务添加标签
            return send_link(
                access_token=access_token,
                title=TASK_TITLE_LABEL,
                text=TASK_LABEL.format(
                    user=data['task']['user']['name'],
                    task=data['task']['title']
                ),
                message_url=data['task']['html_url']
            )
        if data['action'] == 'assigned':
            # 任务分配
            return send_link(
                access_token=access_token,
                title=TASK_TITLE_ASSIGN,
                text=TASK_ASSIGNED.format(
                    user=data['task']['user']['name'],
                    task=data['task']['title'],
                    worker=data['task']['assignee']['name']
                ),
                message_url=data['task']['html_url']
            )
        if data['action'] == 'deleted':
            # 删除任务
            return send_link(
                access_token=access_token,
                title=TASK_TITLE_DELETE,
                text=TASK_DELETE.format(
                    user=data['task']['user']['name'],
                    task=data['task']['title']
                ),
                message_url=data['task']['html_url']
            )
        if data['action'] == 'edited':
            # 更新任务
            return send_link(
                access_token=access_token,
                title=TASK_TITLE_UPDATE,
                text=TASK_ASSIGNED.format(
                    user=data['task']['user']['name'],
                    task=data['task']['title'],
                ),
                message_url=data['task']['html_url']
            )
        if data['action'] == 'reopened':
            # 重启任务
            return send_link(
                access_token=access_token,
                title=TASK_TITLE_REOPEN,
                text=TASK_REOPEN.format(
                    user=data['task']['user']['name'],
                    task=data['task']['title']
                ),
                message_url=data['task']['html_url']
            )
        if data['action'] == 'add watcher':
            # 添加关注者
            return send_link(
                access_token=access_token,
                title=TASK_TITLE_WATCHER_ADD,
                text=TASK_WATCHER_ADD.format(
                    user=data['task']['user']['name'],
                    task=data['task']['title']
                ),
                message_url=data['task']['html_url']
            )
        if data['action'] == 'remove watcher':
            # 移除关注者
            return send_link(
                access_token=access_token,
                title=TASK_TITLE_WATCHER_RM,
                text=TASK_WATCHER_DEL.format(
                    user=data['task']['user']['name'],
                    task=data['task']['title'],
                ),
                message_url=data['task']['html_url']
            )
    elif 'document' in data:
        # 文件变更 ------------------------------------------------
        if data['action'] == 'upload_file':
            # 上传文件
            return send_link(
                access_token=access_token,
                title=FILE_TITLE_UPLOAD,
                text=FILE_UPLOAD.format(
                    user=data['document']['user']['name'],
                    file=data['document']['name']
                ),
                message_url=data['document']['html_url']
            )
        if data['action'] == 'rename':
            # 文件重命名
            return send_link(
                access_token=access_token,
                title=FILE_TITLE_RENAME,
                text=FILE_RENAME.format(
                    user=data['document']['user']['name'],
                    new=data['document']['name']
                ),
                message_url=data['document']['html_url']
            )
        if data['action'] == 'delete_file':
            # 删除文件
            return send_link(
                access_token=access_token,
                title=FILE_TITLE_REMOVE,
                text=FILE_REMOVE.format(
                    user=data['document']['user']['name'],
                    file=data['document']['name']
                ),
                message_url=data['document']['html_url']
            )
    elif 'ref' in data:
        # 代码提交 -----------------------------------------------------------
        return send_md(
            access_token=access_token,
            title=PUSH_TITLE,
            md=COMMIT.format(
                project=data['repository']['name'],
                branch=data['ref'].split('/')[-1],
                author=data['commits'][0]['committer']['name'],
                desc=data['commits'][0]['message'],
                link_txt=data['repository']['clone_url'],
                link=data['repository']['clone_url']
            )
        )
    else:
        pass
    return result


if __name__ == "__main__":
    pass
