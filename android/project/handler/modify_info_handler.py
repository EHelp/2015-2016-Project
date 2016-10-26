#!/user/python
#-*- coding: utf-8 -*-

import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler

from utils import utils
from utils import KEY
from utils import STATUS
from database import db 

class Login_Handler(base_handler.BaseHandler):
	@tornado.web.authenticated
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
        
        resp[KEY.STATUS] = 200 
        user_id = db.validate_password(params)
   
        if user_id > 0:
            
            resp[KEY.ACCOUNT] = params[KEY.ACCOUNT]
            resp[KEY.ID] = user_id

            



        else:
            resp[KEY.STATUS] = 400
    
        #这里用来判断是不是用手机登录
        if not utils.is_App(self.request):
            self.set_secure_cookie("username", resp[KEY.ACCOUNT])
      
        self.write(json_encode(resp))




