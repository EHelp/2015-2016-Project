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

class ModifyPhoneHandler(base_handler.BaseHandler):
    def post(self):
        params = utils.decode_params(self.request)
        resp = {}
        if KEY.PHONE in params and KEY.SMSCODE in params and KEY.TEMP_ID in params and KEY.ID in params:
            if Session.Session.confirm_by_flag(params):
                if db.update_user(params):
                    resp[KEY.STATUS] = 200
                else:
                    resp[KEY.STATUS] = 300;
            else:
                resp[KEY.STATUS] = 400
        else:
            resp[KEY.STATUS] = 500

        self.write(json_encode(resp))
