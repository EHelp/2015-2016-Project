import tornado.web
import json

from utils import utils
from utils import KEY
from utils import sendSMS
from utils import Session
from database import db
from tornado.escape import json_encode

class APPRegisterHandler(tornado.web.RequestHandler):

    def post(self):
        params = {}
        resp = {}
        params = utils.decode_params(self.request)
        
        if KEY.ACCOUNT in params and KEY.PASSWORD in params and KEY.PHONE in params:
            if Session.Session.exists(params):
                '''if user not exists, return true'''
                if db.check_user_exist(params):
                    user_id = db.add_account(params)
                    if user_id > 0:
                        '''set the user phone number'''
                        db.update_user({KEY.ID: user_id, KEY.PHONE: params[KEY.PHONE]})
                        resp[KEY.STATUS] = 200
                        resp[KEY.ACCOUNT] = params[KEY.ACCOUNT]
                        resp[KEY.ID] = user_id
                        resp[KEY.SALT] = db.get_salt(params)
                        resp[KEY.CHAT_TOKEN] = db.get_chat_token(params)
                        bank_account_id = db.create_loving_bank(resp, 20, 0)
                        
                    else:
                        resp[KEY.STATUS] = 250
                else:
                    resp[KEY.STATUS] = 260
            else:
                resp[KEY.STATUS] = 270
        else:
            resp[KEY.STATUS] = 300

        self.write(json_encode(resp))
