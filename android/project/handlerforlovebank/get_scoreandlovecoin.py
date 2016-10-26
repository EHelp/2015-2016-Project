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

class Get_ScoreAndLovecoin(tornado.web.RequestHandler):
	'''
		获取用户个人爱心账户，包括爱心币，积分，家庭爱心币
	'''
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		if KEY.USER_ID in params:
			temp = {}
			temp[KEY.USER_ID] = params[KEY.USER_ID]
			resp = db.get_user_loving_bank(temp)
			resp[KEY.STATUS] = 200
		else:
			resp[KEY.STATUS] = 500
			
		self.write(json_encode(resp))