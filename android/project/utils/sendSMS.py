#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from CCPRestSDK import REST
import ConfigParser

def sendTemplateSMS(to,datas,tempId):
    accountSid= '8a48b55150e162370150e6ad378825ac'; 

    accountToken= 'c67a265e8ec14ff48bc14737a803d59e'; 

    appId='8a48b55150e162370150e6ae3d5925c6'; 

    serverIP='app.cloopen.com';

    serverPort='8883'; 

    softVersion='2013-12-26';

    rest = REST(serverIP, serverPort, softVersion) 
    rest.setAccount(accountSid, accountToken) 
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to,datas,tempId) 
    if result['statusCode'] == '000000':
        return True
    return False

'''
if __name__ == '__main__':
    sendTemplateSMS('15521057950', {'2', '8888'}, 1)
'''
'''

#!/usr/bin/env python
# encoding: utf-8
import requests

class MobSMS:
    def __init__(self, appkey):
        self.appkey = appkey
        self.verify_url = 'https://api.sms.mob.com/sms/verify'

    def verify_sms_code(self, zone, phone, code, debug=False):
        if debug:
            return 200

        data = {'appkey': self.appkey, 'phone': phone, 'zone': zone, 'code': code}
        req = requests.post(self.verify_url, data=data, verify=False)
        if req.status_code == 200:
            j = req.json()
            return j.get('status', 500)

        return 500

def sendTemplateSMS(to,datas,tempId):
    mobsms = MobSMS('a257119e9293')
    if mobsms.verify_sms_code(86, to, datas[0]) != 500:
        return False
    return True

'''