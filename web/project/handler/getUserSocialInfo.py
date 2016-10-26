#!/usr/python
#coding:utf-8
import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler
from utils import KEY
from utils import STATUS
from utils import utils
from database import db


class Get_User_Social_Info_Handler(base_handler.BaseHandler):

    @tornado.web.authenticated
    def get(self):

        id = self.get_secure_cookie("id")
        data = {}
        data[KEY.ID] = int(id)
        data[KEY.STATE] = 0
        allRelationUser = db.query_follow(data);
        print(allRelationUser)
        user_Info = db.get_user_information(data)
        print '\n'
        print user_Info

        if (allRelationUser != -1):
            family = [elem for elem in allRelationUser if elem[KEY.RELATION_TYPE] == 0]
            neighbour = [elem for elem in allRelationUser if elem[KEY.RELATION_TYPE] == 1]
            career = [elem for elem in allRelationUser if elem[KEY.RELATION_TYPE] == 2]
            # avatar = user_Info[KEY.AVATAR] if user_Info[KEY.AVATAR] else "default.png"
            self.render("Ralationship.html", family = family, neighbour = neighbour, career = career)
        else:
            self.write("error")

