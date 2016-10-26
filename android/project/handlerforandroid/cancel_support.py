#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import json
from utils import utils
from utils import KEY
from database import db
from tornado.escape import json_encode
from utils import sendHelp
from utils import xinge

title = '提示信息'
content = '此时有爱心人士由于某些原因取消对您的帮助'
header = 'ehelp_'

class CancelSupportHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.ID not in params or KEY.LAUNCHER_ID not in params or KEY.TYPE not in params or KEY.EVENT_ID not in params:
            self.write(json_encode(resp))
            return

        '''trans the term's type'''
        params[KEY.EVENT_ID] = int(params[KEY.EVENT_ID])
        params[KEY.ID] = int(params[KEY.ID])
        params[KEY.LAUNCHER_ID] = int(params[KEY.LAUNCHER_ID])
        params[KEY.TYPE] = int(params[KEY.TYPE])
        
        flag = db.remove_support_relation(params)
        if flag:
            '''when the event is help or emergence, it is necessary to notify the users'''
            user_info = db.get_user_information({KEY.ID: params[KEY.LAUNCHER_ID]})
            user_info = utils.trans_unicode_to_utf(user_info)
            if user_info is not None:
                if params[KEY.TYPE] == 2:
                    mess = sendHelp.buildMessage(type=1, title=title, content=content, style=xinge.Style(0, 0, 0, 1, 3))
                    sendHelp.sendEhelp(header + user_info[KEY.NICKNAME], mess)
                if params[KEY.TYPE] == 1:
                    mess = sendHelp.buildMessage(type=1, title=title, content=content, style=xinge.Style(0, 0, 0, 0, 6))
                    sendHelp.sendEhelp(header + user_info[KEY.NICKNAME], mess)
            resp[KEY.STATUS] = 200

        self.write(json_encode(resp))
