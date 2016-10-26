#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Delete_Answer_Handler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		params[KEY.VALID] = 0
		result = db.update_answer(params)
		if result is True:
			resp[KEY.STATUS] = STATUS.OK
		else:
			resp[KEY.STATUS] = STATUS.ERROR
		
		self.write(json_encode(resp))