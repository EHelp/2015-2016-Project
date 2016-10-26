#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode

from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class GetUserInfoFromPhoneHandler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		result = db.get_id_by_phone(params)
		if result is not None:
			resp[KEY.STATUS] = STATUS.OK
			user_info = db.get_user_information({KEY.ID: result})
			resp[KEY.USER_ID] = result
			resp[KEY.NICKNAME] = user_info[KEY.NICKNAME]
			resp[KEY.GENDER] = user_info[KEY.GENDER]
			resp[KEY.OCCUPATION] = user_info[KEY.OCCUPATION]
			resp[KEY.LOCATION] = user_info[KEY.LOCATION]
			resp[KEY.REPUTATION] = user_info[KEY.REPUTATION]
			resp[KEY.IS_VERIFY] = user_info[KEY.IS_VERIFY]
		else:
			resp[KEY.STATUS] = STATUS.ERROR
		
		self.write(json_encode(resp))