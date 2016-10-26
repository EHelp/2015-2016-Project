#!/usr/python
# encoding: utf-8
import tornado.httpserver
import tornado
import random
import string
import hashlib

from tornado.web import RequestHandler
from tornado.escape import json_encode
from utils import utils
from utils import KEY
from utils import STATUS
from database import db
from utils import sendEmail

class Regist_Handler(RequestHandler):

  def post(self):
    params = utils.decode_params(self.request)
    resp = {}

    if utils.is_App(self.request):
      user_id = db.add_account(params)
    else:
      user_id = db.web_add_account(params)
    
    resp = {}
    
    if user_id > 0:
      resp[KEY.STATUS] = STATUS.OK
      resp[KEY.ACCOUNT] = params[KEY.ACCOUNT]
      resp[KEY.ID] = user_id
      resp[KEY.SALT] = db.get_salt(params)
      resp[KEY.CHAT_TOKEN] = db.get_chat_token(params)
      bank_account_id = db.create_loving_bank(resp, 20, 0)
    else:
      resp[KEY.STATUS] = STATUS.ERROR

    self.write(json_encode(resp))


  def get(self):
    self.render("signup.html")



class GetIdenCodeHandler(tornado.web.RequestHandler):
  def post(self):
    resp = {}
    resp[KEY.STATUS] = 500
    params = {}
    params = utils.decode_params(self.request)
    
    if KEY.EMAIL in params and KEY.ACCOUNT in params:
      isExist = db.isAccountHasExist(params)
      if isExist is not None:

        #如果这个账户不存在
        if isExist == 0:
          idencode = ''.join(random.sample(string.ascii_letters, 4))
          #emailt = email.PlainEmail()
          params[KEY.EMAIL] = params[KEY.EMAIL].replace("%40", '@')
          if sendEmail.sendEmail([params[KEY.EMAIL]], "新用户注册", "您的验证码为：" + idencode) == 200:
            md5_encode = hashlib.md5()
            md5_encode.update(params[KEY.ACCOUNT] + idencode + "?" + params[KEY.EMAIL])
            idencode = md5_encode.hexdigest()
            resp[KEY.STATUS] = 200
            resp["secret"] = idencode
        else:
          resp[KEY.STATUS] = 400

    self.write(json_encode(resp))