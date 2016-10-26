import tornado
import time
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler
from datetime import *

from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class GetRecordHandler(tornado.web.RequestHandler):
    def post(self):
    	params = utils.decode_params(self.request)
    	userId = params["userId"]
    	frontDesk = {}
    	
        frontDesk["currentUserRecordInfo"] = {}
        '''for question event's data-------------start------------'''
        frontDesk["currentUserRecordInfo"]["question"] = {}
        question_launch_event_list = db.get_launch_event_list({KEY.ID: int(userId), KEY.TYPE: 0})
        frontDesk["currentUserRecordInfo"]["question"]["ask_num"] = len(question_launch_event_list)
        frontDesk["currentUserRecordInfo"]["question"]["ask_date"] = []
        #print frontDesk["currentUserRecordInfo"]["question"]["ask_num"]

        tempDate = []
        for item in question_launch_event_list:
            tempEventInfo = db.get_event_datetime({KEY.EVENT_ID: item})
            tempDate.append(tempEventInfo["time"])

        frontDesk["currentUserRecordInfo"]["question"]["ask_date"] = getCountNum(tempDate)

        
        
        question_reply_time_list = db.get_comment_by_id({KEY.ID: int(userId)})        
        frontDesk["currentUserRecordInfo"]["question"]["reply_num"] = len(question_reply_time_list)

        frontDesk["currentUserRecordInfo"]["question"]["reply_date"] = getCountNum(question_reply_time_list)

        #print frontDesk["currentUserRecordInfo"]["question"]["reply_num"]

        '''for question event's data-------------end--------------'''

        '''for help event's data-------------start------------'''
        frontDesk["currentUserRecordInfo"]["help"] = {}
        help_launch_event_list = db.get_launch_event_list({KEY.ID: int(userId), KEY.TYPE: 1})
        frontDesk["currentUserRecordInfo"]["help"]["ask_num"] = len(help_launch_event_list)
        #print frontDesk["currentUserRecordInfo"]["help"]["ask_num"]
        frontDesk["currentUserRecordInfo"]["help"]["ask_date"] = []
        tempDate = []
        for item in help_launch_event_list:
            tempEventInfo = db.get_event_datetime({KEY.EVENT_ID: item})
            tempDate.append(tempEventInfo["time"])
        frontDesk["currentUserRecordInfo"]["help"]["ask_date"] = getCountNum(tempDate)


        help_reply_time_list = db.get_support_time({KEY.ID: int(userId), KEY.TYPE: 2, "event_type": 1})        
        frontDesk["currentUserRecordInfo"]["help"]["reply_num"] = len(help_reply_time_list)
        frontDesk["currentUserRecordInfo"]["help"]["reply_date"] = getCountNum(help_reply_time_list)
        #print frontDesk["currentUserRecordInfo"]["help"]["reply_num"]

        '''for help event's data---end----'''

        '''for save event's data-------------start------------'''
        frontDesk["currentUserRecordInfo"]["save"] = {}
        save_launch_event_list = db.get_launch_event_list({KEY.ID: int(userId), KEY.TYPE: 2})
        frontDesk["currentUserRecordInfo"]["save"]["ask_num"] = len(save_launch_event_list)
        #print frontDesk["currentUserRecordInfo"]["save"]["ask_num"]
        frontDesk["currentUserRecordInfo"]["save"]["ask_date"] = []
        tempDate = []
        for item in save_launch_event_list:
            tempEventInfo = db.get_event_datetime({KEY.EVENT_ID: item})
            tempDate.append(tempEventInfo["time"])
        frontDesk["currentUserRecordInfo"]["save"]["ask_date"] = getCountNum(tempDate)

        save_reply_time_list = db.get_support_time({KEY.ID: int(userId), KEY.TYPE: 2, "event_type": 2})        
        frontDesk["currentUserRecordInfo"]["save"]["reply_num"] = len(save_reply_time_list)
        #print frontDesk["currentUserRecordInfo"]["save"]["reply_num"]
        frontDesk["currentUserRecordInfo"]["save"]["reply_date"] = getCountNum(save_reply_time_list)
        
        '''for save event's data---end----'''
        '''
        temp_str = ""
        for item in frontDesk["currentUserRecordInfo"]["save"]["reply_date"]:
        	temp_str = temp_str + str(item) + ":"
        frontDesk["currentUserRecordInfo"]["save"]["reply_date"] = temp_str
        '''
        self.write(json_encode(frontDesk))


def getCountNum(tempDate):
    nowtime = datetime.now();
    data = [0, 0, 0, 0, 0, 0]
    timePoint = []
    for item in range(0, 7):
        delta_t = timedelta(item * 30)
        timePoint.append(nowtime - delta_t)

    for itemDate in tempDate:
        temp = itemDate
        for item in range(1, 7):
            if temp > timePoint[item] and temp < timePoint[item - 1]:
                data[item - 1] += 1
    return data
