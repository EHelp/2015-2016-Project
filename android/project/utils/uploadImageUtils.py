#!/usr/python
#coding:utf-8
 
import os
 
#inputName为对应的上传图片 input里面的名称
#saveName为文件保存的名称--不包括后缀名
#path为文件保存的绝对路径---不包含文件名 路径为  例如project/handler  这样就可以
#return  success path(包括文件名的总路径)  fail None

def uploadImageUtils(request, inputName, saveName, path):

     if request.files == {} or inputName not in  request.files:
               
          return None

     # 判断格式
     image_type_list = ['image/gif', 'image/jpg', 'image/png']

     #获取对应的文件属性字典
     uploadFile = request.files[inputName][0]
     if uploadFile['content_type'] not in image_type_list:
          return None

     #限制大小 2M  len()字节数 
     if len(uploadFile['body']) > 2 * 1024 * 1024:
          
          return None

     #保存图片
     format = uploadFile['filename'].split('.').pop().lower()
     saveName = saveName + '.' + format
     filepath = os.path.join(path, saveName)
     
     with open(filepath,'wb') as up:
          up.write(uploadFile['body'])
     return filepath