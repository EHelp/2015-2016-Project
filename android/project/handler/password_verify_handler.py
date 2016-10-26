#!/usr/python
#coding:utf-8
import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler

from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Password_Verify_Handler(base_handler.BaseHandler):
	@tornado.web.authenticated
	def post(self):
		params = utils.decode_params(self.request)
		#传过来用户id 和 加密后的密码

		if KEY.ID in params:
			params[KEY.ID] = int(params[KEY.ID])
			
			password = db.get_password_by_id(params)

			resp = {}
			if (password is None):
				resp[KEY.STATUS]= 500
			else:
				if password == params[KEY.PASSWORD]:
					resp[KEY.STATUS] = 200
					self.set_secure_cookie("passwordVerify", "yes")
				else:
					resp[KEY.STATUS] = 400
			self.write(json_encode(resp))

    


