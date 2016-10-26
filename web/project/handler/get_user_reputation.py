#!/usr/python
#coding:utf-8
import tornado
from tornado.web import RequestHandler
from handler import base_handler
from utils import KEY
from database import db


class Get_Reputation(base_handler.BaseHandler):

    @tornado.web.authenticated
    def get(self):

        id = self.get_secure_cookie("id")
        data = {}
        data[KEY.ID] = int(id)
        user_Info = db.get_user_information(data)
        if (user_Info is not None):
            reputation = user_Info[KEY.REPUTATION]
            avatar = user_Info[KEY.AVATAR] if user_Info[KEY.AVATAR] else "default.png"
            self.render("reputation.html", reputation = reputation, avatar = avatar)
        else:
            self.write("error")