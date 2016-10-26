#!/usr/python
# -*- coding: utf-8 -*-

import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler

from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class transferChoose(tornado.web.RequestHandler):
	"""前端提供userid，state=0
		返还user列表"""
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		resp[KEY.USER_LIST] = db.query_follow(params)
		if resp[KEY.USER_LIST] == -1:
			resp[KEY.STATUS] = 500
		else:
			resp[KEY.STATUS] = 200
    
		self.write(json_encode(resp))
