#!/usr/python
# -*- coding: utf-8 -*-

import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode

from utils import utils
from utils import KEY
from database import db
from database import dblove

class maintain_system(tornado.web.RequestHandler):
	"""docstring for maintain_system"""
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}

		if KEY.TYPE not in params:
			resp[KEY.STATUS] = 500
			self.write(json_encode(resp))

		if params[KEY.TYPE] == 0:
			if KEY.DEFAULT_COIN not in params or KEY.REWARD_FACTOR not in params:
				resp[KEY.STATUS] = 500
				self.write(json_encode(resp))
			else:
				dblove.modify_reward_factor(params[KEY.REWARD_FACTOR])
				dblove.modify_default_coin(params[KEY.DEFAULT_COIN])
				resp[KEY.STATUS] = 200

		else:
			if KEY.REWARD_FACTOR not in params or KEY.LOVE_COIN not in params:
				resp[KEY.STATUS] = 500
				self.write(json_encode(resp))
			else:
				dblove.modify_reward_factor(params[KEY.REWARD_FACTOR])
				if dblove.welfare_coin(params[KEY.LOVE_COIN]) is not None:
					resp[KEY.STATUS] = 200
				else:
					resp[KEY.STATUS] = 500

		self.write(json_encode(resp))

