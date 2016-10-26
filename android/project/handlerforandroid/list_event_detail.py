#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import json
from utils import utils
from utils import KEY
from database import db
from tornado.escape import json_encode

class ListEventDetailHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.EVENT_ID not in params:
            self.write(json_encode(resp))
            return

        '''trans the term's type'''
        params[KEY.EVENT_ID] = int(params[KEY.EVENT_ID])
        event_info = db.get_event_information(params)
        if event_info is not None:
            resp[KEY.STATUS] = 200
            resp[KEY.LAUNCHER_ID] = event_info[KEY.LAUNCHER_ID]
            resp[KEY.TIME] = event_info[KEY.TIME]
            resp[KEY.TYPE] = int(event_info[KEY.TYPE])
            resp[KEY.SUPPORT_NUMBER] = event_info[KEY.SUPPORT_NUMBER]
            resp[KEY.DEMAND_NUMBER] = event_info[KEY.DEMAND_NUMBER]
            resp[KEY.LONGITUDE] = event_info[KEY.LONGITUDE]
            resp[KEY.LATITUDE] = event_info[KEY.LATITUDE]
            resp[KEY.LAUNCHER_NAME] = event_info[KEY.LAUNCHER]
            user = db.get_user_information({KEY.ID: resp[KEY.LAUNCHER_ID]})
            if user is not None:
                resp[KEY.CONTACT] = user[KEY.PHONE]
                resp[KEY.GENDER] = user[KEY.GENDER]
                resp[KEY.REPUTATION] = user[KEY.REPUTATION]

            '''if this event is help'''
            if resp[KEY.TYPE] == 1:
                resp[KEY.TITLE] = event_info[KEY.TITLE]
                resp[KEY.CONTENT] = event_info[KEY.CONTENT]
                resp[KEY.LOVE_COIN] = int(event_info[KEY.LOVE_COIN])

        self.write(json_encode(resp))
