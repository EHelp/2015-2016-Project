import tornado.web
import json

from utils import utils
from utils import KEY
from utils import Session
from tornado.escape import json_encode

class verifySMSCodeHandler(tornado.web.RequestHandler):

    def post(self):
        params = {}
        resp = {}
        params = utils.decode_params(self.request)
        
        if Session.Session.confirm_by_flag(params):
            resp[KEY.STATUS] = 200
        else:
            resp[KEY.STATUS] = 500
        self.write(json_encode(resp))