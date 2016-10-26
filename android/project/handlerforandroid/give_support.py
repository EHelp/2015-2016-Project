#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import json
from utils import sendHelp
from utils import utils
from utils import KEY
from utils import xinge
from database import db
from tornado.escape import json_encode

title = '提示'
content = '此时有爱心人士正赶来帮助您'
header = 'ehelp_'

class GiveSupportHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.ID not in params or KEY.EVENT_ID not in params or KEY.LAUNCHER_ID not in params or KEY.TYPE not in params:
            self.write(json_encode(resp))
            return

        '''trans the term's type'''
        params[KEY.ID] = int(params[KEY.ID])
        params[KEY.EVENT_ID] = int(params[KEY.EVENT_ID])
        params[KEY.LAUNCHER_ID] = int(params[KEY.LAUNCHER_ID])
        params[KEY.TYPE] = int(params[KEY.TYPE])

        flag = db.add_support_relation(params)
        if flag >= 0:
            resp[KEY.STATUS] = 200
            '''send notification to supportee, someone is coming to help him'''
            launcher_info = db.get_user_information({KEY.ID: params[KEY.LAUNCHER_ID]})
            launcher_info = utils.trans_unicode_to_utf(launcher_info)
            if launcher_info is not None:
                if params[KEY.TYPE] == 2:
                    mess = sendHelp.buildMessage(type=1, title=title, content=content, style=xinge.Style(0, 0, 0, 1, 2))
                    sendHelp.sendEhelp(header + launcher_info[KEY.NICKNAME], mess)
                if params[KEY.TYPE] == 1:
                    mess = sendHelp.buildMessage(type=1, title=title, content=content, style=xinge.Style(0, 0, 0, 0, 5))
                    sendHelp.sendEhelp(header + launcher_info[KEY.NICKNAME], mess)


        self.write(json_encode(resp))
