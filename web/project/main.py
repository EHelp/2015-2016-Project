#!/usr/python
#coding:utf-8
import tornado
import os
import sys
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import tornado.auth
import time

from handler import index_handler
from handler import struct_handler
from handler import culture_handler
from handler import help_handler
from handler import aboutus_handler
from handler import base_handler
from handler import regist_handler
from handler import get_salt_handler
from handler import login_handler
from handler import logout_handler
from handler import forget_pwd_handler
from handler import modify_password_handler
from handler import get_chat_token_handler
from handler import get_salt_handler
from handler import user_main_handler
from handler import socket_comment_handler
from handler import userinfo_modify_handler
from handler import password_verify_handler
from handler import get_user_record
from handler import get_user_love_coin
from handler import get_user_reputation
from handler import manageRelationship
from handler import getUserSocialInfo

from handler import showDownloadPage
#from handler import downloadApp_handler


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):

        handlers=[
            (r"/", index_handler.IndexHandler),
            (r"/structure", struct_handler.StructureHandler),
            (r"/culture", culture_handler.CultureHandler),
            (r"/help", help_handler.HelpHandler),
            (r"/aboutus", aboutus_handler.AboutusHandler),
            (r"/account", user_main_handler.MainHandler),
            (r"/account/regist", regist_handler.Regist_Handler),
            (r"/account/login", login_handler.Login_Handler),
            (r"/account/record", get_user_record.GetRecordHandler),
            (r"/account/get_iden_code", regist_handler.GetIdenCodeHandler),
            (r"/account/logout", logout_handler.LogoutHandler),
            (r"/account/get_salt_value", get_salt_handler.GetSaltHandler),
            (r"/account/forget", forget_pwd_handler.ForgetPwdHandler),
            (r"/account/forget/phone", forget_pwd_handler.GetPwdEmailHandler),
            (r"/account/forget/ident", forget_pwd_handler.GetIdentiHandler),
            (r"/account/setpwd", forget_pwd_handler.SetPwdHandler),
            (r"/socket/question", socket_comment_handler.SocketCommentHandler),
            (r"/modify/password", modify_password_handler.Modify_Password_Handler),
            (r"/account/userinfo/modify", userinfo_modify_handler.Userinfo_Modify_Handler),
            (r"/account/passwordVerify", password_verify_handler.Password_Verify_Handler),
            (r"/account/userinfo/modify/phone", userinfo_modify_handler.Userinfo_Modify_Phone_Handler),
            (r"/account/userinfo/modify/get/idenCode", userinfo_modify_handler.GetUserInfoModifyIdenCodeHandler),
            (r"/account/userinfo/modify/phone/success", userinfo_modify_handler.Userinfo_Modify_Phone_SOF_Handler),
            (r"/account/userinfo/modify/email", userinfo_modify_handler.Userinfo_Modify_Email_Handler),
            (r"/account/userinfo/modify/email_verify/(\w+)", userinfo_modify_handler.Userinfo_Modify_Email_Verify_Handler),
            (r"/account/userinfo/modify/email_wait", userinfo_modify_handler.Userinfo_Modify_Email_Wait_Handler),
            (r"/account/userinfo/modify/real_name_comfirm", userinfo_modify_handler.Userinfo_Modify_Real_Name_Comfirm_Handler),
            (r"/account/userinfo/modify/user_verify_by_email/(\w+)", userinfo_modify_handler.Userinfo_Modify_User_Verify_By_Email_Handler),
            (r"/account/userinfo/get_user_love_coin", get_user_love_coin.Get_Love_Coin),
            (r"/account/userinfo/get_user_reputation", get_user_reputation.Get_Reputation),
            (r"/account/manageRelationship", manageRelationship.Manage_Relationship_Handler),
            (r"/account/manageRelationship/delete", manageRelationship.Manage_Relationship_Delete_Handler),
            (r"/account/manageRelationship/update", manageRelationship.Manage_Relationship_update_Handler),
            (r"/account/getUserSocialInfo", getUserSocialInfo.Get_User_Social_Info_Handler),
            (r"/download", showDownloadPage.showDownloadPage),
            #(r"/account/userinfo/downloadApp", downloadApp_handler.DownloadApp_Handler),           
        ]

        settings = dict(
            cookie_secret="c14/YxGgSVeezF56Sx/SZ5QUQCgRS0R0gNA8GGfkrBU=",
            #xsrf_cookies=True,
            login_url="/account/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True
        )

        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
