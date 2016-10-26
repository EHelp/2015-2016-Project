import tornado.web
import json
import random
import string
import uuid
import redis

from tornado.escape import json_encode
from utils import utils
from utils import KEY
from utils import sendSMS
from utils import Session
from database import db

class SendSMSCodeHandler(tornado.web.RequestHandler):

    def post(self):
        params = {}
        resp = {}
        params = utils.decode_params(self.request)
        
        if KEY.PHONE in params and KEY.TYPE in params:
            if params[KEY.TYPE] == 0:
                '''if phone no exists'''
                if db.check_phone_exist(params):
                    resp = dealWithSend(params)
                else:
                    resp[KEY.STATUS] = 300

            if params[KEY.TYPE] == 1:
                '''if phone exists'''
                if not db.check_phone_exist(params):
                    resp = dealWithSend(params)
                else:
                    resp[KEY.STATUS] = 400

        else:
            resp[KEY.STATUS] = 500

        self.write(json_encode(resp))

def dealWithSend(params):
    resp = {}
    uuid_strs = str(uuid.uuid1())
    sms_code = ""
    '''for item in random.sample(range(0, 10), 4):
        sms_code += str(item)'''

    #if sendSMS.sendTemplateSMS(params[KEY.PHONE], [sms_code, 2], 1):
    sms_code = "1234"
    if True:
        Session.Session.insert_session({KEY.TEMP_ID: uuid_strs, KEY.SMSCODE: sms_code})
        resp[KEY.TEMP_ID] = uuid_strs
        resp[KEY.STATUS] = 200
    else:
        resp[KEY.STATUS] = 250
    return resp
