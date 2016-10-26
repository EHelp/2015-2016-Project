#!/usr/python
import tornado
from utils import sendEmail
from utils import KEY
from utils import utils
from tornado.web import RequestHandler
from tornado.escape import json_encode
from utils import STATUS

class FeedbackHandler(RequestHandler):
  def post(self):
  	params = utils.decode_params(self.request)
  	resp = {}
  	resp[KEY.STATUS] = 500
  	if KEY.TITLE in params and KEY.CONTENT in params:
  		content_t = params[KEY.TITLE] + "---" + params[KEY.CONTENT]
		if sendEmail.sendEmail([KEY.EMAIL_BOSS], "User-Feedback", content_t) == 200:
			resp[KEY.STATUS] = 200

  	self.write(json_encode(resp))
