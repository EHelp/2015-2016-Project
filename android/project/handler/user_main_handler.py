#!/usr/python
# encoding: utf-8

import tornado
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler

from utils import utils
from utils import KEY
from utils import STATUS
import string
from database import db

class MainHandler(base_handler.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        '''----------------------------------------------------------------------------------'''
    	'''----------------search the nearby event from the database-------------------------'''
        '''----------------------------------------------------------------------------------'''
        userId = self.get_secure_cookie("id")
    	eventData = {}
        frontDesk = {}
        frontDesk["quesEvent"] =  []
        frontDesk["helpEvent"] = []
        frontDesk["saveEvent"] = []

    	eventData[KEY.ID] = int(userId)

        #注意项目中的事件信息和评论的区别
        #事件是每个有标题有内容的大部分
        #评论是每个事件下面的小部分内容
        '''get question event infomation------start-----'''
    	eventData[KEY.TYPE] = 0

        quesTempData = db.get_nearby_event(eventData)
        if len(quesTempData) > 5:
            quesTempData = quesTempData[0:5]
    	for item in quesTempData:
            data = {}
            data[KEY.EVENT_ID] = item
            
            eventInfo = {}
            eventAllInfo = db.get_event_information(data)
            '''get event information'''
            eventInfo["eventinfos"] = {}
            eventInfo["eventinfos"]["event_id"] = eventAllInfo[KEY.EVENT_ID]
            eventInfo["eventinfos"]["launcher_id"] = eventAllInfo[KEY.LAUNCHER_ID]
            eventInfo["eventinfos"]["event_title"] = eventAllInfo[KEY.TITLE]
            eventInfo["eventinfos"]["event_content"] = eventAllInfo[KEY.CONTENT]
            eventInfo["eventinfos"]["event_time"] = eventAllInfo[KEY.TIME]
            eventInfo["eventinfos"]["love_coin"] = eventAllInfo[KEY.LOVE_COIN]

            '''get event comments information'''
            eventInfo["comments"] = []
            eventAllComs = db.get_comments(data)
            eventInfo["comments_num"] = len(eventAllComs)
            for item in eventAllComs:
                temp = {}

                commenterProfile = db.get_user_extra_information(int(item[KEY.AUTHOR_ID]))
                if commenterProfile["name"] != None:
                    fout = open('static/images/head/' + commenterProfile["name"], 'wb')

                    #数据库里面可以存一个图片的或者其他类型的二进制文件，把数据库
                    #里面的数据读到图片文件中
                    fout.write(commenterProfile["profile"])
                    fout.close()
                else:
                    commenterProfile["name"] = "default.png"

                #-----------------------debug--------------------------

                commenterAvatar = db.get_user_information({"id":int(item[KEY.AUTHOR_ID])})
                if commenterAvatar[KEY.IS_VERIFY] == 1:

                    #print commenterAvatar[KEY.AVATAR]
                    commenterProfile["name"] = commenterAvatar[KEY.AVATAR]

                #------------------------------------------------------


                temp["comment_pic_src"] = commenterProfile["name"]
                temp["comment_author"] = item[KEY.AUTHOR]
                temp["comment_content"] = item[KEY.CONTENT]
                temp["comment_time"] = item[KEY.TIME]
                eventInfo["comments"].append(temp)

            
            #获得事件发起人的信息，event_id是整个事件的信息，
            #里面的launcher_id为发起人的id    
            '''get launcher information'''
            eventInfo["launcherinfos"] = {}
            userAllInfo = db.get_user_information({KEY.ID: eventAllInfo[KEY.LAUNCHER_ID]})
            eventInfo["launcherinfos"]["launcher_nickname"] = userAllInfo[KEY.NICKNAME]
            eventInfo["launcherinfos"]["launcher_reputation"] = userAllInfo[KEY.REPUTATION]
            eventInfo["launcherinfos"]["launcher_type"] = userAllInfo[KEY.TYPE]
            eventInfo["launcherinfos"]["launcher_isverify"] = userAllInfo[KEY.IS_VERIFY]
            '''get launcher profile'''
            launcherExtraInfo = db.get_user_extra_information(int(eventAllInfo[KEY.LAUNCHER_ID]))
            if launcherExtraInfo["name"] != None:
                fout = open('static/images/head/' + launcherExtraInfo["name"], 'wb')
                fout.write(launcherExtraInfo["profile"])
                fout.close()
            else:
                launcherExtraInfo["name"] = "default.png"


            #-----------------------------debug--------------------------
            if userAllInfo[KEY.IS_VERIFY]:
                launcherExtraInfo["name"] = userAllInfo[KEY.AVATAR]







            #-----------------------------------------------------------



            eventInfo["launcherinfos"]["launcher_profile"] = launcherExtraInfo["name"]

            frontDesk["quesEvent"].append(eventInfo)

        '''get question event infomation-----end------'''

        '''get help event information-----start------'''
        eventData[KEY.TYPE] = 1
        helpTempData = db.get_nearby_event(eventData)
        if len(helpTempData) > 5:
            helpTempData = helpTempData[0:5]

        for item in helpTempData:
            data = {}
            data[KEY.EVENT_ID] = item
            
            eventInfo = {}
            eventAllInfo = db.get_event_information(data)
            '''get event information'''
            eventInfo["eventinfos"] = {}
            eventInfo["eventinfos"]["event_id"] = eventAllInfo[KEY.EVENT_ID]
            eventInfo["eventinfos"]["launcher_id"] = eventAllInfo[KEY.LAUNCHER_ID]
            eventInfo["eventinfos"]["event_title"] = eventAllInfo[KEY.TITLE]
            eventInfo["eventinfos"]["event_content"] = eventAllInfo[KEY.CONTENT]
            eventInfo["eventinfos"]["event_time"] = eventAllInfo[KEY.TIME]
            eventInfo["eventinfos"]["love_coin"] = eventAllInfo[KEY.LOVE_COIN]

            eventInfo["eventinfos"]["event_state"] = eventAllInfo[KEY.STATE]
            eventInfo["eventinfos"]["event_longitude"] = eventAllInfo[KEY.LONGITUDE]
            eventInfo["eventinfos"]["event_latitude"] = eventAllInfo[KEY.LATITUDE]
            eventInfo["eventinfos"]["event_follower_num"] = eventAllInfo[KEY.FOLLOW_NUMBER]
            eventInfo["eventinfos"]["event_supporter_num"] = eventAllInfo[KEY.SUPPORT_NUMBER]
            eventInfo["eventinfos"]["event_location"] = eventAllInfo[KEY.LOCATION]

            '''get launcher information'''
            eventInfo["launcherinfos"] = {}
            userAllInfo = db.get_user_information({KEY.ID: eventAllInfo[KEY.LAUNCHER_ID]})
            eventInfo["launcherinfos"]["launcher_nickname"] = userAllInfo[KEY.NICKNAME]
            eventInfo["launcherinfos"]["launcher_reputation"] = userAllInfo[KEY.REPUTATION]
            eventInfo["launcherinfos"]["launcher_type"] = userAllInfo[KEY.TYPE]
            eventInfo["launcherinfos"]["launcher_isverify"] = userAllInfo[KEY.IS_VERIFY]
            '''get launcher profile'''
            launcherExtraInfo = db.get_user_extra_information(int(eventAllInfo[KEY.LAUNCHER_ID]))
            eventInfo["launcherinfos"]["launcher_profile"] = launcherExtraInfo["profile"]

            frontDesk["helpEvent"].append(eventInfo)
        '''get help event information-----end-----'''


        '''get save event information-----start---'''
        eventData[KEY.TYPE] = 2

        saveTempData = db.get_nearby_event(eventData)
        if len(saveTempData) > 5:
            saveTempData = saveTempData[0:5]
        for item in saveTempData:
            data = {}
            data[KEY.EVENT_ID] = item
            
            eventInfo = {}
            eventAllInfo = db.get_event_information(data)
            '''get event information'''
            eventInfo["eventinfos"] = {}
            eventInfo["eventinfos"]["event_id"] = eventAllInfo[KEY.EVENT_ID]
            eventInfo["eventinfos"]["launcher_id"] = eventAllInfo[KEY.LAUNCHER_ID]
            eventInfo["eventinfos"]["event_title"] = eventAllInfo[KEY.TITLE]
            eventInfo["eventinfos"]["event_content"] = eventAllInfo[KEY.CONTENT]
            eventInfo["eventinfos"]["event_time"] = eventAllInfo[KEY.TIME]

            eventInfo["eventinfos"]["event_state"] = eventAllInfo[KEY.STATE]
            eventInfo["eventinfos"]["event_longitude"] = eventAllInfo[KEY.LONGITUDE]
            eventInfo["eventinfos"]["event_latitude"] = eventAllInfo[KEY.LATITUDE]
            eventInfo["eventinfos"]["event_follower_num"] = eventAllInfo[KEY.FOLLOW_NUMBER]
            eventInfo["eventinfos"]["event_supporter_num"] = eventAllInfo[KEY.SUPPORT_NUMBER]

            '''get launcher information'''
            eventInfo["launcherinfos"] = {}
            userAllInfo = db.get_user_information({KEY.ID: eventAllInfo[KEY.LAUNCHER_ID]})
            eventInfo["launcherinfos"]["launcher_nickname"] = userAllInfo[KEY.NICKNAME]
            eventInfo["launcherinfos"]["launcher_reputation"] = userAllInfo[KEY.REPUTATION]
            eventInfo["launcherinfos"]["launcher_type"] = userAllInfo[KEY.TYPE]
            eventInfo["launcherinfos"]["launcher_isverify"] = userAllInfo[KEY.IS_VERIFY]
            '''get launcher profile'''
            launcherExtraInfo = db.get_user_extra_information(int(eventAllInfo[KEY.LAUNCHER_ID]))
            eventInfo["launcherinfos"]["launcher_profile"] = launcherExtraInfo["profile"]

            frontDesk["saveEvent"].append(eventInfo)

        '''get save event information----end------'''

        '''----------------------------------------------------------------------------------'''
        '''----------------current user information from the database------------------------'''
        '''----------------------------------------------------------------------------------'''
        frontDesk["currentUserInfo"] = {}
        userBasicInfo = db.get_user_information({KEY.ID: int(userId)})
        frontDesk["currentUserInfo"]["user_nickname"] = userBasicInfo[KEY.NICKNAME]
        userExtraInfo = db.get_user_extra_information(int(userId))
        frontDesk["currentUserInfo"]["user_profile"] = userExtraInfo["profile"]
        frontDesk["currentUserInfo"]["user_concernNum"] = userExtraInfo["concernNum"]
        frontDesk["currentUserInfo"]["user_checkIn"] = userExtraInfo["checkIn"]

        userBankInfo = db.get_user_loving_bank({"user_id": int(userId)})
        frontDesk["currentUserInfo"]["user_score"] = userBankInfo[KEY.SCORE]
        frontDesk["currentUserInfo"]["user_checkIn"] = userBankInfo[KEY.LOVE_COIN]


        '''----------------------------------------------------------------------------------'''
        '''----------------current user record information from the database-----------------'''
        '''----------------------------------------------------------------------------------'''
        frontDesk["currentUserRecordInfo"] = {}
        '''for question event's data-------------start------------'''
        frontDesk["currentUserRecordInfo"]["question"] = {}
        question_launch_event_list = db.get_launch_event_list({KEY.ID: int(userId), KEY.TYPE: 0})
        frontDesk["currentUserRecordInfo"]["question"]["ask_num"] = len(question_launch_event_list)
        frontDesk["currentUserRecordInfo"]["question"]["ask_date"] = []
        for item in question_launch_event_list:
            tempEventInfo = db.get_event_information({KEY.EVENT_ID: item})
            frontDesk["currentUserRecordInfo"]["question"]["ask_date"].append(tempEventInfo["time"])

        question_reply_time_list = db.get_comment_by_id({KEY.ID: int(userId)})        
        frontDesk["currentUserRecordInfo"]["question"]["reply_num"] = len(question_reply_time_list)
        frontDesk["currentUserRecordInfo"]["question"]["reply_date"] = question_reply_time_list
        '''for question event's data-------------end--------------'''

        '''for help event's data-------------start------------'''
        frontDesk["currentUserRecordInfo"]["help"] = {}
        help_launch_event_list = db.get_launch_event_list({KEY.ID: int(userId), KEY.TYPE: 1})
        frontDesk["currentUserRecordInfo"]["help"]["ask_num"] = len(help_launch_event_list)
        frontDesk["currentUserRecordInfo"]["help"]["ask_date"] = []
        for item in help_launch_event_list:
            tempEventInfo = db.get_event_information({KEY.EVENT_ID: item})
            frontDesk["currentUserRecordInfo"]["help"]["ask_date"].append(tempEventInfo["time"])

        help_reply_time_list = db.get_support_time({KEY.ID: int(userId), KEY.TYPE: 2, "event_type": 1})        
        frontDesk["currentUserRecordInfo"]["help"]["reply_num"] = len(help_reply_time_list)
        frontDesk["currentUserRecordInfo"]["help"]["reply_date"] = help_reply_time_list
        '''for help event's data---end----'''

        '''for save event's data-------------start------------'''
        frontDesk["currentUserRecordInfo"]["save"] = {}
        save_launch_event_list = db.get_launch_event_list({KEY.ID: int(userId), KEY.TYPE: 2})
        frontDesk["currentUserRecordInfo"]["save"]["ask_num"] = len(save_launch_event_list)
        frontDesk["currentUserRecordInfo"]["save"]["ask_date"] = []
        for item in save_launch_event_list:
            tempEventInfo = db.get_event_information({KEY.EVENT_ID: item})
            frontDesk["currentUserRecordInfo"]["save"]["ask_date"].append(tempEventInfo["time"])

        save_reply_time_list = db.get_support_time({KEY.ID: int(userId), KEY.TYPE: 2, "event_type": 2})        
        frontDesk["currentUserRecordInfo"]["save"]["reply_num"] = len(save_reply_time_list)
        frontDesk["currentUserRecordInfo"]["save"]["reply_date"] = save_reply_time_list
        '''for save event's data---end----'''

        #self.write(frontDesk)
        self.render('information.html', userId=userId, userName = self.current_user, disData = frontDesk)
        #self.render('demo.html', userId=userId, userName = self.current_user, eventInfo = frontDesk)