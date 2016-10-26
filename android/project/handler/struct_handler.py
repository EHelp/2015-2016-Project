#!/usr/python
import tornado
from tornado.web import RequestHandler

class StructureHandler(RequestHandler):
  def get(self):
    self.render("function.html")
