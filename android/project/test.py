#!/usr/bin/env python
#-*- coding: utf-8 -*-
from utils import xinge
from utils import KEY

access_id = "2100167910"
secret_key = "53ec71bcafdf3cfad26f132f7006cacd"

'''send xinge message
@params: account(the target), mess(a dict)
@return: true if succeeded, otherwise false.
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
                通过这个四维向量的值来控制通知的类型，含义：样式编号0 ，响铃，震动，不可从通知栏清除
                for example:
                        Style(0, 1, 1, 1)

        action: an object called ClickAction
                if we want to set the relative information, for example:
                        action = ClickAction()
                        action.activity = 'MainActivity'
                        if user clicks the notification, we go into the MainActivity

@return the message object.'''

def buildMessage(type=2, title='', content='', style=None, action=None, custom=None):
        mess = xinge.Message()
	mess.type = type
	mess.title = title
	mess.content = content
        mess.expireTime = 86400
        '''含义：样式编号0 ，响铃，震动，不可从通知栏清除'''
        mess.style = style
        '''we use the default action, that's to open the app'''
        if action is not None:
            action = xinge.ClickAction(activity=action)
        mess.action = action
        mess.custom = custom
        t1 = xinge.TimeInterval(0, 0, 13, 59)
        t2 = xinge.TimeInterval(14, 0, 23, 59)
        mess.acceptTime = (t1, t2)
        return mess

#使用方法举例如下：
    #example 1
    #发送一个notification：其中title为广州，content为中山大学，有响铃，有震动，不可清除。
    #mess = buildMessage(type=1, title='广州', content='中山大学', style=xinge.Style(0, 1, 1, 1))
    #print sendEhelp('ehelp_younglee', mess)

    #example 2
    #发送一个notification：其中title为广州，content为中山大学，有响铃，有震动，不可清除。
    #点击通知后，跳转到某一特定界面,这里是详细事件信息页面，一定要注意是完整包名+activity。
    #mess = buildMessage(type=1, title='广州', action='com.ehelp.ehelp.square.HelpMsgDetailActivity', content='中山大学', style=xinge.Style(0, 1, 1, 1))
    #print sendEhelp('ehelp_younglee', mess)

    #example 3
    #发送一个通透（用户根本没有任何感觉）的消息：其中title为广州，content为中山大学。
    #@params:这里type不需要设置，默认为消息。
    #mess = buildMessage(title='广州', content='中山大学')
    #print sendEhelp('ehelp_younglee', mess)

    #example 4
    #发送一个通透（用户根本没有任何感觉）的消息：另外发送key-value的字典数据.
    #@params:这里type不需要设置，默认为消息。
    #mess = buildMessage(title='广州', content='中山大学', custom={'name': 'lyang'})
    #print sendEhelp('ehelp_younglee', mess)
n = '汉'
u = 'youngle'
print repr(u)
print repr(n)
n.encode('UTF-8')
#print repr(n.encode('unicode'))
#n = n.encode('UTF-8')
c = {'name': u.encode('UTF-8')}
mess = buildMessage(title='广州', content='中山大学', custom=c)
#char = c['name']
#char = char.encode("UTF-8")
#print isinstance(char, unicode)
print sendEhelp('ehelp_younglee', mess)
