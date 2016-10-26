#!/usr/python
# -*- coding: utf-8 -*-


from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

#注意这个是修改使用者的信息，就是对使用者的所有可能属性进行修改
#而不仅仅是名字
class Modify_User_Information_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)
    result = db.update_user(params)
    resp = {}
    if result:
      resp[KEY.STATUS] = STATUS.OK
      resp[KEY.ID] = params[KEY.ID]
    else:
      resp[KEY.STATUS] = STATUS.ERROR    
   
    self.write(json_encode(resp))

    

