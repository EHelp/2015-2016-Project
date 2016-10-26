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

if __name__ == '__main__':
    sendTemplateSMS('18926105076', {'2', '8888'}, 1)
