#!/usr/python
import tornado
from tornado.web import RequestHandler
from utils import KEY
from utils import utils
from tornado.web import RequestHandler
from tornado.escape import json_encode
from utils import STATUS

class AboutusHandler(RequestHandler):
  def get(self):
    self.render("we.html")
  def post(self):
  	params = utils.decode_params(self.request)
  	resp = {}
  	resp[KEY.STATUS] = 500
  	if "title" in params and "content" in params and "contact" in params:
  		content_t = params["title"] + "---" + params["content"] + "---" + params["contact"]
  		emailt = email_req.PlainEmail()
  		if emailt.sendPlainEmail(KEY.EMAIL_TEST, "User-Feedback", content_t) == 200:
  			resp[KEY.STATUS] = 200

  	self.write(json_encode(resp))
   	
