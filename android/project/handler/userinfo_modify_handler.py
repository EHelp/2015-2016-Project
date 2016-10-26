#!/usr/python
#coding:utf-8
import tornado
import random
import string
import hashlib
from tornado.web import RequestHandler
from tornado.escape import json_encode
from handler import base_handler
import time
import os
import shutil


from utils import utils
from utils import KEY
from utils import STATUS
from utils import uploadImageUtils
from database import db


#----------debug----------

from utils import sendEmail
#----------debug-----------



class Userinfo_Modify_Handler(base_handler.BaseHandler):

    @tornado.web.authenticated
    def get(self):

        id = self.get_secure_cookie("id")
        data = {}
        data[KEY.ID] = int(id)
        user = db.get_user_information(data)
        if (user is not None):
            email = user[KEY.EMAIL].replace("%40", "@");
            self.render("userinfo-modify.html", id = user[KEY.ID], phone = user[KEY.PHONE], email = email, isverified = user[KEY.IS_VERIFY], account=user[KEY.NICKNAME])
        else:
            self.write("error")



class Userinfo_Modify_Phone_Handler(base_handler.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = self.get_secure_cookie("id")
        params = {}
        params[KEY.ID] = int(id)
        user = db.get_user_information(params)

        if user is not None:
            account = user[KEY.NICKNAME]
            email = user[KEY.EMAIL]
            self.render("changemobile.html", id = id, account = account, email = email)
        else:
            self.write("error")
    @tornado.web.authenticated
    def post(self):

        id = self.get_secure_cookie("id")
        resp = {}
        if self.get_secure_cookie("passwordVerify") != "yes":
            resp[KEY.STATUS] = 400
            
        else:
            params = utils.decode_params(self.request)

            resp[KEY.STATUS] = 500
            if KEY.ID in params and KEY.PHONE in params:
                
                params[KEY.ID] = int(params[KEY.ID])
                verify = db.update_user(params)
                if verify:

                    self.set_secure_cookie("passwordVerify", "no")

                    resp[KEY.STATUS] = 200
        
        return self.write(json_encode(resp))        


class Userinfo_Modify_Phone_SOF_Handler(base_handler.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        account = self.get_secure_cookie("username")
        params = {}
        params[KEY.ACCOUNT] = account
        userinfo = db.get_user_information(params)
        self.render("mobile-success.html", id = userinfo[KEY.ID])


class Userinfo_Modify_Email_Handler(base_handler.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = self.get_secure_cookie("id")
        self.render("changeemail.html", id = id);

    @tornado.web.authenticated
    def post(self):

        id = self.get_secure_cookie("id")
        resp = {}
        if self.get_secure_cookie("passwordVerify") != "yes":
            resp[KEY.STATUS] = 400
            
        else: 
            params = utils.decode_params(self.request)

            resp[KEY.STATUS] = 500
            if KEY.ID in params and KEY.EMAIL in params:
                

                emailAddress = params[KEY.EMAIL].replace("%40", "@")

                #防止有人跨过登录这个地址
                while (True):

                    idencode = ''.join(random.sample(string.ascii_letters, 4))
                    tempParams = {}
                    tempParams[KEY.IDENCODE] = idencode
                    if db.get_verify_email_by_idencode(tempParams) == None:
                        params[KEY.IDENCODE] = idencode
                        break


                link = "链接为: " + "http://120.24.208.130:8000/account/userinfo/modify/email_verify/" + params[KEY.IDENCODE]

                if sendEmail.sendEmail([emailAddress], "邮箱验证", link) == 200:

                    params[KEY.ID] = int(params[KEY.ID])
                    verify = db.add_email_verify(params)

                    if verify != -1:
                        
                        #self.set_secure_cookie("passwordVerify", "no")
                        resp[KEY.STATUS] = 200

        return self.write(json_encode(resp))


class Userinfo_Modify_Email_Verify_Handler(base_handler.BaseHandler):
    def get(self, idencode):
        #http://localhost:8000/account/userinfo/modify/email_verify/

        #获取email_id中的值 而且为最新的
        params = {}
        params[KEY.IDENCODE] = idencode

        params = db.get_verify_email_by_idencode(params)
        if params is None:
            return self.render("email-failed.html", email = None)


        verify_email_info = db.get_latest_verify_email(params)
        if verify_email_info is not None:   

            #先把数据库里面的全部删除
            db.clear_verify_email_info(params)

            #时间戳 设置时间间隔为10分钟链接失效
            s = verify_email_info[KEY.TIME]

            emailTime = time.mktime(s.timetuple())
            nowTime = time.time()

            email = verify_email_info[KEY.EMAIL].replace("%40", "@")
            timeInterval = nowTime - emailTime
            if timeInterval > 120:
                return self.render("email-failed.html", email = email)
            else:
                success = db.update_user(params)
                if success:
                    return self.render("email-success.html")
                else:
                    return self.render("email-failed.html", email = email)

        return self.render("email-failed.html", email = None)



class Userinfo_Modify_Email_Wait_Handler(base_handler.BaseHandler):
    
    @tornado.web.authenticated
    def get(self):
        account = self.get_secure_cookie("username")
        params = {}
        params[KEY.ACCOUNT] = account
        userinfo = db.get_user_information(params)
        newEmail = self.get_argument("email").replace('%40', "@")
        self.render('send-email.html', id=userinfo[KEY.ID], email=newEmail)


class Userinfo_Modify_Real_Name_Comfirm_Handler(base_handler.BaseHandler):
    @tornado.web.authenticated
    def get(self):

        id = self.get_secure_cookie("id")
        params = {}
        params[KEY.ID] = int(id)
        verify_user_info = db.get_user_verify_info(params)

        if verify_user_info is None:
            return self.render("real-nameComfirm.html", id = id)
        else:
            return self.render("comfirm-submit.html", id = id)


    @tornado.web.authenticated
    def post(self):
        
        id = self.get_secure_cookie("id")
        params = {}
        params[KEY.ID] = int(id)
        user = db.get_user_information(params)
        #加入邮件
        params[KEY.EMAIL] = user[KEY.EMAIL]
        #对图片名称加密
        md5_encode = hashlib.md5()
        md5_encode.update(str(id))
        saveName = md5_encode.hexdigest()

        #saveName = id
        nowpath = os.path.dirname(__file__).replace("handler", "static")
        path = os.path.join(nowpath, "images", "head")
        filepath = uploadImageUtils.uploadImageUtils(self.request, "fileImage", saveName, path)

        if filepath:
            params[KEY.NAME] = self.get_argument('realname')

            params[KEY.IDENTITY_ID] = self.get_argument('realID')
            #-----------------------------------------------------
            params[KEY.AVATAR] = saveName + filepath[-4:]

            #防止有人跨过登录这个地址
            while (True):

                idencode = ''.join(random.sample(string.ascii_letters, 4))
                tempParams = {}
                tempParams[KEY.IDENCODE] = idencode
                if db.get_user_verify_info(tempParams) == None:
                    params[KEY.IDENCODE] = idencode
                    break

            verify = db.add_user_verify(params)

            if verify != -1:

                link = "http://120.24.208.130:8000/account/userinfo/modify/user_verify_by_email/" + idencode
                if sendEmail.sendEmailForVerifyUser(params[KEY.NAME], params[KEY.IDENTITY_ID], filepath, link) == 200:

                    return self.render("comfirm-submit.html", id=id)

        return self.write('error')




class Userinfo_Modify_User_Verify_By_Email_Handler(base_handler.BaseHandler):

    def get(self, idencode):

        
        params = {}
        params[KEY.IDENCODE] = idencode

        #先判段是是否有人确认过了
        verify_user_info = db.get_user_verify_info(params)
        if verify_user_info is None:
            return self.write('the link is fail')

        #没有的话 清除数据
        db.clear_verify_user_info(verify_user_info)

        #判段时间是否失效

        s = verify_user_info[KEY.TIME]
        emailTime = time.mktime(s.timetuple())
        nowTime = time.time()
        timeInterval = nowTime - emailTime

        verify_user_info[KEY.EMAIL] = verify_user_info[KEY.EMAIL].replace("%40", "@")
        if timeInterval > 30:
            sendEmail.sendEmail([verify_user_info[KEY.EMAIL]], "认证失败消息", "您的实名认证失败,请重新认证")
            return self.write('the link is fail (The effective time has passed.)')
        else:
            verify_user_info[KEY.IS_VERIFY] = 1

            success = db.update_user(verify_user_info)
            if success:
                return self.write("success comfirm")
            else:
                sendEmail.sendEmail([verify_user_info[KEY.EMAIL]], "认证失败消息", "您的实名认证失败,请重新认证")
                return self.write("server error")




class GetUserInfoModifyIdenCodeHandler(base_handler.BaseHandler):
    
    @tornado.web.authenticated
    def post(self):
        resp = {}
        resp[KEY.STATUS] = 500
        params = {}
        params = utils.decode_params(self.request)
                
        if KEY.EMAIL in params and KEY.ACCOUNT in params:

            idencode = ''.join(random.sample(string.ascii_letters, 4))
            #emailt = email.PlainEmail()

            params[KEY.EMAIL] = params[KEY.EMAIL].replace("%40", '@')
            if sendEmail.sendEmail([params[KEY.EMAIL]], "账号信息修改", "您的验证码为：" + idencode) == 200:
                md5_encode = hashlib.md5()

                md5_encode.update(params[KEY.ACCOUNT] + idencode + "?" + params[KEY.EMAIL])
                idencode = md5_encode.hexdigest()
                resp[KEY.STATUS] = 200
                resp["secret"] = idencode

        self.write(json_encode(resp))




    

