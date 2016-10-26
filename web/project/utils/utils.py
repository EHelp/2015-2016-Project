#!/usr/python
# -*- coding: utf-8 -*-
from tornado.escape import json_decode
import KEY

#对一个网页请求对象的解析，其中包括请求的一些信息，headers为字典类型
#解析后得到传入的数据
def decode_params(request):
  params = {}
  headerFormat = request.headers.get("Content-Type")
  try:
    if headerFormat == "application/json":
      params = json_decode(request.body)

    if headerFormat == "application/x-www-form-urlencoded" or headerFormat == "application/x-www-form-urlencoded; charset=UTF-8":

      params_str = str(request.body)
      params_duals = params_str.split("&")
      for duals in params_duals:
        dual = duals.split("=")
        params[dual[0]] = dual[1]
  except:
    pass
  finally:
    return transformat(params)

def is_App(request):
  headerFormat = request.headers.get("Content-Type")
  if headerFormat == "application/json":
  	return True
  else:
  	return False


def transformat(data):
  if KEY.ID in data:
    data[KEY.ID] = int(data[KEY.ID])
  if KEY.EVENT_ID in data:
    data[KEY.EVENT_ID] = int(data[KEY.EVENT_ID])
  if KEY.TYPE in data:
    data[KEY.TYPE] = int(data[KEY.TYPE])
  if KEY.LONGITUDE in data:
    data[KEY.LONGITUDE] = float(data[KEY.LONGITUDE])
  if KEY.LATITUDE in data:
    data[KEY.LATITUDE] = float(data[KEY.LATITUDE])
  if KEY.LAUNCHER_ID in data:
    data[KEY.LAUNCHER_ID] = int(data[KEY.LAUNCHER_ID])
  if KEY.USER_ID in data:
    data[KEY.USER_ID] = int(data[KEY.USER_ID])
  if KEY.OPERATION in data:
    data[KEY.OPERATION] = int(data[KEY.OPERATION])
  if KEY.STATUS in data:
    data[KEY.STATUS] = int(data[KEY.STATUS])
  if KEY.STATE in data:
    data[KEY.STATE] = int(data[KEY.STATE])
  if KEY.OCCUPATION in data:
    data[KEY.OCCUPATION] = int(data[KEY.OCCUPATION])
  if KEY.DEMAND_NUMBER in data:
    data[KEY.DEMAND_NUMBER] = int(data[KEY.DEMAND_NUMBER])
  if KEY.IS_VERIFY in data:
    data[KEY.IS_VERIFY] = int(data[KEY.IS_VERIFY])
  if KEY.ANSWER_ID in data:
    data[KEY.ANSWER_ID] = int(data[KEY.ANSWER_ID])
  return data

def trans_unicode_to_utf(data):
  if KEY.NAME in data and data[KEY.NAME] is not None:
    data[KEY.NAME] = data[KEY.NAME].encode('UTF-8')
  if KEY.NICKNAME in data and data[KEY.NICKNAME] is not None:
    data[KEY.NICKNAME] = data[KEY.NICKNAME].encode('UTF-8')
  if KEY.LOCATION in data and data[KEY.LOCATION] is not None:
    data[KEY.LOCATION] = data[KEY.LOCATION].encode('UTF-8')
  if KEY.TITLE in data and data[KEY.TITLE] is not None:
    data[KEY.TITLE] = data[KEY.TITLE].encode('UTF-8')
  if KEY.CONTENT in data and data[KEY.CONTENT] is not None:
    data[KEY.CONTENT] = data[KEY.CONTENT].encode('UTF-8')

  return data
