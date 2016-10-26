#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import json
from utils import sendHelp
from utils import utils
from utils import KEY
from utils import VALUE
from database import db
from tornado.escape import json_encode

class EvaluateHelpHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.ID not in params or KEY.EVENT_ID not in params or KEY.USER_ID not in params or KEY.VALUE not in params:
            self.write(json_encode(resp))
            return

        '''trans the term's type'''
        params[KEY.ID] = int(params[KEY.ID])
        params[KEY.EVENT_ID] = int(params[KEY.EVENT_ID])
        params[KEY.USER_ID] = int(params[KEY.USER_ID])
        params[KEY.VALUE] = float(params[KEY.VALUE])


        event_info = db.get_event_information({KEY.EVENT_ID: params[KEY.EVENT_ID]})
        
        flag = db.evaluate_user(params)
        if flag:
            '''we can import here, use some algorithm to incease the helper's reputation'''
            user = db.get_user_information({KEY.ID: params[KEY.USER_ID]})
            if user is not None:
                reputation = user[KEY.REPUTATION]
                params[KEY.VALUE] = reputation*(1 - VALUE.RATE) + VALUE.RATE*params[KEY.VALUE]
                if db.update_user({KEY.ID: params[KEY.USER_ID], KEY.REPUTATION: params[KEY.VALUE]}):
                    resp[KEY.STATUS] = 200
                '''
                update_info = {}
                update_info[KEY.ID] = params[KEY.USER_ID]
                update_info[KEY.OPERATION] = 0
                update_info[KEY.LOVE_COIN] = event_info[KEY.LOVE_COIN]
                update_info[KEY.SCORE] = 5

                if db.update_loving_bank(update_info):
                    if resp[KEY.STATUS] == 200:
                        resp[KEY.STATUS] = 200
                '''


        self.write(json_encode(resp))
