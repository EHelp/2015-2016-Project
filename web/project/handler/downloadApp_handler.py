#!/usr/python
#coding:utf-8
import tornado
import string
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler
import os

from utils import downloadUtils


class DownloadApp_Handler(base_handler.BaseHandler):

    def get(self):

    	nowpath = os.path.dirname(__file__).replace("handler", "files")
    	filename = os.path.join(nowpath, "app-release.apk")
        downloadUtils.downloadUtils(self, filename, "yizhu-app-release.apk")