#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Get_Static_Relation_Handler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		resp[KEY.USER_LIST] = db.query_follow(params)
		if resp[KEY.USER_LIST] == -1:
			resp[KEY.STATUS] = STATUS.ERROR
		else:
			resp[KEY.STATUS] = STATUS.OK
    
		self.write(json_encode(resp))

    

