#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import json
from utils import utils
from utils import KEY
from database import db
from tornado.escape import json_encode

class GetRecipientInfoHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.EVENT_ID not in params:
            self.write(json_encode(resp))
            return

        '''trans the term's type'''
        params[KEY.EVENT_ID] = int(params[KEY.EVENT_ID])
        launcher_info = db.get_event_information(params)
        if launcher_info is not None:
            user_info = db.get_user_information({KEY.ID: launcher_info[KEY.LAUNCHER_ID]})
            if user_info is not None:
                resp[KEY.STATUS] = 200
                resp[KEY.ID] = user_info[KEY.ID]
                resp[KEY.NICKNAME] = user_info[KEY.NICKNAME]
                resp[KEY.NAME] = user_info[KEY.NAME]
                resp[KEY.AGE] = user_info[KEY.AGE]
                resp[KEY.GENDER] = user_info[KEY.GENDER]
                resp[KEY.PHONE] = user_info[KEY.PHONE]
                resp[KEY.OCCUPATION] = user_info[KEY.OCCUPATION]
                resp[KEY.REPUTATION] = user_info[KEY.REPUTATION]
                resp[KEY.LOCATION] = user_info[KEY.LOCATION]
                resp[KEY.IS_VERIFY] = user_info[KEY.IS_VERIFY]

        self.write(json_encode(resp))
