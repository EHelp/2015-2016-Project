#!/usr/bin/env python
#-*- coding: utf-8 -*-
from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db
from utils import sendHelp
from utils import xinge

title = '社区广场'
content = '有人回复了您提出的问题'
header = 'ehelp_'
action = 'com.ehelp.ehelp.square.AskMsgDetailActivity'
style = xinge.Style(0, 0, 0, 0, 7)

class Add_Answer_Handler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		answer_id = db.add_answer(params)
		if answer_id == -1:
			resp[KEY.STATUS] = STATUS.ERROR
		else:
			resp[KEY.STATUS] = STATUS.OK
			event_info = db.get_event_information({KEY.EVENT_ID: params[KEY.EVENT_ID]})
			user_info = db.get_user_information({KEY.ID: event_info[KEY.LAUNCHER_ID]})
			helper_info = db.get_user_information({KEY.ID: params[KEY.ID]})
			user_info = utils.trans_unicode_to_utf(user_info)
			helper_info = utils.trans_unicode_to_utf(helper_info)
			event_info = utils.trans_unicode_to_utf(event_info)
			
			is_like = 0
			if db.is_user_like_event({KEY.ID: event_info[KEY.LAUNCHER_ID], KEY.EVENT_ID: params[KEY.EVENT_ID]}):
				is_like = 1

			custom = {KEY.EVENT_ID: params[KEY.EVENT_ID], KEY.NICKNAME: helper_info[KEY.NICKNAME], KEY.LAUNCHER: user_info[KEY.NICKNAME], KEY.TIME: event_info[KEY.TIME], KEY.TITLE: event_info[KEY.TITLE], \
			KEY.CONTENT: event_info[KEY.CONTENT], KEY.LOVE_COIN: event_info[KEY.LOVE_COIN], KEY.FOLLOW_NUMBER: event_info[KEY.FOLLOW_NUMBER],\
			KEY.SUPPORT_NUMBER: event_info[KEY.SUPPORT_NUMBER], KEY.IS_LIKE: is_like}
			custom['message-type'] = 5
			mess = sendHelp.buildMessage(type=1, title=title, content=content, style=style, action=action, custom=custom)
			sendHelp.sendEhelp(header + user_info[KEY.NICKNAME], mess)
			'''and send the tongyou message'''
			mess = sendHelp.buildMessage(custom=custom)
			sendHelp.sendEhelp(header + user_info[KEY.NICKNAME], mess)

		resp[KEY.ANSWER_ID] = answer_id
		self.write(json_encode(resp))
