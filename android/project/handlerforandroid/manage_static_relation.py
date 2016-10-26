#!/usr/bin/env python
#-*- coding: utf-8 -*-
from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from utils import xinge
from utils import sendHelp
from database import db

header = 'ehelp_'

class Manage_Static_Relation_Handler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		result = True
		if KEY.OPERATION in params and params[KEY.OPERATION] == 0:
			result = db.remove_static_relation(params)
			update_account = {}
			update_account[KEY.ID] = params[KEY.ID]
			update_account[KEY.USER_ID] = params[KEY.USER_ID]
			update_account[KEY.TYPE] = 0
			
			if(db.update_family_love_coin(update_account)):
				result = True
			else:
				result = False

		elif KEY.OPERATION in params and params[KEY.OPERATION] == 1:
			result = db.add_static_relation(params)
			'''send the tongtou message to tell the user'''
			user_info = db.get_user_information({KEY.ID: params[KEY.ID]})
			user_acc = db.get_user_information({KEY.ID: params[KEY.USER_ID]})
			
			user_info = utils.trans_unicode_to_utf(user_info)
			user_acc = utils.trans_unicode_to_utf(user_acc)

			mess_package = {KEY.USER_ID: user_info[KEY.ID], KEY.NICKNAME: user_info[KEY.NICKNAME],\
			 KEY.REALNAME: user_info[KEY.NAME], KEY.LOCATION: user_info[KEY.LOCATION], KEY.OCCUPATION: user_info[KEY.OCCUPATION]}
			mess_package[KEY.TYPE] = params[KEY.TYPE]
			mess_package['message-type'] = 4
			if KEY.CONTENT in params:
				mess_package[KEY.CONTENT] = params[KEY.CONTENT].encode('UTF-8')
			
			mess = sendHelp.buildMessage(custom=mess_package)
			sendHelp.sendEhelp(header + user_acc[KEY.NICKNAME], mess)

			update_account = {}
			update_account[KEY.ID] = params[KEY.ID]
			update_account[KEY.USER_ID] = params[KEY.USER_ID]
			update_account[KEY.TYPE] = 1
			if(db.update_family_love_coin(update_account)):
				result = True
			else:
				result = False

		else:
			result = False
		if result:
			resp[KEY.STATUS] = STATUS.OK
		else:
			resp[KEY.STATUS] = STATUS.ERROR

		self.write(json_encode(resp))
