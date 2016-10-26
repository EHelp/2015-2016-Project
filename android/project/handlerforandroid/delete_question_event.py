#!/usr/python
#-*- coding: utf-8 -*-
from tornado.web import RequestHandler
from tornado.escape import json_encode

from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Delete_Question_event_Handler(RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: STATUS.ERROR}
        params = utils.decode_params(self.request)
        if KEY.ID not in params or KEY.EVENT_ID not in params:
            self.write(json_encode(resp))
            return
        params[KEY.ID] = int(params[KEY.ID])
        params[KEY.EVENT_ID] = int(params[KEY.EVENT_ID])
        result = db.delete_question_event(params)
        if result is True:
            resp[KEY.STATUS] = STATUS.OK
        else:
            resp[KEY.STATUS] = STATUS.ERROR
        self.write(json_encode(resp))