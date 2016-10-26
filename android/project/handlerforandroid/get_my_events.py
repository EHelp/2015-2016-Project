#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Get_My_Events_Handler(RequestHandler):
	def post(self):
		params = utils.decode_params(self.request)
		resp = {}
		get_events_method = None
		if KEY.OPERATION in params and params[KEY.OPERATION] == 0:
			get_events_method = db.get_launch_event_list
		elif KEY.OPERATION in params and params[KEY.OPERATION] == 1:
			get_events_method = db.get_join_event_list
		elif KEY.OPERATION in params and params[KEY.OPERATION] == 2:
			params[KEY.TYPE] = 1 # help	
			params[KEY.STATE] = 0 # ing
			get_events_method = db.get_nearby_event_by_location
		elif KEY.OPERATION in params and params[KEY.OPERATION] == 3:
			params[KEY.TYPE] = 0 # question
			params[KEY.STATE] = 0 # ing
			get_events_method = db.get_all_events
		if get_events_method is None:
			resp[KEY.STATUS] = STATUS.ERROR
		else:
			resp[KEY.STATUS] = STATUS.OK
			resp[KEY.EVENT_LIST] = db.get_events(params, get_events_method, 30)
    
		self.write(json_encode(resp))