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

class ChangePWDHandler(base_handler.BaseHandler):
  def post(self):
    params = utils.decode_params(self.request)
    resp = {}
    if KEY.SALT in params and KEY.PASSWORD in params and KEY.PHONE in params and KEY.NEW_PASSWORD in params:
      params[KEY.ACCOUNT] = db.get_account_by_phone({KEY.PHONE: params[KEY.PHONE]})
      user_id = db.validate_password(params)

      if user_id > 0:
        if db.android_modify_password({KEY.PASSWORD: params[KEY.NEW_PASSWORD], KEY.PHONE: params[KEY.PHONE]}):
            resp[KEY.STATUS] = 200
        else:
            resp[KEY.STATUS] = 300
      else:
        resp[KEY.STATUS] = 400
    else:
      resp[KEY.STATUS] = 500

    self.write(json_encode(resp))
