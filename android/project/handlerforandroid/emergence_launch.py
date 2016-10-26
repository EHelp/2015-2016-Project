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
from database import dblove

title = '求救信息'
stitle = '紧急联系人求救'
scontent = '您的紧急联系人发出了求救信号！'
content = '您的附近有人发出了求救信息！'
content1 = '您发出了求救信息！'
header = 'ehelp_'
style = xinge.Style(0, 1, 1, 1, 1)
style1 = xinge.Style(0, 0, 1, 1, 1)
action = 'com.ehelp.ehelp.square.HelpMsgDetailActivity'

class EmergenceLaunchHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        resp = {KEY.STATUS: 500}
        params = utils.decode_params(self.request)
        if KEY.ID not in params or KEY.TYPE not in params or KEY.LONGITUDE not in params or KEY.LATITUDE not in params:
            self.write(json_encode(resp))
            return
        
        '''trans the term's type'''
        params[KEY.ID] = int(params[KEY.ID])
        params[KEY.LATITUDE] = float(params[KEY.LATITUDE])
        params[KEY.LONGITUDE] = float(params[KEY.LONGITUDE])
        params[KEY.TYPE] = int(params[KEY.TYPE])


        params[KEY.LOVE_COIN] = dblove.set_emergence_event_default_lovecoin()
        

        '''add emergent event'''
        flag = db.add_event(params)
        if flag > 0:
            resp[KEY.STATUS] = 200
            resp[KEY.EVENT_ID] = flag
            '''put message to the people nearby'''
            user_list = db.get_nearby_people(params)
            '''get the emergent contact'''
            relation_list = db.get_static_relation({KEY.ID: params[KEY.ID]})
            emergent_list = []
            for item in relation_list:
                user_infom = db.get_user_information({KEY.ID: item[KEY.ID]})
                emergent_list.append(user_infom[KEY.NICKNAME])

            people_nearby_sum = 0
            launcher_info = db.get_user_information({KEY.ID: params[KEY.ID]})
            if user_list.count(launcher_info[KEY.NICKNAME]) > 0:
                user_list.remove(launcher_info[KEY.NICKNAME])
                launcher_info = utils.trans_unicode_to_utf(launcher_info)
                mess = sendHelp.buildMessage(type=1, title=title, content=content1, style=style1)
                sendHelp.sendEhelp(header + launcher_info[KEY.NICKNAME], mess)

            for item in user_list:
                if emergent_list.count(item) > 0:
                    continue

                item = item.encode('UTF-8')
                mess = sendHelp.buildMessage(type=1, title=title, content=content, style=style, action=action, custom={KEY.EVENT_ID: flag})    
                sendHelp.sendEhelp(header + item, mess)
                people_nearby_sum += 1

            '''send notification to their contact'''
            for item in emergent_list:
                item = item.encode('UTF-8')
                mess = sendHelp.buildMessage(type=1, title=stitle, content=scontent, style=style, action=action, custom={KEY.EVENT_ID: flag})    
                sendHelp.sendEhelp(header + item, mess)
            
            '''
               here we can enhance it, if the people_nearby_sum = 0, we can change the range and send the message
            '''

            '''
               here we can improve it, meanwhile, send message to the emergent contact.
            '''

        self.write(json_encode(resp))
