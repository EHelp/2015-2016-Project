#!/usr/bin/env python
#-*- coding: utf-8 -*-

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db
from utils import xinge
from utils import sendHelp

title = '提示信息'
content = '您所参与的帮助事件已经结束了，谢谢您的参与！'
header = 'ehelp_'
action = 'com.ehelp.ehelp.square.AskMsgDetailActivity'
style = xinge.Style(0, 0, 0, 0, 9)

class AdoptAnswerHandler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		if KEY.ID not in params or KEY.EVENT_ID not in params or KEY.ANSWER_ID not in params:
			self.write(json_encode(resp))
			return

		resp = {}
		params[KEY.IS_ADOPTED] = 1
		result = db.update_answer(params)
		if result is True:
			resp[KEY.STATUS] = STATUS.OK
			
			event_info = db.get_event_information({KEY.EVENT_ID: params[KEY.EVENT_ID]})
			user_info = db.get_user_information({KEY.ID: event_info[KEY.LAUNCHER_ID]})
			answer_info = db.get_answer_info({KEY.ANSWER_ID: params[KEY.ANSWER_ID]})
			user_info = utils.trans_unicode_to_utf(user_info)
			event_info = utils.trans_unicode_to_utf(event_info)
			answer_info = utils.trans_unicode_to_utf(answer_info)

			is_like = 0
			if db.is_user_like_event({KEY.ID: event_info[KEY.LAUNCHER_ID], KEY.EVENT_ID: params[KEY.EVENT_ID]}):
				is_like = 1

			custom = {KEY.EVENT_ID: params[KEY.EVENT_ID], KEY.NICKNAME: user_info[KEY.NICKNAME], KEY.LAUNCHER: answer_info[KEY.AUTHOR].encode('UTF-8'), \
			KEY.TIME: event_info[KEY.TIME], KEY.TITLE: event_info[KEY.TITLE], \
			KEY.CONTENT: event_info[KEY.CONTENT], KEY.LOVE_COIN: event_info[KEY.LOVE_COIN], KEY.FOLLOW_NUMBER: event_info[KEY.FOLLOW_NUMBER],\
			KEY.SUPPORT_NUMBER: event_info[KEY.SUPPORT_NUMBER], KEY.IS_LIKE: is_like}
			custom['message-type'] = 7
			mess = sendHelp.buildMessage(type=1, title=title, content=content, style=style, action=action, custom=custom)
			sendHelp.sendEhelp(header + answer_info[KEY.AUTHOR].encode('UTF-8'), mess)
			
			mess = sendHelp.buildMessage(custom=custom)
			sendHelp.sendEhelp(header + answer_info[KEY.AUTHOR].encode('UTF-8'), mess)

		else:
			resp[KEY.STATUS] = STATUS.ERROR
		
		self.write(json_encode(resp))