#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import json
from utils import utils
from utils import KEY
from database import db
from tornado.escape import json_encode

class GetHelperNumHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.EVENT_ID not in params:
            self.write(json_encode(resp))
            return

        '''trans the term's type'''
        params[KEY.EVENT_ID] = int(params[KEY.EVENT_ID])
        supporter_ids = db.list_support_relation(params)
        if supporter_ids is not None:
            resp[KEY.STATUS] = 200
            resp[KEY.NUM] = len(supporter_ids)

        self.write(json_encode(resp))
