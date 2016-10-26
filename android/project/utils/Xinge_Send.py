#!/usr/bin/env python
#-*- coding: utf-8 -*-
import xinge
import KEY

access_id = "2100167910"
secret_key = "53ec71bcafdf3cfad26f132f7006cacd"

'''
send notification to the online user nearby.
@params a dict data:
        includes account, title, content.
@return true indicates notification is sent out successfully.
        otherwise, failed.
'''
'''

'''
def sendEhelp(account, mess):
	push = xinge.XingeApp(access_id, secret_key)
	ret = push.PushSingleAccount(0, account, mess)
	if ret[0] == 0:
		return True
	print ret[0]
	return False

'''build the message format, to make the message we want.
@params a dict data:
        includes type, title, content, style, action.
        
        type: 1 stands for the TYPE_NOTIFICATION
              2 stands for the TYPE_MESSAGE
        title: the title of message
        content: the content of message
        style: an object called Style
                '''通过这个四维向量的值来控制通知的类型，含义：样式编号0 ，响铃，震动，不可从通知栏清除'''
                for example:
                        Style(0, 1, 1, 1)

        action: an object called ClickAction
                if we want to set the relative information, for example:
                        action = ClickAction()
                        action.activity = 'MainActivity'
                        if user clicks the notification, we go into the MainActivity

@return the message object.
'''
def buildMessage(data):
	mess = xinge.Message()
        mess.type = data[KEY.TYPE]
	mess.title = data[KEY.TITLE]
        mess.content = data[KEY.CONTENT]
        mess.expireTime = 86400
        '''含义：样式编号0 ，响铃，震动，不可从通知栏清除'''
        mess.style = data[KEY.STYLE]
        '''we use the default action, that's to open the app'''
        mes.action = data[KEY.ACTION]
        t1 = xinge.TimeInterval(0, 0, 13, 59)
        t2 = xinge.TimeInterval(14, 0, 23, 59)
        mess.acceptTime = (t1, t2)
        return mess










'''backup
        mess = xinge.Message()
        mess.type = data[KEY.TYPE]
        mess.title = data[KEY.TITLE]
        mess.content = data[KEY.CONTENT]
        mess.expireTime = 86400
        mess.style = xinge.Style(0, 1, 1, 1)
        t1 = xinge.TimeInterval(0, 0, 13, 59)
        t2 = xinge.TimeInterval(14, 0, 23, 59)
        mess.acceptTime = (t1, t2)
        return mess
'''