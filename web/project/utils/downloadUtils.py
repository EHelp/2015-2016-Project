#!/usr/python
#coding:utf-8
'''
download file
params self当前请求类对象  filename = 是文件所在的位置加文件名 
       downloadname 下载的默认名称
'''
def downloadUtils(self, filename, downloadname):

    self.set_header ('Content-Type', 'application/octet-stream')
    self.set_header ('Content-Disposition', 'attachment; filename=' + downloadname)

    buff_size = 2048
    with open(filename, 'rb') as fileObject:
        while True:
            data = fileObject.read(buff_size)
            if not data:
                break
            self.write(data)
    self.finish()