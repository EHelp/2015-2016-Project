#!/usr/python
# -*- coding: utf-8 -*-

__author__ = 'hanks'

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

#Token，即计算机术语：令牌，符文
#这里的Token是为了调用融云app中的第三方库中标识身份的
class Get_Chat_Token_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)

    resp = {}
    chat_token = db.get_chat_token(params)
    if chat_token is None:
      resp[KEY.STATUS] = STATUS.ERROR
    else:
      resp[KEY.CHAT_TOKEN] = chat_token
      resp[KEY.STATUS] = STATUS.OK
      
    self.write(json_encode(resp))