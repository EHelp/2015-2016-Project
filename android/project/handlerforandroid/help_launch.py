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

title = '求助'
content = '您的附近有人发出了求助信息'
header = 'ehelp_'
style = xinge.Style(0, 0, 0, 0, 4)
action = 'com.ehelp.ehelp.square.HelpMsgDetailActivity'


class HelpLaunchHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.ID not in params or KEY.TYPE not in params:
            self.write(json_encode(resp))
            return
        params[KEY.TYPE] = int(params[KEY.TYPE])
        if KEY.TITLE not in params or KEY.CONTENT not in params or KEY.LOVE_COIN not in params:
            self.write(json_encode(resp))
            return
        if params[KEY.TYPE] == 1:
            if KEY.LONGITUDE not in params or KEY.LATITUDE not in params or KEY.DEMAND_NUMBER not in params:
                self.write(json_encode(resp))
                return
            else:
                params[KEY.DEMAND_NUMBER] = int(params[KEY.DEMAND_NUMBER])
        
        '''trans the term's type'''
        params[KEY.ID] = int(params[KEY.ID])
        params[KEY.LOVE_COIN] = int(params[KEY.LOVE_COIN])
        params[KEY.LATITUDE] = float(params[KEY.LATITUDE])
        params[KEY.LONGITUDE] = float(params[KEY.LONGITUDE])
        '''add event'''
        flag = db.add_event(params)
        if flag > 0:
            resp[KEY.STATUS] = 200
            resp[KEY.EVENT_ID] = flag

            '''spread the message to the people nearby'''
            '''if the event is help, then spread the notification'''
            user_list = db.get_nearby_people(params)
            people_nearby_sum = 0
            for item in user_list:
                item = item.encode('UTF-8')
                if params[KEY.TYPE] == 1:
                    mess = sendHelp.buildMessage(type=1, title=title, content=content, style=style, action=action, custom={KEY.EVENT_ID: flag, KEY.TYPE: 1})
                    sendHelp.sendEhelp(header + item, mess)
                if params[KEY.TYPE] == 0:
                    mess = sendHelp.buildMessage(custom={'message-type': 1})
                    sendHelp.sendEhelp(header + item, mess)
                people_nearby_sum += 1

        self.write(json_encode(resp))
