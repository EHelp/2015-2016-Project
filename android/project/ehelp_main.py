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
#from handler import downloadApp_handler

from handlerforandroid import get_SMS_code
from handlerforandroid import register_app
from handlerforandroid import verify_SMS
from handlerforandroid import login_app
from handlerforandroid import get_Salt
from handlerforandroid import reset_pwd
from handlerforandroid import emergence_launch
from handlerforandroid import emergence_cancel
from handlerforandroid import emergence_complete
from handlerforandroid import give_support
from handlerforandroid import helper_list
from handlerforandroid import list_event_detail
from handlerforandroid import get_event_nearby
from handlerforandroid import evaluate_help
from handlerforandroid import get_helper_num
from handlerforandroid import get_user_information_handler
from handlerforandroid import modify_user_information_handler
from handlerforandroid import get_static_relation
from handlerforandroid import manage_static_relation
from handlerforandroid import get_my_events
from handlerforandroid import cancel_support
from handlerforandroid import help_launch
from handlerforandroid import add_answer
from handlerforandroid import delete_answer
from handlerforandroid import get_answers
from handlerforandroid import manage_event_like
from handlerforandroid import get_recipient_info
from handlerforandroid import handle_static_relation
from handlerforandroid import get_user_info_from_phone
from handlerforandroid import adopt_answer
from handlerforandroid import change_password
from handlerforandroid import change_phone
from handlerforandroid import change_email
from handlerforandroid import user_feedback
from handlerforandroid import delete_question_event

#lovingbangk
from handlerforlovebank import get_scoreandlovecoin
from handlerforlovebank import lovebankPersonalInfoHandler
from handlerforlovebank import transferChoose
from handlerforlovebank import transferHandler
from handlerforlovebank import exchange_coin_record
from handlerforlovebank import trade_coin_record
from handlerforlovebank import get_system_user_information
from handlerforlovebank import get_system_lovecoin_information
from handlerforlovebank import data_from_algorithm
from handlerforlovebank import maintain_system

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
            #(r"/account/userinfo/downloadApp", downloadApp_handler.DownloadApp_Handler),

            (r"/android/getMes", get_SMS_code.SendSMSCodeHandler),
            (r"/android/verifyMes", verify_SMS.verifySMSCodeHandler),
            (r"/android/register", register_app.APPRegisterHandler),
            (r"/android/login", login_app.Login_Handler),
            (r"/android/getSalt", get_Salt.GetSaltHandler),
            (r"/android/resetPassword", reset_pwd.Modify_Password_Handler),
            (r"/android/emergency_launch", emergence_launch.EmergenceLaunchHandler),
            (r"/android/emergency_cancel", emergence_cancel.EmergenceCancelHandler),
            (r"/android/emergency_complete", emergence_complete.EmergenceCompleteHandler),
            (r"/android/give_support", give_support.GiveSupportHandler),
            (r"/android/emergency_helper_list", helper_list.HelperListHandler),
            (r"/android/event_details", list_event_detail.ListEventDetailHandler),
            (r"/android/get_events", get_event_nearby.GetEventNearbyHandler),
            (r"/android/evaluate_event", evaluate_help.EvaluateHelpHandler),
            (r"/android/get_helper_num", get_helper_num.GetHelperNumHandler),
			(r"/android/user/get_information", get_user_information_handler.Get_User_Information_Handler),
            (r"/android/user/modify_information", modify_user_information_handler.Modify_User_Information_Handler),
			(r"/android/user/get_static_relation", get_static_relation.Get_Static_Relation_Handler),
			(r"/android/user/manage_static_relation", manage_static_relation.Manage_Static_Relation_Handler),
            (r"/android/user/change_password", change_password.ChangePWDHandler),
            (r"/android/user/modify_phone", change_phone.ModifyPhoneHandler),
            (r"/android/user/modify_email", change_email.ModifyEmailHandler),
			(r"/android/get_my_events", get_my_events.Get_My_Events_Handler),
            (r"/android/cancel_support", cancel_support.CancelSupportHandler),
            (r"/android/help_launch", help_launch.HelpLaunchHandler),
			(r"/android/event/add_answer", add_answer.Add_Answer_Handler),
			(r"/android/event/delete_answer", delete_answer.Delete_Answer_Handler),
			(r"/android/event/get_answers", get_answers.Get_Answers_Handler),
            (r"/android/event/adopt_answer", adopt_answer.AdoptAnswerHandler),
			(r"/android/event/manage_like", manage_event_like.Manage_Event_Like_Handler),
            (r"/android/help_launch", help_launch.HelpLaunchHandler),
            (r"/android/recipient_info", get_recipient_info.GetRecipientInfoHandler),
			(r"/android/user/handle_static_relation", handle_static_relation.Handle_Static_Relation_Handler),
            (r"/android/user/get_user_info_from_phone", get_user_info_from_phone.GetUserInfoFromPhoneHandler),
            (r"/android/feedback", user_feedback.FeedbackHandler),
            (r"/android/delete_question_event", delete_question_event.Delete_Question_event_Handler),

            (r"/android/lovingbank/lovebank_personal_information", lovebankPersonalInfoHandler.lovebank_personal_info),
            (r"/android/lovingbank/get_user_score_and_lovecoin", get_scoreandlovecoin.Get_ScoreAndLovecoin),
            (r"/android/lovingbank/choose_transfer", transferChoose.transferChoose), 
            (r"/android/lovingbank/handler_transfer",transferHandler.transferHandler),
            (r"/android/lovingbank/get_exchange_coin_record",exchange_coin_record.exchangeCoinRecord),
            (r"/android/lovingbank/get_trade_coin_record",trade_coin_record.tradeCoinRecord),
            (r"/android/lovingbank/get_system_user_information",get_system_user_information.get_system_user_information),
            (r"/android/lovingbank/get_system_lovecoin_information",get_system_lovecoin_information.get_system_lovecoin_information),
            (r"/android/lovingbank/data_from_algorithm",data_from_algorithm.data_from_algorithm),
            (r"/android/lovingbank/maintain_system",maintain_system.maintain_system),
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
