#coding:utf-8
import tornado.web
import tornado.websocket
import tornado.escape
import json
import time

from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class SocketCommentHandler(tornado.websocket.WebSocketHandler):
    onlineUser = []

    @staticmethod
    def send_to_all(message):
    	for user in SocketCommentHandler.onlineUser:

            #给每个socket对应链接的客户端发送信息
    		user.write_message(json.dumps(message))

    def open(self):
        SocketCommentHandler.onlineUser.append(self)

    def on_close(self):
        if self in SocketCommentHandler.onlineUser:
            SocketCommentHandler.onlineUser.remove(self)

    def on_message(self, message):
        mes = tornado.escape.json_decode(message)
        mes[KEY.ID] = int(mes[KEY.ID])

        '''indicate the status of create comment or question'''
        mes["resp_status"] = 200
        
        mes[KEY.TYPE] = 0


        '''to show the current time, but the format must be consistent with the database'''
        mes["date"] = time.asctime(time.localtime(time.time()))

        if mes["mesType"] == 0:

            mes[KEY.LOVE_COIN] = int(mes[KEY.LOVE_COIN]) #debug
            eventId = db.add_event(mes)

            if eventId > 0:

                mes["eventId"] = eventId


                SocketCommentHandler.send_to_all(mes)
            else:
                mes["resp_status"] = 500

                #debug
                #有错误时 把错误发给当前的websocket
                self.write_message(json.dumps(mes))
                #SocketCommentHandler.send_to_all(mes)
        
        #这是评论
        if mes["mesType"] == 1:


            mes["event_id"] = int(mes["event_id"])
            mes["parent_author"] = int(mes["author_id"])

            if db.add_comment(mes) > 0:

                SocketCommentHandler.send_to_all(mes)
            else:
                mes["resp_status"] = 500
