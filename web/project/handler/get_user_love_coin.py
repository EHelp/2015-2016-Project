#!/usr/python
#coding:utf-8
import tornado
from tornado.web import RequestHandler
from handler import base_handler
from utils import KEY
from database import db


class Get_Love_Coin(base_handler.BaseHandler):

    @tornado.web.authenticated
    def get(self):

        id = self.get_secure_cookie("id")
        data = {}
        data[KEY.USER_ID] = int(id)
        bank_Info = db.get_user_loving_bank(data)
        data[KEY.ID] = int(id)
        user_Info = db.get_user_information(data)
        avatar = user_Info[KEY.AVATAR] if user_Info[KEY.AVATAR] else "default.png"
        if (bank_Info is not None):
            love_coin = bank_Info[KEY.LOVE_COIN]
            self.render("love_coin.html", love_coin = love_coin, avatar = avatar)
        else:
            self.write("error")