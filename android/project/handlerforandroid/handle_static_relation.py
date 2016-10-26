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


class Handle_Static_Relation_Handler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		
		result = db.handle_static_relation(params)
		if result is True:
			resp[KEY.STATUS] = STATUS.OK
			user_info = db.get_user_information({KEY.ID: params[KEY.ID]})
			user_acc = db.get_user_information({KEY.ID: params[KEY.USER_ID]})
			user_acc = utils.trans_unicode_to_utf(user_acc)
			custom = {'message-type': 5, KEY.STATUS: params[KEY.OPERATION], KEY.NICKNAME: user_info[KEY.NICKNAME]}
			custom = utils.trans_unicode_to_utf(custom)
			mess = sendHelp.buildMessage(custom=custom)
			sendHelp.sendEhelp(KEY.HEADER + user_acc[KEY.NICKNAME], mess)
		else:
			resp[KEY.STATUS] = STATUS.ERROR
    
		self.write(json_encode(resp))