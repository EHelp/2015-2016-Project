#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
import json

from utils import utils
from utils import KEY
from database import db
from utils import sendHelp
from utils import xinge
from tornado.escape import json_encode


title = '提示信息'
content = '您所参与的帮助事件已经结束了，谢谢您的参与！'
header = 'ehelp_'
action = 'com.ehelp.ehelp.square.HelpEventFinishActivity'
style = xinge.Style(0, 0, 1, 0, 8)

class EmergenceCompleteHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.ID not in params or KEY.EVENT_ID not in params:
            self.write(json_encode(resp))
            return
        
        '''trans the term's type'''
        params[KEY.ID] = int(params[KEY.ID])
        params[KEY.EVENT_ID] = int(params[KEY.EVENT_ID])

        event_info = db.get_event_information(params)
        if event_info is not None:
            if event_info[KEY.LAUNCHER_ID] == params[KEY.ID]:
                resp[KEY.STATUS] = 200
            
            
            params[KEY.STATE] = 2
            if not db.update_event(params):
                resp[KEY.STATUS] = 500
            else:
                '''send notification to the people who is coming to help him'''
                supporter_ids = db.list_support_relation({KEY.EVENT_ID: params[KEY.EVENT_ID]})
                if supporter_ids is not None:
                    for item in supporter_ids:
                        user_info = db.get_user_information({KEY.ID: item})
                        user_info = utils.trans_unicode_to_utf(user_info)
                        if user_info is not None:
                            mess = sendHelp.buildMessage(type=1, title=title, content=content, style=style, custom={KEY.EVENT_ID: params[KEY.EVENT_ID]})
                        
                            sendHelp.sendEhelp(header + user_info[KEY.NICKNAME], mess)
                            '''send tongtou message to android'''
                            mess = sendHelp.buildMessage(custom={'message-type': 3})
                            sendHelp.sendEhelp(header + user_info[KEY.NICKNAME], mess)

        self.write(json_encode(resp))
