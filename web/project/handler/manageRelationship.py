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


class Manage_Relationship_Handler(base_handler.BaseHandler):

    @tornado.web.authenticated
    def get(self):

        id = self.get_secure_cookie("id")
        data = {}
        data[KEY.ID] = int(id)
        data[KEY.STATE] = 0
        allRelationUser = db.query_follow(data);
        # print(allRelationUser)
        user_Info = db.get_user_information(data)

        if (allRelationUser != -1):
            family = [elem for elem in allRelationUser if elem[KEY.RELATION_TYPE] == 0]
            neighbour = [elem for elem in allRelationUser if elem[KEY.RELATION_TYPE] == 1]
            career = [elem for elem in allRelationUser if elem[KEY.RELATION_TYPE] == 2]
            # avatar = user_Info[KEY.AVATAR] if user_Info[KEY.AVATAR] else "default.png"
            self.render("Ralationship.html", family = family, neighbour = neighbour, career = career)
        else:
            self.write("error")


class Manage_Relationship_Delete_Handler(base_handler.BaseHandler):

    @tornado.web.authenticated
    def post(self):

        id = self.get_secure_cookie("id")
        resp = {}
        resp[KEY.STATUS] = STATUS.ERROR
        params = utils.decode_params(self.request)

        if KEY.NICKNAME in params:
            params[KEY.ID] = int(id)
            print params
            user_b = db.get_id_by_nickname(params)
            print user_b
            if user_b is not None:
                params[KEY.USER_ID] = user_b
                if db.remove_static_relation(params):
                    resp[KEY.STATUS] = STATUS.OK
        return self.write(json_encode(resp))


class Manage_Relationship_update_Handler(base_handler.BaseHandler):

    @tornado.web.authenticated
    def post(self):

        id = self.get_secure_cookie("id")
        resp = {}
        resp[KEY.STATUS] = STATUS.ERROR
        params = utils.decode_params(self.request)

        if KEY.NICKNAME in params and KEY.TYPE in params:
            params[KEY.ID] = int(id)
            user_b = db.get_id_by_nickname(params)
            
            if user_b is not None:
                params[KEY.USER_ID] = user_b
                if db.update_static_relation(params):
                    resp[KEY.STATUS] = STATUS.OK
        return self.write(json_encode(resp))


