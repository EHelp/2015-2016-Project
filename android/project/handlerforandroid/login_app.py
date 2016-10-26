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

class Login_Handler(base_handler.BaseHandler):
  def post(self):
    params = utils.decode_params(self.request)
    resp = {}
    
    if KEY.SALT in params and KEY.PASSWORD in params and KEY.PHONE in params:
      params[KEY.ACCOUNT] = db.get_account_by_phone({KEY.PHONE: params[KEY.PHONE]})
      user_id = db.validate_password(params)
      
      if user_id > 0:
        resp[KEY.STATUS] = 200
        resp[KEY.ACCOUNT] = params[KEY.ACCOUNT]
        resp[KEY.ID] = user_id
        
        if(dblove.record_login({KEY.ID:user_id})):
            resp[KEY.STATUS] = 200
        else:
            resp[KEY.STATUS] = 500

      else:
        resp[KEY.STATUS] = 500
    else:
      resp[KEY.STATUS] = 500

    self.write(json_encode(resp))
