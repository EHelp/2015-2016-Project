import tornado.web

from utils import utils
from utils import KEY
from database import db
from tornado.escape import json_encode

class GetSaltHandler(tornado.web.RequestHandler):
    def post(self):
        params = {}
        params = utils.decode_params(self.request)
        resp = {}
        if KEY.PHONE in params:
            '''get id by phone, and get salt by id'''
            user_id = db.get_id_by_phone(params)
            salt = db.get_salt_by_id({KEY.ID: user_id})
            if salt is not None:
                resp[KEY.STATUS] = 200
                resp[KEY.SALT] = salt
            else:
                resp[KEY.STATUS] = 500
        else:
            resp[KEY.STATUS] = 500
        
        self.write(json_encode(resp))