#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Get_User_Information_Handler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		user_info = db.get_user_information(params)
		if user_info is None:
			resp[KEY.STATUS] = STATUS.ERROR
		else:
			user_info[KEY.SUPPORT_NUMBER] = len(db.get_join_event_list({KEY.ID: user_info[KEY.ID]}))
			user_info[KEY.LOVE_COIN] = db.get_user_loving_bank({KEY.USER_ID: user_info[KEY.ID]})
			user_info[KEY.MEDICINE_TAKEN] = ""
			user_info[KEY.ANAPHYLAXIS] = ""
			user_info[KEY.MEDICAL_HISTORY] = ""
			health_record = db.get_health_record(user_info[KEY.ID])
			if health_record is not None:
				user_info[KEY.MEDICINE_TAKEN] = health_record[KEY.MEDICINE_TAKEN]
				user_info[KEY.ANAPHYLAXIS] = health_record[KEY.ANAPHYLAXIS]
				user_info[KEY.MEDICAL_HISTORY] = health_record[KEY.MEDICAL_HISTORY]
			resp.update(user_info)
			resp[KEY.STATUS] = STATUS.OK
    
		self.write(json_encode(resp))
