#!/usr/python
#coding:utf-8

import tornado
from tornado.web import RequestHandler
from handler import base_handler

class showDownloadPage(base_handler.BaseHandler):

    def get(self):

    	self.render("downloadApp.html")