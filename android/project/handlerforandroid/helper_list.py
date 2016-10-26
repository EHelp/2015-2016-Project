#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import json
from utils import utils
from utils import KEY
from database import db
from tornado.escape import json_encode

class HelperListHandler(tornado.web.RequestHandler):
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
        print supporter_ids
        if supporter_ids is not None:
            supporter_info = []
            for item in supporter_ids:
                user_info = db.get_user_information({KEY.ID: item})
                if user_info is not None:
                    user = {}
                    user[KEY.ID] = user_info[KEY.ID]
                    user[KEY.NICKNAME] = user_info[KEY.NICKNAME]
                    user[KEY.NAME] = user_info[KEY.NAME]
                    user[KEY.OCCUPATION] = user_info[KEY.OCCUPATION]
                    user[KEY.REPUTATION] = user_info[KEY.REPUTATION]
                    user[KEY.LOCATION] = user_info[KEY.LOCATION]
                    user[KEY.IS_VERIFY] = user_info[KEY.IS_VERIFY]
                    user[KEY.GENDER] = user_info[KEY.GENDER]
                    supporter_info.append(user)
            resp[KEY.STATUS] = 200
            resp[KEY.INFO] = supporter_info

        self.write(json_encode(resp))
