#!/usr/python
import tornado
from tornado.web import RequestHandler

class CultureHandler(RequestHandler):
  def get(self):
    self.render("culture.html")
