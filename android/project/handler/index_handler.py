#!/usr/python
import tornado
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
  def get(self):
    self.render("index.html")
