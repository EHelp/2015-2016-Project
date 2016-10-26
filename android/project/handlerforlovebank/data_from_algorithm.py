#!/usr/user_earn_coin()
# -*- coding: utf-8 -*-

import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler

from utils import utils
from utils import KEY
from utils import STATUS
from database import db
from database import dblove

class data_from_algorithm(tornado.web.RequestHandler):
	"""docstring for data_from_algorithm"""
	def post(self):
		
		resp = {}

		resp[KEY.LOVE_COIN] = dblove.calcultae_system_lovecoin()
		resp[KEY.CONSUME_COIN] = float(dblove.user_consume_coin())
		resp[KEY.EARN_COIN] = float(dblove.user_earn_coin())
		resp[KEY.EXCHANGE_SERVICE] = float(dblove.user_exchange_coin())
		resp[KEY.PERCENT] = float(dblove.algorithm_analysis())
		
		if resp[KEY.LOVE_COIN] is None or resp[KEY.CONSUME_COIN] is None or \
			resp[KEY.EARN_COIN] is None or resp[KEY.EXCHANGE_SERVICE] is None or resp[KEY.PERCENT] is None:
			resp[KEY.STATUS] = 500
		else:
			resp[KEY.STATUS] = 200

		self.write(json_encode(resp))