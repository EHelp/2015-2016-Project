#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Get_Answers_Handler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		get_answers_method = db.get_answer_id_list
		resp[KEY.ANSWER_LIST] = db.get_answers(params, get_answers_method, 30)
		if resp[KEY.ANSWER_LIST] is None:
			resp[KEY.STATUS] = STATUS.ERROR
		else:
			resp[KEY.STATUS] = STATUS.OK
		
		self.write(json_encode(resp))