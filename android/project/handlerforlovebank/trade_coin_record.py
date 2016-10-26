#!/usr/python
# -*- coding: utf-8 -*-

import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode

from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class tradeCoinRecord(tornado.web.RequestHandler):
	"""docstring for exchangeCoinRecord"""
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}

		temp = {}
		temp[KEY.ID] = params[KEY.ID]
		resp[KEY.TRADE_RECORD] = db.get_trade(temp)
		if(resp[KEY.TRADE_RECORD] != -1):
			resp[KEY.STATUS] = STATUS.OK
		else:
			resp[KEY.STATUS] = STATUS.ERROR

		self.write(json_encode(resp))


