# -*- coding: utf-8 -*-
__descriptions__ = """
    一些工具接口
"""

import json

from flask import Response, request, render_template
from flask.views import MethodView


def http_echo_view():
    json_data = request.get_json()
    response = Response(json.dumps(json_data), mimetype='application/json')
    return response
