import tornado.web
import tornado.auth
import tornado.gen
import tornado.httpclient
import json
import time

from utils import utils
from utils import KEY
from database import db

class GetSaltHandler(tornado.web.RequestHandler):

    def post(self):


        params = {}
        params = utils.decode_params(self.request)
        salt = ""

        if KEY.ACCOUNT in params:

            salt = db.get_salt(params)
        elif KEY.ID in params:

            params[KEY.ID] = int(params[KEY.ID])

            salt = db.get_salt_by_id(params)

        if salt is None:
            salt = ""
        self.write(salt)