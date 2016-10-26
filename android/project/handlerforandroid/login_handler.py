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

class Login_Handler(base_handler.BaseHandler):
  def post(self):
    params = utils.decode_params(self.request)
    resp = {}
    if KEY.SALT not in params:
      salt = db.get_salt(params)
      if salt is None:
        resp[KEY.STATUS] = 500
      else:
        resp[KEY.ACCOUNT] = params[KEY.ACCOUNT]
        resp[KEY.SALT] = salt
        user_id = db.validate_password(params)
        if user_id > 0:
          resp[KEY.STATUS] = 200
          resp[KEY.ID] = user_id
          self.set_secure_cookie(KEY.USER_NAME, resp[KEY.ACCOUNT])
          self.set_secure_cookie(KEY.ID, str(resp[KEY.ID]))
        else:
          resp[KEY.STATUS] = 300
    
    else:
      user_id = db.validate_password(params)
      if user_id > 0:
        resp[KEY.STATUS] = 200
        resp[KEY.ACCOUNT] = params[KEY.ACCOUNT]
        resp[KEY.ID] = user_id
        self.set_secure_cookie(KEY.USER_NAME, resp[KEY.ACCOUNT])
        self.set_secure_cookie(KEY.ID, str(resp[KEY.ID]))
      else:
        resp[KEY.STATUS] = 300

    self.write(json_encode(resp))
