#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import json
from utils import utils
from utils import KEY
from database import db
from tornado.escape import json_encode

class GetEventNearbyHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.LONGITUDE not in params or KEY.LATITUDE not in params:
            self.write(json_encode(resp))
            return

        '''trans the term's type'''
        params[KEY.LONGITUDE] = float(params[KEY.LONGITUDE])
        params[KEY.LATITUDE] = float(params[KEY.LATITUDE])
        params[KEY.STATE] = 0
        params[KEY.TYPE] = -1
        event_id_list = db.get_nearby_event_by_location(params)
        if event_id_list is not None:
            event_list = []
            for item in event_id_list:
                event_info = db.get_event_information({KEY.EVENT_ID: item})
                if event_info is not None:
                    event_temp = {}
                    event_temp[KEY.EVENT_ID] = event_info[KEY.EVENT_ID]
                    event_temp[KEY.TYPE] = event_info[KEY.TYPE]
                    event_temp[KEY.LONGITUDE] = event_info[KEY.LONGITUDE]
                    event_temp[KEY.LATITUDE] = event_info[KEY.LATITUDE]
                    event_list.append(event_temp)
            resp[KEY.STATUS] = 200
            resp[KEY.INFO] = event_list

        self.write(json_encode(resp))
