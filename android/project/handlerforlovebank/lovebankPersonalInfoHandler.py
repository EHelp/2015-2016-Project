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

class lovebank_personal_info(tornado.web.RequestHandler):
	"""返还爱心账户个人信息，包括名字，积分，爱心币等"""
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}

		if KEY.USER_ID in params:
			resp = db.get_user_loving_bank( { KEY.USER_ID:params[KEY.USER_ID] } )
			resp[KEY.NICKNAME] = db.get_userName( { KEY.ID:params[KEY.USER_ID] } )[0]
			resp[KEY.STATUS] = 200			
		else:
			resp[KEY.STATUS] = 500

		self.write(json_encode(resp))

