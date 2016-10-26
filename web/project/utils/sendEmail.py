# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
 

'''
sendEmail to one person or more
@params list_to_user_address title textContent
@return success 200 false 400 

'''

def sendEmail(list_to_user_address, title, textContent):

    from_mail = 'yongningfu123@126.com'
    #from_mail = 'ss2014yizhu@163.com'
    to_mail = ';'.join(list_to_user_address)

    msg = MIMEMultipart()
    msg['From'] = from_mail
    msg['To'] = to_mail
    msg['Subject'] = '%s'%(title)
    content = MIMEText('%s'%(textContent), _charset='utf8')
    msg.attach(content)

    try:
        server=smtplib.SMTP('smtp.126.com')
        #server=smtplib.SMTP('smtp.163.com')
        #server.set_debuglevel(1)
        server.docmd('ehlo','yongningfu123@126.com')
        #server.docmd('ehlo','ss2014yizhu@163.com')
        server.login('yongningfu123@126.com','cmuxhmavsvtmzipn')
        #server.login('ss2014yizhu@163.com','uklikyuytvjufgpl')
        try:
            server.sendmail(from_mail, list_to_user_address ,msg.as_string())
            server.quit()
            return 200
        except:
            server.quit()
            return 400
    except:
        return 400




'''
send emil to verify user information
@params realname identity_id imagePath link(click if accept)
@return if success 200 false 400
'''
def sendEmailForVerifyUser(realname, identity_id, imagePath, link):
    from_mail = 'yongningfu123@126.com'
    to_mail = ['535802703@qq.com', 'yongningfu123@126.com']
     
    msg = MIMEMultipart()
    msg['From'] = from_mail
    msg['To'] = ';'.join(to_mail)
    msg['Subject']='user verify'

    
    #realname = realname.decode('utf8')
    content = MIMEText(u'<b>realname<b>: %s<br/>identity_id: %s<br/>sure link: <a href="%s">%s</a>' %((realname), identity_id, link, link),'html', 'utf8')
    #print '----------------'

    msg.attach(content)

    attac = MIMEImage(file(imagePath,'rb').read())
    attac['Content-Type'] = 'application/octet-stream'

    imageFormat = imagePath.split('.').pop().lower()
    attac.add_header('content-disposition','attachment', filename='avatar.%s'%(imageFormat))
    msg.attach(attac)

    try:
        server = smtplib.SMTP('smtp.126.com')
        #server.set_debuglevel(1)
        server.docmd('ehlo','yongningfu123@126.com')
        server.login('yongningfu123@126.com','cmuxhmavsvtmzipn')
        try:
            
            server.sendmail(from_mail,to_mail,msg.as_string())
            server.quit()
            return 200
        except:
            server.quit()
            return 400
    except:
        return 400

        
    


    


