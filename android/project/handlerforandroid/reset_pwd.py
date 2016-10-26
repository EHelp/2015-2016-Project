#!/usr/python
import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler

from utils import utils
from utils import KEY
from utils import STATUS
from database import db
from utils import Session

class Modify_Password_Handler(base_handler.BaseHandler):
    def post(self):
        params = utils.decode_params(self.request)
        resp = {}
        if KEY.PHONE in params and KEY.PASSWORD in params and KEY.TEMP_ID in params:
            if Session.Session.exists(params):
                if db.android_modify_password(params):
                    resp[KEY.STATUS] = 200
                else:
                    resp[KEY.STATUS] = 500
            else:
                resp[KEY.STATUS] = 500
        else:
            resp[KEY.STATUS] = 500

        self.write(json_encode(resp))
