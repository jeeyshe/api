# -*- coding: utf-8 -*-
__descriptions__ = """
    一些工具接口
"""

import logging
import json

from flask import Response, request, render_template
from flask.views import MethodView

logger = logging.getLogger(__name__)


def http_echo_view():
    json_data = json.dumps(request.get_json())
    logger.info(json_data)
    response = Response(json_data, mimetype='application/json')
    return response
