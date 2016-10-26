#!/usr/bin/env python
# encoding: utf-8
import tornado.web
import json
import hashlib
import tornado
import random
import string
from tornado.web import RequestHandler
from tornado.escape import json_encode
from utils import utils
from utils import KEY
from utils import STATUS

from database import db
from utils import sendEmail

class ForgetPwdHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("selection.html")

class GetPwdEmailHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("phone.html")

class GetIdentiHandler(tornado.web.RequestHandler):
	def post(self):
		resp = {}
		resp[KEY.STATUS] = 500
		params = {}


		#对当前请求对象的参数解析，得到当前请求对象里面的参数
		params = utils.decode_params(self.request)
		
		if KEY.EMAIL in params and KEY.ACCOUNT in params:
			userInfo = {}
			userInfo = db.get_user_information_by_email(params)
			
			if userInfo is not None:
				if KEY.NICKNAME in userInfo and userInfo[KEY.NICKNAME] == params[KEY.ACCOUNT]:
					#获得验证码

					idencode = ''.join(random.sample(string.ascii_letters, 4))

					#emailt = email.PlainEmail()

					userEmail = params[KEY.EMAIL].replace('%40', '@')
					#if emailt.sendPlainEmail(params[KEY.EMAIL], "找回密码", "您的验证码为：" + idencode) == 200:
					if sendEmail.sendEmail([userEmail], "找回密码", "您的验证码为：" + idencode) == 200:
						md5_encode = hashlib.md5()
						md5_encode.update(userInfo[KEY.NICKNAME] + idencode)
						idencode = md5_encode.hexdigest()
						resp[KEY.STATUS] = 200
						resp["secret"] = idencode

		self.write(json_encode(resp))

class SetPwdHandler(tornado.web.RequestHandler):
	def get(self):

		self.render("setPwd.html", account = self.get_argument("account"))

	def post(self):
		params = {}
		resp = {}
		resp[KEY.STATUS] = STATUS.ERROR
		params = utils.decode_params(self.request)
		salt = db.get_salt(params)
		if salt:
			md5_encode = hashlib.md5()

			md5_encode.update(params[KEY.PASSWORD] + salt)
			params[KEY.PASSWORD] = md5_encode.hexdigest()
			isModfied = db.modify_password_For_Forget(params)
			if isModfied:
				resp[KEY.STATUS] = STATUS.OK

		self.write(json_encode(resp))