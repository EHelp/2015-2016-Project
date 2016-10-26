#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Manage_Event_Like_Handler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		result = db.manage_event_like(params)
		if result is True:
			resp[KEY.STATUS] = STATUS.OK
		else:
			resp[KEY.STATUS] = STATUS.ERROR
		
		self.write(json_encode(resp))