#!/usr/python
import tornado
from tornado.web import RequestHandler

class HelpHandler(RequestHandler):
  def get(self):
    self.render("help.html")
