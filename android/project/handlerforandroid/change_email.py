#!/usr/python
import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler

from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class ModifyEmailHandler(base_handler.BaseHandler):
    def post(self):
        params = utils.decode_params(self.request)
        resp = {}
        if db.update_user(params):
            resp[KEY.STATUS] = 200
        else:
            resp[KEY.STATUS] = 500

        self.write(json_encode(resp))
