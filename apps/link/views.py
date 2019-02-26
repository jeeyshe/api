# -*- coding: utf-8 -*-
__descriptions__ = """
* Auhtor: lujianxin@magexiot.com
* Env: py3.6.5 
* Time: 19-1-23 下午2:35
* IDE: PyCharm
* Purpose: ---文件作用描述---
    压缩网址视图
"""

from flask import Response, request, render_template
from flask.views import MethodView


class LinkZip(MethodView):

    def get(self):
        """
        返回页面文件
        """
        return render_template('linkzip.html')

    def post(self):
        old_url = request.form.get('url', None)
        if not old_url:
            pass
        return Response('nihoay')
