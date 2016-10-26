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

class exchangeCoinRecord(tornado.web.RequestHandler):
	"""docstring for exchangeCoinRecord"""
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}

		resp[KEY.EXCHANGE_RECORD] = db.check_transfer( { KEY.ID:params[KEY.ID] } )
		if(resp[KEY.EXCHANGE_RECORD] != -1):
			resp[KEY.STATUS] = STATUS.OK
		else:
			resp[KEY.STATUS] = STATUS.ERROR

		self.write(json_encode(resp))

