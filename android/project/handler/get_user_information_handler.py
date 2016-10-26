#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Get_User_Information_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)
    resp = {}
    user_info = db.get_user_information(params)
    if user_info is None:
      resp[KEY.STATUS] = STATUS.ERROR
    else:
      follow = {}
      follow[KEY.ID] = user_info[KEY.ID]
      follow[KEY.STATE] = 0
      user_info[KEY.FOLLOW] = len(db.query_follow(follow))
      follow[KEY.STATE] = 1
      user_info[KEY.FOLLOWER] = len(db.query_follow(follow))
      resp.update(user_info)
      resp[KEY.STATUS] = STATUS.OK
    
    self.write(json_encode(resp))

    

