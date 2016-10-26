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
from database import dblove

class get_system_user_information(tornado.web.RequestHandler):
	"""计算用户登录数据的接口函数，获取3个数据
		1. 当天系统所有用户数量
		2. 当天系统用户登录数量
		3. 最近一周用户登录情况
	"""
	def post(self):
		#params = utils.decode_params(self.request)
		resp = {}

		resp[KEY.NUM_OF_USER] = dblove.calculate_number_of_user()
		resp[KEY.NUM_OF_LOGIN] = dblove.calculate_number_of_login()
		resp[KEY.LOGIN_INFORMATION] = dblove.calculate_number_of_login_weekly()
		
		if resp[KEY.LOGIN_INFORMATION] is not None:
			resp[KEY.STATUS] = 200
		else:
			resp[KEY.STATUS] = 500
		
		self.write(json_encode(resp))
