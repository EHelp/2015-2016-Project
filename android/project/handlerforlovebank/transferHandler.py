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

class transferHandler(tornado.web.RequestHandler):
	"""转账页面，传过来sender，receiver和lovecoin
		成功返还200，否则返还500
	"""
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		result = {}

		if KEY.SENDER in params and KEY.RECEIVER in params and KEY.LOVE_COIN in params:
			resp[KEY.SENDER] = params[KEY.SENDER]
			resp[KEY.RECEIVER] = params[KEY.RECEIVER]
			resp[KEY.LOVE_COIN] = params[KEY.LOVE_COIN]
			if(db.love_coin_transfer(resp)):
				result[KEY.STATUS] = 200
			else:
				result[KEY.STATUS] = 500
		else:
			result[KEY.STATUS] = 500

		self.write(json_encode(result))