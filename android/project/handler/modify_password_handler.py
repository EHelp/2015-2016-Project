#!/usr/python
import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler

from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Modify_Password_Handler(base_handler.BaseHandler):
    @tornado.web.authenticated
    def post(self):
        params = utils.decode_params(self.request)
      
        user_id = db.validate_password(params)

        resp = {}
        if user_id < 0:
            resp[KEY.STATUS] = 500
        else:    
            
            result = db.modify_password(params)
            if result > 0:
                resp[KEY.STATUS] = 200
                resp[KEY.ID] = user_id
                resp[KEY.ACCOUNT] = params[KEY.ACCOUNT]
            else:
                resp[KEY.STATUS] = 400    
   
        self.write(json_encode(resp))
    @tornado.web.authenticated
    def get(self):
      self.render("modifyUserInfo.html")

    

