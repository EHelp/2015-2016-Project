#!/usr/python
# -*- coding: utf-8 -*-

import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode

from utils import utils
from utils import KEY
from database import db
from database import dblove

class get_system_lovecoin_information(tornado.web.RequestHandler):
	"""计算爱心币数据的接口函数，获取4个数据
		1. 当天爱心币流通数量
		2. 当天爱心币流通次数
		3. 当天涉及爱心币交易的用户数量
		4. 最近一周爱心币流通数量情况
	"""
	def post(self):
		
		resp = {}

		resp[KEY.CURRENY_OF_LOVECOIN] = dblove.calculate_currency()
		resp[KEY.CIRCULATION] = dblove.calculate_circulation_times()
		resp[KEY.USER_INVOLVE_COIN] = dblove.calclulate_user_involve_lovecoin()
		resp[KEY.CURRENY_WEEKLY] = dblove.calculate_currency_weekly()

		if resp[KEY.CURRENY_OF_LOVECOIN] is None or resp[KEY.CIRCULATION] is None or \
			resp[KEY.USER_INVOLVE_COIN] is None or resp[KEY.CURRENY_WEEKLY] is None:
			resp[KEY.STATUS] = 500
		else:
			resp[KEY.STATUS] = 200

		self.write(json_encode(resp))



