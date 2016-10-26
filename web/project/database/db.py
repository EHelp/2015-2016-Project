#!/usr/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import random
import string
import hashlib
import MySQLdb
import ast
import traceback

from dbhelper import dbhelper
from utils import haversine
from utils import KEY
from utils import STATUS
from utils import getToken


import sys 
reload(sys) 
#print sys.getdefaultencoding(); 

'''
add a new account to database.
@params a dict data:
        includes account and password.
@return -1 indicates params are not complete. Or account is not unique that leads to database fails.
        other number indicates success and the number is the id of the new account.
'''
def add_account(data):
  if KEY.ACCOUNT not in data or KEY.PASSWORD not in data:
    return -1
  
  salt = ''.join(random.sample(string.ascii_letters, 8))
  md5_encode = hashlib.md5()
  md5_encode.update(data[KEY.PASSWORD]+salt)
  password = md5_encode.hexdigest()

  sql_account = "insert into account (account, password, salt) values ('%s', '%s', '%s')"
  sql_user = "insert into user (id, nickname, phone) values (%d, '%s', '%s')"
  sql_user_extra = "insert into user_extension (userId) values (%d)"
  try:
    insert_id = dbhelper.insert(sql_account%(data[KEY.ACCOUNT], password, salt))
    dbhelper.insert(sql_user%(insert_id, data[KEY.ACCOUNT], data[KEY.ACCOUNT]))

    dbhelper.insert(sql_user_extra%(insert_id))
    chat_token = getToken.getToken(insert_id, None, None)
    sql_chat = "update account set chat_token = '%s' where id = %d"
    dbhelper.execute(sql_chat%(chat_token, insert_id))
    return insert_id
  except Exception, e:
    print e
    return -1

'''
update information of an account.
@params a dict data:
        includes id and chat_token:
@return True if successfully modify chat_token
        False modification fails.
'''
def update_account(data):
  if KEY.ID in data and KEY.CHAT_TOKEN in data:
    sql = "update account set chat_token = '%s' where id = %d"
    try:
      if dbhelper.execute(sql%(data[KEY.CHAT_TOKEN], data[KEY.ID])) > 0:
        return True
    except:
      return False
  else:
    return False


'''
modify user's information.
@params a dict data:
        options include user's name, nickname, gender, age, phone, location,
        (longitude and latitude), occupation, identity_id, reputation.
@return True if successfully modify
        False modification fails.
'''
def update_user(data):
  if KEY.ID not in data:
    return False
  result = True
  
  sql = ""
  if KEY.NAME in data:
    data[KEY.NAME] = MySQLdb.escape_string(data[KEY.NAME].encode("utf8"))
    sql = "update user set name = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.NAME], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.NICKNAME in data:
    data[KEY.NICKNAME] = MySQLdb.escape_string(data[KEY.NICKNAME].encode("utf8"))
    sql = "update user set nickname = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.NICKNAME], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.GENDER in data:
    sql = "update user set gender = %d where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.GENDER], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.AGE in data:
    sql = "update user set age = %d where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.AGE], data[KEY.ID]))
      result &= True
    except:
      result &= False
   
  if KEY.PHONE in data:
    sql = "update user set phone = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.PHONE], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.LOCATION in data:
    data[KEY.LOCATION] = MySQLdb.escape_string(data[KEY.LOCATION].encode("utf8"))
    sql = "update user set location = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.LOCATION], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.LONGITUDE in data and KEY.LATITUDE in data:
    sql = "update user set longitude = %f, latitude = %f where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.LONGITUDE], data[KEY.LATITUDE], data[KEY.ID]))
      result &= True
    except:
      result &= False
  elif not (KEY.LONGITUDE not in data and KEY.LATITUDE not in data):
    result &= False

  if KEY.OCCUPATION in data:
    sql = "update user set occupation = %d where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.OCCUPATION], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.IDENTITY_ID in data:
    sql = "update user set identity_id = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.IDENTITY_ID], data[KEY.ID]))
      result &= True
    except:
      result &= False


  if KEY.EMAIL in data:
    sql = "update user set email = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.EMAIL], data[KEY.ID]))
      result &= True
    except:
      result &= False


  if KEY.IS_VERIFY in data:
    sql = "update user set isVerify = %d where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.IS_VERIFY], data[KEY.ID]))
      result &= True
    except:
      result &= False


  if KEY.AVATAR in data:
    sql = "update user set avatar = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.AVATAR], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.REPUTATION in data:
    sql = "update user set reputation = %f where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.REPUTATION], data[KEY.ID]))
      result &= True
    except:
      result &= False

  return result


'''
get salt of an account.
@params include user's account.
@return salt of an account.
  None if account not exists or database query error.
'''
def get_salt(data):
  if KEY.ACCOUNT not in data:
    return None
  sql = "select salt from account where account = '%s'"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.ACCOUNT]))
    if res is None:
      return None
    else:
      return res[0]
  except:
    return None

'''get id from the phone
@params include user's phone
@return user's id
  None if it does not exist!
'''
def get_id_by_phone(data):
  if KEY.PHONE not in data:
    return None
  sql = "select id from user where phone = '%s'"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.PHONE]))
    if res is None:
      return None
    else:
      return res[0]
  except Exception, e:
    print e
    return None


'''get id from the nickname
@params include user's nickname
@return user's id
  None if it does not exist!
'''
def get_id_by_nickname(data):
  if KEY.NICKNAME not in data:
    return None
  sql = "select id from user where nickname = '%s'"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.NICKNAME]))
    if res is None:
      return None
    else:
      return res[0]
  except Exception, e:
    print e
    return None


'''get account or nickname from the phone
@params include user's phone
@return user's nickname or account
  None if it does not exist!
'''
def get_account_by_phone(data):
  if KEY.PHONE not in data:
    return None
  user_sql = "select nickname from user where phone = '%s'"
  try:
    res = dbhelper.execute_fetchone(user_sql%(data[KEY.PHONE]))
    if res is None:
      return None
    else:
      return res[0]
  except Exception, e:
    print e

'''
get salt by id.
@params include user's id.
@return salt of an id.
  None if id not exists or database query error.
'''
def get_salt_by_id(data):
  if KEY.ID not in data:
    return None
  sql = "select salt from account where id = '%d'"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.ID]))
    if res is None:
      return None
    else:
      return res[0]
  except:
    return None

'''
check the account whether is used already.
@params include user's account.
@return bool.
  yes if not exists and else no.
'''
def check_user_exist(data):
  if KEY.ACCOUNT not in data:
    return False
  if get_salt(data) is not None:
    return False
  return True

'''
check the phone whether is used already.
@params include user' phone.
@return bool.
  yes if not exists and else no.
'''
def check_phone_exist(data):
  if KEY.PHONE not in data:
    return False
  if get_account_by_phone(data) is not None:
    return False
  return True

'''
get password by id.
@params include user's id.
@return salt of an id.
  None if id not exists or database query error.
'''
def get_password_by_id(data):
  if KEY.ID not in data:
    return None
  sql = "select password from account where id = '%d'"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.ID]))
    if res is None:
      return None
    else:
      return res[0]
  except:
    return None



'''
validate whether password is correct.
@params includes user's account and password.
                      password need to be md5 encode.
@return user's id if password is correct.
         -1 otherwise.
'''
def validate_password(data):

  if KEY.ACCOUNT not in data or KEY.PASSWORD not in data or KEY.SALT not in data:
    return -1
  sql = "select id, password from account where account = '%s' and salt = '%s'"
  user_id = -1
  password = None
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.ACCOUNT], data[KEY.SALT]))
    if res is not None:
      user_id = res[0]
      password = res[1]
  except:
    pass
  finally:
    print user_id
    print password
    if password is None or data[KEY.PASSWORD] is None:
      return -1
    elif password == data[KEY.PASSWORD]:
      return user_id
    else:
      return -1

'''
modify user's password to a new one, but not modify its salt value.
@params include user's account, phone, newPassword(the raw password).
@return true if successfully modify.
           false otherwise.
'''
def android_modify_password(data):
  if KEY.PASSWORD not in data or KEY.PHONE not in data:
    return False
  data[KEY.ACCOUNT] = get_account_by_phone(data)
  user_id = get_id_by_phone(data)
  if user_id < 0:
    return False
  salt = get_salt_by_id({KEY.ID: user_id})
  if salt is None:
    return False
  md5_encode = hashlib.md5()
  md5_encode.update(data[KEY.PASSWORD] + salt)
  data[KEY.PASSWORD] = md5_encode.hexdigest()

  sql = "update account set password = '%s' where account = '%s'" 
  try:
    n = dbhelper.execute(sql%(data[KEY.PASSWORD], data[KEY.ACCOUNT]))
    if n > 0:
      return True
    else:
      return False
  except Exception, e:
      print e
      return False



'''
modify user's password to a new one, but not modify its salt value.
@params include user's account. 
                      new password that encode with salt by md5.
@return true if successfully modify.
           false otherwise.
'''
def modify_password_For_Forget(data):
  if KEY.ACCOUNT not in data or KEY.PASSWORD not in data:
    return False

  sql = "update account set password = '%s' where account = '%s'" 
  try:
    n = dbhelper.execute(sql%(data[KEY.PASSWORD], data[KEY.ACCOUNT]))
    if n > 0:
      return True
    else:
      return False
  except Exception, e:
      print e
      return False
  
  
'''
get user's information, which includes user's name, nickname, gender ...... .
@params include user's id
        option user's phone
@return a json includes user's concrete information.
           None if params error or database query error.
'''
def get_user_information(data):
  if KEY.ID not in data:
    if KEY.PHONE not in data:
      #return None
      #add get information by account
      if KEY.ACCOUNT not in data:
        return None
      else:
        sql = sql = "select * from user where nickname = '%s'"%(data[KEY.ACCOUNT])

    else:
      sql = "select * from user where phone = '%s'"%(data[KEY.PHONE])
  else:
    sql = "select * from user where id = %d"%(data[KEY.ID])
  try:
    res = dbhelper.execute_fetchone(sql)
    if res is None:
      return None
    else:
      user = {}
      user[KEY.ID] = res[0]
      user[KEY.NAME] = res[1]
      user[KEY.NICKNAME] = res[2]
      user[KEY.GENDER] = res[3]
      user[KEY.AGE] = res[4]
      user[KEY.PHONE] = res[5]
      user[KEY.EMAIL] = res[6]
      user[KEY.LOCATION] = res[7]
      user[KEY.LONGITUDE] = float(res[8])
      user[KEY.LATITUDE] = float(res[9])
      user[KEY.OCCUPATION] = res[10]
      user[KEY.REPUTATION] = float(res[11])
      user[KEY.AVATAR] = res[12]
      user[KEY.IDENTITY_ID] = res[13]
      user[KEY.TYPE] = res[14]
      user[KEY.IS_VERIFY] = res[15]

      return user
  except:
    return None


'''
launch a help event by launcher.
@params includes user's id and type of help event.
        help event types:
                         0 represents normal question.
                         1 represents nornal help.
                         2 represents emergency.
       other option params includes content of event, longitude and latitude of event.
@return event_id if successfully launches.
        -1 if fails.
        -2 if lack love_coin
'''
def add_event(data):
	if KEY.TYPE not in data or KEY.ID not in data:
		return -1

	'''先对交易爱心币进行判断（比如用户爱心币是否足够）和存储  
		求救事件不会经行检查爱心币'''
  
	'''while debuging this is canceled'''
	'''
	if data[KEY.TYPE] != 2:
		if KEY.TITLE not in data or not exchange(data):
			return -1
	'''
	sql = "insert into event (launcher, type, time) values (%d, %d, now())"
	event_id = -1
	try:
		event_id = dbhelper.insert(sql%(data[KEY.ID], data[KEY.TYPE]))
		if event_id > 0:
			data[KEY.EVENT_ID] = event_id
			if not update_event(data):
				return -1
		return event_id
	except: 
		return -1


'''
modify information of a help event.
@params  includes event_id, which is id of the event to be modified.
         option params includes: title of event, content of event, longitude and latitude of event, state of event,
         the number of the demand person, the number of the love_coin to paid, the comment of the event.
@return True if successfully modifies.
        False otherwise.
'''
def update_event(data):
  result = True
  if KEY.EVENT_ID not in data:
    return False
  sql = ""
  if KEY.TITLE in data:
    data[KEY.TITLE] = MySQLdb.escape_string(data[KEY.TITLE].encode("utf8"))
    sql = "update event set title = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.TITLE], data[KEY.EVENT_ID]))
      result &= True
    except Exception, e:
      print e
      result &= False

  if KEY.CONTENT in data:
    data[KEY.CONTENT] = MySQLdb.escape_string(data[KEY.CONTENT].encode("utf8"))
    sql = "update event set content = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.CONTENT], data[KEY.EVENT_ID]))
      result &= True
    except Exception, e:
      print e
      result &= False
  
  if KEY.LONGITUDE in data and KEY.LATITUDE in data:
    sql = "update event set longitude = %f, latitude = %f where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.LONGITUDE], data[KEY.LATITUDE], data[KEY.EVENT_ID]))
      result &= True
    except:
      result &= False

  if KEY.STATE in data:
    if data[KEY.STATE] == 0:
      data[KEY.STATE] = 1
    sql = "update event set state = %d where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.STATE], data[KEY.EVENT_ID]))
      if reward(data):
        result &= True
      else:
        result &= False
    except:
      result &= False

  if KEY.DEMAND_NUMBER in data:
    sql = "update event set demand_number = %d where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.DEMAND_NUMBER], data[KEY.EVENT_ID]))
      result &= True
    except Exception, e:
      print e
      result &= False

  if KEY.LOVE_COIN in data:
    sql = "update event set love_coin = %d where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.LOVE_COIN], data[KEY.EVENT_ID]))
      result &= True
    except Exception, e:
      print e
      result &= False

  if KEY.COMMENT in data:
    data[KEY.COMMENT] = MySQLdb.escape_string(data[KEY.COMMENT].encode("utf8"))
    sql = "update event set comment = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.COMMENT], data[KEY.EVENT_ID]))
      result &= True
    except:
      result &= False

  if KEY.LOCATION in data:
    data[KEY.LOCATION] = MySQLdb.escape_string(data[KEY.LOCATION].encode("utf8"))
    sql = "update event set location = '%s' where id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.LOCATION], data[KEY.EVENT_ID]))
      result &= True
    except:
      result &= False

  return result


'''
remove a help event by event launcher.
@params includes user's id, which is remover. Actually, only the launcher can remove his/her event.
                 event's id, which represents the event to be removed.
@return True if successfully removes, or remover is not the launcher, actually nothing happens.
        False if fails.
'''
def remove_event(data):
  if KEY.ID not in data or KEY.EVENT_ID not in data:
    return False
  sql = "delete from event where id = %d and launcher = %d"
  try:
    dbhelper.execute(sql%(data[KEY.EVENT_ID], data[KEY.ID]))
    return True
  except:
    return False


'''
get information of a help event.
@params includes id of the event to get.
@return concrete information of the event:
        event_id, launcher's id and his/her nickname, content, type, time, longitude and latitude, state, number of followers, number of supporters and group points.
        None indicates fail query.
'''
def get_event_information(data):
	if KEY.EVENT_ID not in data:
		return None
	event_info = None
	sql = "select * from event where id = %d"
	try:
		sql_result = dbhelper.execute_fetchone(sql%(data[KEY.EVENT_ID]))
		if sql_result is not None:
			event_info = {}
			event_info[KEY.EVENT_ID] = int(sql_result[0])
			event_info[KEY.LAUNCHER_ID] = int(sql_result[1])
			event_info[KEY.TITLE] = sql_result[2]
			event_info[KEY.CONTENT] = sql_result[3]
			event_info[KEY.TYPE] = sql_result[4]
			event_info[KEY.TIME] = str(sql_result[5])
			event_info[KEY.LAST_TIME] = str(sql_result[6])
			event_info[KEY.LONGITUDE] = float(sql_result[7])
			event_info[KEY.LATITUDE] = float(sql_result[8])
			event_info[KEY.STATE] = sql_result[9]
			event_info[KEY.FOLLOW_NUMBER] = sql_result[10]
			event_info[KEY.SUPPORT_NUMBER] = sql_result[11]
			event_info[KEY.GROUP_PTS] = float(sql_result[12])
			event_info[KEY.DEMAND_NUMBER] = sql_result[13]
			event_info[KEY.LOVE_COIN] = sql_result[14]
			event_info[KEY.COMMENT] = sql_result[15]
			event_info[KEY.LOCATION] = sql_result[16]
			user = {}
			user[KEY.ID] = event_info[KEY.LAUNCHER_ID]
			user = get_user_information(user)
			if user is not None:
				event_info[KEY.LAUNCHER] = user[KEY.NICKNAME]
			if KEY.ID in data and event_info[KEY.TYPE] == 0:
				event_info[KEY.IS_LIKE] = int(is_user_like_event(data))
	except:
		pass
	finally:
		return event_info

'''
get information of a collection of events.
@params includes data, a json that contains user's id and type of events to get.
                 get_event_id_list a method of getting event id list.
@return a array of events. each element is information of an event in json form.
'''
def get_events(data, get_event_id_list, limit=0):
	event_id_list = get_event_id_list(data, limit)
	event_list = []
	for event_id in event_id_list:
                event_info = {}
		event_info[KEY.EVENT_ID] = event_id
		if KEY.ID in data:
			event_info[KEY.ID] = data[KEY.ID]
		event_info = get_event_information(event_info)
		if event_info is not None:
			event_list.append(event_info)
	return event_list

'''
get events that launch by user.
@params includes user's id,
                 option params includes state indicates all events or those starting or ended.
                 type indicates type of events.
                 last_time indicates the last time client update
@return an array of result event ids.
'''
def get_launch_event_list(data, limit=0):
	event_id_list = []
	if KEY.ID not in data:
		return event_id_list
	sql = "select id from event where launcher = %d"%data[KEY.ID]
	if KEY.STATE in data:
		if data[KEY.STATE] >= 0 and data[KEY.STATE] <= 2:
			sql += " and state = %d"%data[KEY.STATE]
	if KEY.TYPE in data:
		if data[KEY.TYPE] >= 0 and data[KEY.TYPE] <= 2:
			sql += " and type = %d"%data[KEY.TYPE]
	if KEY.LAST_TIME in data:
		sql += " and last_time > \"" + data[KEY.LAST_TIME] + "\""
	if KEY.EVENT_ID in data:
		sql += " and id < %d"%data[KEY.EVENT_ID]
	sql += " order by time DESC"
	if limit != 0:
		sql += " limit %d"%limit
	sql_result = dbhelper.execute_fetchall(sql)
	for each_result in sql_result:
		for each_id in each_result:
			event_id_list.append(each_id)

	return event_id_list


'''return the event's datetime object. used to show the records.
'''
def get_event_datetime(data):
  if KEY.EVENT_ID not in data:
    return None
  event_info = None
  sql = "select * from event where id = %d"
  try:
    sql_result = dbhelper.execute_fetchone(sql%(data[KEY.EVENT_ID]))
    if sql_result is not None:
      event_info = {}
      event_info[KEY.TIME] = sql_result[5]
  except:
    pass
  finally:
    return event_info


'''
add a support relation record.
@params includes supporter's id and event's type, event id, launcher_id.
@return -1 if fail,
       otherwise,return the record id.
'''
def add_support_relation(data):
  if KEY.ID not in data or KEY.LAUNCHER_ID not in data or KEY.TYPE not in data or KEY.EVENT_ID not in data:
    return -1

  sql = "insert into support_relation (event_id, supportee, supporter, type, time) values (%d, %d, %d, %d, now())"
  record_id = -1
  try:
    record_id = dbhelper.insert(sql%(data[KEY.EVENT_ID], data[KEY.LAUNCHER_ID], data[KEY.ID], data[KEY.TYPE]))
    if record_id >= 0:
      return record_id
  except Exception, e:
    print e
    return -1
  return -1

'''
remove a support relation record.
@params includes supporter's id and event's type, event id, launcher_id.
@return False if fail,
       otherwise,return True.
'''
def remove_support_relation(data):
  if KEY.ID not in data or KEY.LAUNCHER_ID not in data or KEY.EVENT_ID not in data:
    return -1

  sql = "delete from support_relation where event_id = %d and supportee = %d and supporter = %d"
  record_id = -1
  try:
    dbhelper.execute(sql%(data[KEY.EVENT_ID], data[KEY.LAUNCHER_ID], data[KEY.ID]))
  except:
    return False
  
  return True

'''
get the supporters of some event.
@params includes event id.
@return a list incluing the supporters's id.
'''
def list_support_relation(data):
  if KEY.EVENT_ID not in data:
    return None
  sql = "select supporter from support_relation where event_id = %d"
  try:
    res = dbhelper.execute_fetchall(sql%(data[KEY.EVENT_ID]))
    helper_list = []
    for item in res:
      helper_list.append(item[0])
    return helper_list
  except Exception, e:
    print e
  return None

'''
get user's follow or support events.
@params includes user's id and type of user's state in event.
                 user's state 0 indicates follow, and 1 indicates support.
@return an array of result event ids.
'''
def get_join_event_list(data, limit=0):
	event_id_list = []
	if KEY.ID not in data:
		return event_id_list
	sql = "select event_id from support_relation where supporter = %d"%data[KEY.ID]
	if KEY.TYPE in data:
		if data[KEY.TYPE] == 0 or data[KEY.TYPE] == 1:
			sql += " and type = %d"%data[KEY.TYPE]
	if KEY.EVENT_ID in data:
		sql += " and event_id < %d"%data[KEY.EVENT_ID]
	sql += " order by time DESC"
	if limit != 0:
		sql += " limit %d"%limit
	
	sql_result = dbhelper.execute_fetchall(sql)
	for each_result in sql_result:
		event_id_list.append(each_result[0])
	'''sql_result = dbhelper.execute_fetchall(sql)
	for each_result in sql_result:
		for each_id in each_result:
			event_id_list.append(each_id)'''

	return event_id_list

def get_support_time(data):
  if KEY.ID not in data:
    return None
  res = []
  sql = "select event_id from support_relation where supporter = %d" % data[KEY.ID]
  if KEY.TYPE in data:
    if data[KEY.TYPE] == 1 or data[KEY.TYPE] == 2:
      sql += " and type = %d"%data[KEY.TYPE]
  sql += " order by time DESC"
  sql_result = dbhelper.execute_fetchall(sql)
  for each_result in sql_result:
    tempData = get_event_information({KEY.EVENT_ID: each_result})
    if tempData[KEY.TYPE] == data["event_type"]:
      res.append(tempData[KEY.TIME])

  return res

'''
manage relation of user and event.
@params
@return
'''
def user_event_manage(data):
  if KEY.ID not in data or KEY.EVENT_ID not in data:
    return False
  if KEY.OPERATION not in data:
    return False
  if data[KEY.OPERATION] < 0 or data[KEY.OPERATION] > 2:
    return False
  sql = "select launcher from event where id = %d"
  launcher_id = None
  try:
    sql_result = dbhelper.execute_fetchone(sql%(data[KEY.EVENT_ID]))
    if sql_result is not None:
      launcher_id = sql_result[0]
  except:
    pass
  if launcher_id is None:
    return False
  if data[KEY.OPERATION] == 0:
    sql = "delete from support_relation where event_id = %d and supporter = %d"%(data[KEY.EVENT_ID], data[KEY.ID])
  else:
    sql = "replace into support_relation (event_id, supportee, supporter, type, time) values (%d, %d, %d, %d, now())"%(data[KEY.EVENT_ID], launcher_id, data[KEY.ID], data[KEY.OPERATION])


    event = {}

  try:
    dbhelper.execute(sql)
  except:
    return False

  #
  # trust and reputation compute here.
  #
  return True


'''
add a new comment to a help event or a exist comment.
@params includes event_id, represents comment belongs to which event,
                 author, user's id, author of comment,
                 content, content of comment,
                 parent_author, a author of parent comment
@return new comment id if succeed,
        -1 otherwise.
'''
def add_comment(data):
  
  if KEY.ID not in data or KEY.EVENT_ID not in data:
    return -1
  if KEY.CONTENT not in data:
    return -1
  data[KEY.CONTENT] = MySQLdb.escape_string(data[KEY.CONTENT].encode("utf8"))

  # debug add
  launcherExtraInfo = get_user_extra_information(data[KEY.ID]) 
  if launcherExtraInfo["name"] != None:
      fout = open('static/images/head/' + launcherExtraInfo["name"], 'wb')
      fout.write(launcherExtraInfo["profile"])
      fout.close()
  else:
      launcherExtraInfo["name"] = "default.png"


  #-------debug------------------------------------------------
  commenterAvatar = get_user_information({"id":data[KEY.ID]})
  if commenterAvatar[KEY.IS_VERIFY] == 1:

    launcherExtraInfo["name"] = commenterAvatar[KEY.AVATAR]


  #-----debug-------------------------------------------------


 
  data["launcher_profile"] = launcherExtraInfo["name"]
  #  debug add

  if KEY.PARENT_AUTHOR not in data:
    sql = "insert into comment (event_id, author, content, time) values (%d, %d, '%s', now())"
    sql = sql%(data[KEY.EVENT_ID], data[KEY.ID], data[KEY.CONTENT])
  else:
    sql = "insert into comment (event_id, author, content, time, parent_author) values (%d, %d, '%s', now(), %d)"
    sql = sql%(data[KEY.EVENT_ID], data[KEY.ID], data[KEY.CONTENT], data[KEY.PARENT_AUTHOR])
  try:
    comment_id = dbhelper.insert(sql)
    return comment_id
  except:
    return -1


'''
remove a comment from a help event by author him/her self.
@params includes id, indicates author him/her self.
                 event_id, indicates which event the comment belongs to.
                 comment_id, indicates comment itself.
@return True if delete successfully,
        False if fails.
'''
def remove_comment(data):
  if KEY.ID not in data or KEY.EVENT_ID not in data or KEY.COMMENT_ID not in data:
    return False
  sql = "delete from comment where id = %d and event_id = %d and author = %d"
  try:
    n = dbhelper.execute(sql%(data[KEY.COMMENT_ID], data[KEY.EVENT_ID], data[KEY.ID]))
    if n > 0:
      return True
    else:
      return False
  except:
    return False


'''
get comments of a help event.
@params event_id, id of the help event.
@return a list of comments. each comment contain all detail information.
'''
def get_comments(data):
  #data是一个字典，里面 存放的是
  #单个事件的事件id 注意每次总是传入一个事件id
  #成员运算符 in   not in 标识元素符 is   not is 
  if KEY.EVENT_ID not in data:
    return None
  comment_list = []
  comment = {}
  sql = "select id from comment where event_id = %d order by time DESC"
  try:
    sql_result = dbhelper.execute_fetchall(sql%(data[KEY.EVENT_ID]))

    for each_result in sql_result:
   
      for each_id in each_result:

        comment = {}
        comment[KEY.COMMENT_ID] = each_id
        comment = get_comment_info(comment)
        if comment is not None:
          comment_list.append(comment)
    return comment_list
  except:
    return None
'''
get comment's time by user's id
reutrn value: a list.
'''

def get_comment_by_id(data):
  if KEY.ID not in data:
    return None

  sql = "select time from comment where author = %d order by time DESC"
  res = []
  try:
    sql_result = dbhelper.execute_fetchall(sql%(data[KEY.ID]))
    for item in sql_result:
      res.append(item[0])
    return res
  except:
    return None


'''
get detail information of a comment.
@params includes comment_id, id of comment.
@return information of comment, includes id of comment,
                                         event_id, indicates which event belongs to,
                                         author_id, author's user id,
                                         author, nickname of author,
                                         content, main body of comment,
                                         time, add time of comment.
        None indicates a fail query. Maybe the chosen comment doesn't exist.
'''
def get_comment_info(data):
  if KEY.COMMENT_ID not in data:
    return None
  sql = "select event_id, author, content, time, parent_author from comment where id = %d"
  comment_info = None
  try:
    sql_result = dbhelper.execute_fetchone(sql%(data[KEY.COMMENT_ID]))
    if sql_result is not None:
      comment_info = {}
      comment_info[KEY.COMMENT_ID] = data[KEY.COMMENT_ID]
      comment_info[KEY.EVENT_ID] = sql_result[0]
      comment_info[KEY.AUTHOR_ID] = sql_result[1]
      comment_info[KEY.CONTENT] = sql_result[2]
      comment_info[KEY.TIME] = str(sql_result[3])
      comment_info[KEY.PARENT_AUTHOR_ID] = sql_result[4]
      comment_info[KEY.AUTHOR] = None
      comment_info[KEY.PARENT_AUTHOR] = None

      user = {}
      user[KEY.ID] = comment_info[KEY.AUTHOR_ID]
      user = get_user_information(user)
      if user is not None:
        comment_info[KEY.AUTHOR] = user[KEY.NICKNAME]
      user = {}
      user[KEY.ID] = comment_info[KEY.PARENT_AUTHOR_ID]
      user = get_user_information(user)
      if user is not None:
        comment_info[KEY.PARENT_AUTHOR] = user[KEY.NICKNAME]
  except:
    pass
  finally:
    return comment_info


'''
add a static relation between two users. The relation is single direction.
@params includes two users' id, one is called id, the other called user_id.
parameter type indicates type of static relation. two users in one direction could only have one type of relation.
                 type:  0 indicates family relation.
                        1 indicates geography relation.
                        2 indicates career, interest and general friend relation.
@return True if successfully adds.
        False otherwise.
'''
def add_static_relation(data):
	if KEY.ID not in data or KEY.USER_ID not in data or KEY.TYPE not in data:
		return False
	if get_static_relation_status(data[KEY.ID], data[KEY.USER_ID]) == STATUS.AGREE:
		return False
	sql = ""
	if KEY.ALIAS in data:
		data[KEY.ALIAS] = MySQLdb.escape_string(data[KEY.ALIAS].encode("utf8"))
		sql = "replace into static_relation (user_a, user_b, type, time, alias, status) values (%d, %d, %d, now(), '%s', %d)"
	else:
		sql = "replace into static_relation (user_a, user_b, type, time, status) values (%d, %d, %d, now(), %d)"
	try:
		n = 0
		if KEY.ALIAS in data:
			n = dbhelper.execute(sql%(data[KEY.ID], data[KEY.USER_ID], data[KEY.TYPE], data[KEY.ALIAS], STATUS.WAITING))
                        dbhelper.execute(sql%(data[KEY.USER_ID], data[KEY.ID], data[KEY.TYPE], data[KEY.ALIAS], STATUS.WAITING))
		else:
			n = dbhelper.execute(sql%(data[KEY.ID], data[KEY.USER_ID], data[KEY.TYPE], STATUS.WAITING))
                        dbhelper.execute(sql%(data[KEY.USER_ID], data[KEY.ID], data[KEY.TYPE], STATUS.WAITING))
		if n > 0:
			return True
		else:
			return False
	except:
		return False

'''
remove a static relation of two user.
@params includes two users' id, one is called id, the other called user_id.
@return True if successfully removes.
        False otherwise.
'''
def remove_static_relation(data):
	if KEY.ID not in data or KEY.USER_ID not in data:
		return False
	if get_static_relation_status(data[KEY.ID], data[KEY.USER_ID]) != STATUS.AGREE:
		return False
	sql = "update static_relation set status = %d where user_a = %d and user_b = %d"
	try:
		n = dbhelper.execute(sql%(STATUS.REFUSE, data[KEY.ID], data[KEY.USER_ID]))
		if n > 0:
			return True
		else:
			return False
	except:
		return False

'''
handle static relation request, including agree and refuse.
@params includes user's id and target user's id.
                            operation, type of operation, 0 means refuse and 1 means agree.
@return True if succeed.
               False otherwise.
'''
def handle_static_relation(data):
	if KEY.ID not in data or KEY.USER_ID not in data or KEY.OPERATION not in data:
		return False
	if get_static_relation_status(data[KEY.USER_ID], data[KEY.ID]) != STATUS.WAITING:
		return False
	if data[KEY.OPERATION] == STATUS.AGREE or data[KEY.OPERATION] == STATUS.REFUSE:
		sql = "update static_relation set status = %d where user_a = %d and user_b = %d"
		try:
			n = dbhelper.execute(sql%(data[KEY.OPERATION], data[KEY.USER_ID], data[KEY.ID]))
      #dbhelper.execute(sql%(data[KEY.OPERATION], data[KEY.ID], data[KEY.USER_ID]))
			if n > 0:
				return True
			else:
				return False
		except:
			return False
	else:
		return False


'''
update static relation request, including type of relation.
@params includes user's id and target user's id.
                            type of relation.
@return True if succeed.
               False otherwise.
'''
def update_static_relation(data):
  if KEY.ID not in data or KEY.USER_ID not in data or KEY.TYPE not in data:
    return False

  if get_static_relation_status(data[KEY.ID], data[KEY.USER_ID]) != STATUS.AGREE:
    return False

  sql = "update static_relation set type = %d where user_a = %d and user_b = %d"
  try:
    n = dbhelper.execute(sql%(data[KEY.TYPE], data[KEY.ID], data[KEY.USER_ID]))
    print n
    if n > 0:
      return True
    else:
      return False
  except:
    return False




		
'''
query the status of static relation between two indicated user.
@params includes userA's id and userB's id.
@return the status of two user, or None if they haven't built static relation yet.
'''
def get_static_relation_status(userA, userB):
	sql = "select status from static_relation where user_a = %d and user_b = %d"
	try:
		result = dbhelper.execute_fetchone(sql%(userA, userB))
		if result is not None:
			return result[0]
		else:
			return None
	except:
		return None

'''
give an evaluation to a user in a help event.
@params includes: id, evaluater.
                  user_id, evaluatee.
                  event_id, indicates the help event.
                  value, the value of evaluation.
@return True if successfully evaluate.
        Flase otherwise.
'''
def evaluate_user(data):
  if KEY.ID not in data or KEY.USER_ID not in data or KEY.EVENT_ID not in data:
    return False
  if KEY.VALUE not in data:
    return False

  '''from different dimention to evaluate someone'''
  '''value_list = ast.literal_eval(data[KEY.VALUE])
  value = 0.0
  for each_value in value_list:
    value += each_value
  list_len = len(value_list)
  if list_len == 0:
    list_len = 1
  value /= list_len'''

  sql = "replace into evaluation (event_id, from, to, value, time) values (%d, %d, %d, %f, now())"
  try:
    dbhelper.execute(sql%(data[KEY.EVENT_ID], data[KEY.ID], data[KEY.USER_ID], data[KEY.VALUE]))
    return True
  except:
    return False


'''
add a health record of a user into database.
@params includes id, user's id.
                 height, user's height.
                 weight, user's weight.
                 blood_type, user's blood type.
                 medicine_taken, medicine user used to have
                 medical_history, user's medical chart
                 anaphylaxis, user's allergic reaction
@return the health record id of the new record.
        -1 indicates fail.
'''
def health_record(data):
  if KEY.ID not in data:
    return -1
  sql = "insert into health (user_id, time) values (%d, now())"%data[KEY.ID]
  record_id = -1
  try:
    record_id = dbhelper.insert(sql)
    if record_id > 0:
      if not update_health_record(data):
        return -1
    return record_id
  except:
    record_id = -1
  finally:
    return record_id


'''
get details of one certain health record.
@params includes user_id, id of the user.
@return details of the health record, contains record id, user id, type, certain value and record time.
        None indicates fail query.
'''
def get_health_record(user_id):
  sql = "select * from health where user_id = %d"
  record = None
  try:
    sql_result = dbhelper.execute_fetchone(sql%(user_id))
    if sql_result is not None:
      record = {}
      record[KEY.HEALTH_ID] = sql_result[0]
      record[KEY.USER_ID] = sql_result[1]
      record[KEY.HEIGHT] = sql_result[2]
      record[KEY.WEIGHT] = sql_result[3]
      record[KEY.BLOOD_TYPE] = sql_result[4]
      record[KEY.MEDICINE_TAKEN] = sql_result[5]
      record[KEY.MEDICAL_HISTORY] = sql_result[6]
      record[KEY.ANAPHYLAXIS] = sql_result[7]
  except:
    record = None
  finally:
    return record


'''
---------------------change the database & this method is not used-----------------------
get all health records of a user, but at most 100 records.
@params includes id, user's id.
@return a list that contain all health records. each element is a json that contains details information of a health record.
        None indicates fail query.
def get_health_records(data):
  if KEY.ID not in data:
    return None
  sql = "select id from health where user_id = %d order by time DESC limit %d"
  sql_result = None
  try:
    sql_result = dbhelper.execute_fetchall(sql%(data[KEY.ID], 100))
  except:
    sql_result = None
  records = None
  if sql_result is not None:
    records = []
    for each_result in sql_result:
      for each_id in each_result:
        a_record = get_health_record(each_id)
        if a_record is not None:
          records.append(a_record)
  return records
-----------------------------------------------------------------------------------------
'''


'''
add an illness record of a user into database.
@params includes id, user's id.
                 content, illness detail information.
@return illness record id.
        -1 indicates fail.
'''
def illness_record(data):
  if KEY.ID not in data or KEY.CONTENT not in data:
    return -1
  sql = "insert into illness (user_id, content, time) values (%d, '%s', now())"
  illness_id = -1
  try:
    illness_id = dbhelper.insert(sql%(data[KEY.ID], data[KEY.CONTENT]))
  except:
    illness_id = -1
  finally:
    return illness_id


'''
get details of an illness record.
@params includes record id, indicates which record to be queried.
@return content of an illness record, includes record's id, user's id, illness content and illness time.
        None indicates fail query or no such record.
'''
def get_illness_record(record_id):
  sql = "select id, user_id, content, time from illness where id = %d"
  record = None
  try:
    sql_result = dbhelper.execute_fetchone(sql%(record_id))
    if sql_result is not None:
      record = {}
      record[KEY.ILLNESS_ID] = sql_result[0]
      record[KEY.USER_ID] = sql_result[1]
      record[KEY.CONTENT] = sql_result[2]
      record[KEY.TIME] = str(sql_result[3])
  except:
    record = None
  finally:
    return record


'''
get all illness records of a user, but at most 100 records.
@params includes: id, user's id.
@return a list that contain all illness records. each element in the list is a json that is consist of details of an illness record.
        None indicates fail query.
'''
def get_illness_records(data):
  if KEY.ID not in data:
    return None
  sql = "select id from illness where user_id = %d order by time ASC limit %d"
  sql_result = None
  records = None
  try:
    sql_result = dbhelper.execute_fetchall(sql%(data[KEY.ID], 100))
  except:
    sql_result = None
  if sql_result is not None:
    records = []
    for each_result in sql_result:
      for each_id in each_result:
        a_record = get_illness_record(each_id)
        if a_record is not None:
          records.append(a_record)
  return records

'''
create a loving bank account. It contains loving bank and credit.
@params includes user_id, user's id, initial coin number and initial score value.
@return new bank account id if succeed.
        -1 if fail.
'''
def create_loving_bank(data, init_coin=30, init_score=0):
  if KEY.ID not in data:
    return -1
  sql = "insert into loving_bank (userid, love_coin, score_rank, score_exchange, family_love_coin) values (%d, %d, %d, %d, %d)"
  try:
    bank_account_id = dbhelper.insert(sql%(data[KEY.ID], init_coin, init_score, init_score, init_coin))
    return bank_account_id
  except:
    return -1


'''
user could sign in once a day. Especially, if user has signed in today, this method would return false.
@params includes user_id. user's id.
@return True if sign in successfully.
        False otherwise.
'''
def sign_in(data):
  if KEY.ID not in data:
    return False
  user_id = data[KEY.ID]
  if is_sign_in(user_id):
    return False
  sql = "insert into sign_in (user_id, time) values (%d, now())"
  try:
    sign_in_id = dbhelper.insert(sql%(data[KEY.ID]))
    if sign_in_id > 0:
      add_score = {}
      add_score[KEY.ID] = user_id
      add_score[KEY.OPERATION] = 0
      add_score[KEY.LOVE_COIN] = 0
      add_score[KEY.SCORE] = 100
      if update_loving_bank(add_score):
        return True
      else:
        return False
    else:
      return False
  except:
    return False


'''
check whether a user has signed in today.
@params includes user_id. user's id.
@return True if user has signed in.
        False otherwise.
'''
def is_sign_in(user_id):
  result = False
  date_format = "\%Y-\%M-\%D \%H:\%i"
  sql = "select count(*) from sign_in where user_id = %d and to_days(time) = to_days(now())"%(user_id)
  # sql = "select count(*) from sign_in where user_id = %d and date_format(time, '%s') = date_format(now(), '%s')"%(user_id, date_format, date_format)
  try:
    sql_result = dbhelper.execute_fetchone(sql)[0]
    if sql_result > 0:
      result = True
    else:
      result = False
  except:
    result = False
  finally:
    return result


'''
get nearby user's account.
@param includes: user's longitude and latitude
@return a list about user's account
'''
def get_nearby_people(data):
  neighbor_uid_list = []
  if KEY.LONGITUDE not in data or KEY.LATITUDE not in data:
    return neighbor_uid_list
  DISTANCE = 25.0 # 25000m
  location_range = haversine.get_range(data[KEY.LONGITUDE], data[KEY.LATITUDE], DISTANCE)
  sql = "select nickname from user where " \
        "longitude > %f and longitude < %f " \
        "and latitude > %f and latitude < %f"
  sql_result = dbhelper.execute_fetchall(
    sql%(location_range[0], location_range[1], location_range[2], location_range[3]))
  for item in sql_result:
    neighbor_uid_list.append(item[0])
  return neighbor_uid_list

'''
get user's neighbors
@param includes: user_id, user's id
       options:  type, in data, indicates get a list of all user's information
                       not in data, get the identity ids list
@return
'''
def get_neighbor(data):
  neighbor_uid_list = []
  if KEY.ID not in data:
    return neighbor_uid_list
  user = get_user_information(data)
  if user is None:
    return neighbor_uid_list
  DISTANCE = 25.0 # 25000m
  location_range = haversine.get_range(user[KEY.LONGITUDE], user[KEY.LATITUDE], DISTANCE)
  sql = "select id from user where " \
        "longitude > %f and longitude < %f " \
        "and latitude > %f and latitude < %f"
  sql_result = dbhelper.execute_fetchall(
    sql%(location_range[0], location_range[1], location_range[2], location_range[3]))

  if KEY.TYPE in data:
    for each_result in sql_result:
      user = {}
      user[KEY.ID] = each_result[0]
      user = get_user_information(user)
      if user is not None:
        neighbor_uid_list.append(user)
  else:
    for each_result in sql_result:
      user = {}
      user[KEY.ID] = each_result[0]
      user = get_user_information(user)
      if user is not None:
        neighbor_uid_list.append(user[KEY.IDENTITY_ID])
  return neighbor_uid_list

'''
get help_events happend around the user
@param include event id
 option params includes state indicates all events or those starting or ended.
                        type indicates type of events.
                        state indicates state of events.
                        last_time indicates the last time client update.
@return a list of event
'''
def get_nearby_event(data):
  nearby_event_list = []
  if KEY.ID not in data:
    return nearby_event_list
  user = get_user_information(data)
  DISTANCE = 25.0 # 25000m
  location_range = haversine.get_range(user[KEY.LONGITUDE], user[KEY.LATITUDE], DISTANCE)
  sql = "select id from event where " \
        "longitude > %f and longitude < %f " \
        "and latitude > %f and latitude < %f"\
        %(location_range[0], location_range[1], location_range[2], location_range[3])
  if KEY.TYPE in data:
    sql += " and type = %d"%data[KEY.TYPE]
  if KEY.STATE in data:
    sql += " and state = %d"%data[KEY.STATE]

    #sql是可以根据字符串比较大小的 而且sql语句中 字符串填补都需要用
    # '%s'
  if KEY.LAST_TIME in data:
    sql += " and last_time > '%s'"%data[KEY.LAST_TIME]
  sql += " order by time DESC"
  sql_result = dbhelper.execute_fetchall(sql)
  for each_result in sql_result:
    for each_id in each_result:
      nearby_event_list.append(each_id)
  return nearby_event_list


'''
get help_events happend around the user
@param include the user's latitude and longitude
 option params includes state indicates all events or those starting or ended.
                        type indicates type of events.
                        state indicates state of events.
                        last_time indicates the last time client update.
@return a list of event
'''
def get_nearby_event_by_location(data, limit=0):
	nearby_event_list = []
	if KEY.LONGITUDE not in data or KEY.LATITUDE not in data:
		return nearby_event_list

	DISTANCE = 25.0 # 25000m
	location_range = haversine.get_range(data[KEY.LONGITUDE], data[KEY.LATITUDE], DISTANCE)
	sql = "select id from event where " \
			"longitude > %f and longitude < %f " \
			"and latitude > %f and latitude < %f"\
			%(location_range[0], location_range[1], location_range[2], location_range[3])
	'''if KEY.TYPE in data:
		sql += " and type = %d"%data[KEY.TYPE]'''
	sql += " and type != 0"
	if KEY.STATE in data:
		sql += " and state = %d"%data[KEY.STATE]

    #sql是可以根据字符串比较大小的 而且sql语句中 字符串填补都需要用
    # '%s'
	if KEY.LAST_TIME in data:
		sql += " and last_time > '%s'"%data[KEY.LAST_TIME]
	if KEY.EVENT_ID in data:
		sql += " and id < %d"%data[KEY.EVENT_ID]
	sql += " order by time DESC"
	if limit != 0:
		sql += " limit %d"%limit
	sql_result = dbhelper.execute_fetchall(sql)
	for each_result in sql_result:
		nearby_event_list.append(each_result[0])
	return nearby_event_list

'''
get information about loving_bank得到用户关于爱心银行账户信息
@param user_id, user's id
@return user's love coin and score，family love coin
'''
def get_user_loving_bank(data):
  if KEY.USER_ID not in data:
    return None
  sql = "select score_rank, love_coin, family_love_coin from loving_bank where userid = %d"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.USER_ID]))
    if res is None:
      return None
    else:
      bank_info = {}
      bank_info[KEY.ID] = data[KEY.USER_ID]
      bank_info[KEY.SCORE] = res[0]
      bank_info[KEY.LOVE_COIN] = res[1]
      bank_info[KEY.FAMILY_LOVE_COIN] = res[2]
      return bank_info
  except:
    return None

'''
add an answer to a question
@param  data contains author_id, event_id, content
@return answer_id if successfully adds
    -1 is fails.
'''
def add_answer(data):
	if KEY.ID not in data or KEY.EVENT_ID not in data or KEY.CONTENT not in data:
		return -1
	data[KEY.CONTENT] = MySQLdb.escape_string(data[KEY.CONTENT].encode("utf8"))
	sql_insert = "insert into answer (event_id, author_id, content) values (%d, %d, '%s')"
	sql_update = "update event set support_number = support_number + 1 where id = %d and type = %d and state = %d"
	answer_id = -1
	try:
		answer_id = dbhelper.insert(sql_insert%(data[KEY.EVENT_ID], data[KEY.ID], data[KEY.CONTENT]))
		n = dbhelper.execute(sql_update%(data[KEY.EVENT_ID], 0, 0))
		if n <= 0:
			update_answer({KEY.ANSWER_ID: answer_id, KEY.EVENT_ID: data[KEY.EVENT_ID], KEY.VALID: 0})
			answer_id = -1
	except:
		pass
	finally:
		return answer_id

'''
update information about an answer
@param
@return
'''
def update_answer(data):
	if KEY.ANSWER_ID not in data:
		return False

	result = True
	sql = ""
	if KEY.IS_ADOPTED in data:
		sql = "update answer set is_adopted = %d where id = %d"
		try:
			dbhelper.execute(sql%(data[KEY.IS_ADOPTED], data[KEY.ANSWER_ID]))
			result &= True
			
			event = {}
			event[KEY.ID] = author_id
			event[KEY.EVENT_ID] = event_id
			event[KEY.STATE] = 2
			result &= update_event(event)
		except:
			result &= False
	if KEY.LIKING_NUM in data:
		sql = "update answer set liking_num = %d where id = %d"
		try:
			dbhelper.execute(sql%(data[KEY.LIKING_NUM], data[KEY.ANSWER_ID]))
			result &= True
		except:
			result &= False
	if KEY.VALID in data and KEY.EVENT_ID in data:
		sql_answer = "update answer set valid = %d where id = %d and valid = %d"      # delete answer
		sql_event = "update event set support_number = support_number - 1 where id = %d and type = %d"
		try:
			n = dbhelper.execute(sql_answer%(0, data[KEY.ANSWER_ID], 1))
			if n > 0:
				dbhelper.execute(sql_event%(data[KEY.EVENT_ID], 0))
				result &= True
			else:
				result &= False
		except:
			result &= False
		
	return result
  
'''
get information about an answer
@param data contains answer_id
@return concrete information about answer
    which contains id, event_id, author_id, content, time, is_adopted, liking_num.
'''
def get_answer_info(data):
	if KEY.ANSWER_ID not in data:
		return None
	answer_info = None
	sql = "select * from answer where id = %d"
	try:
		sql_result = dbhelper.execute_fetchone(sql%(data[KEY.ANSWER_ID]))
		if sql_result is not None:
			answer_info = {}
			answer_info[KEY.ANSWER_ID] = sql_result[0]
			answer_info[KEY.EVENT_ID] = sql_result[1]
			answer_info[KEY.AUTHOR_ID] = sql_result[2]
			answer_info[KEY.CONTENT] = sql_result[3]
			answer_info[KEY.TIME] = str(sql_result[4])
			answer_info[KEY.IS_ADOPTED] = sql_result[5]
			answer_info[KEY.LIKING_NUM] = sql_result[6]
			user = {}
			user[KEY.ID] = answer_info[KEY.AUTHOR_ID]
			user = get_user_information(user)
			if user is not None:
				answer_info[KEY.AUTHOR] = user[KEY.NICKNAME]
	except:
		pass
	finally:
		return answer_info

'''
get a list of answer of the question
@param include event's id
@return a array of answers. each element is information of an answer
'''
def get_answers(data, get_answerid_list, limit=0):
	answer_id_list = get_answerid_list(data, limit)
	answer_list = []
	answer_info = {}
	for answer_id in answer_id_list:
		answer_info[KEY.ANSWER_ID] = answer_id
		answer_info = get_answer_info(answer_info)
		if answer_info is not None:
			answer_list.append(answer_info)
	return answer_list

'''
get the id list of a question
@param include event's id
@return a list of answer_id about the question
'''
def get_answer_id_list(data, limit=0):
	answer_id_list = []
	if KEY.EVENT_ID not in data:
		return answer_id_list
	sql = "select id from answer where event_id = %d and valid = %d"%(data[KEY.EVENT_ID], 1)
	if KEY.ANSWER_ID in data:
		sql += " and id < %d"%data[KEY.ANSWER_ID]
	sql += " order by id DESC"
	if limit != 0:
		sql += " limit %d"%limit
	sql_result = dbhelper.execute_fetchall(sql)
	for each_result in sql_result:
		for each_id in each_result:
			answer_id_list.append(each_id)

	return answer_id_list

'''
query all the users whom the user follows/follows the user.
@params includes: user's id.
                  type indicates type of static relation. two users in one direction could only have one type of relation.
                  type: 0 indicates family relation.
                        1 indicates geography relation.
                        2 indicates career, interest and general friend relation.
                  state indicates the follow relation.
                  state: 0, query user's followed users
                         1, query user's follower
@return a list contains ids
        -1 if fails
'''
def query_follow(data):
	sql = ""
	if KEY.ID not in data or KEY.STATE not in data:
		return -1
	if data[KEY.STATE] == 0:
		sql = "select user_b, type, alias from static_relation where user_a = %d and status = %d"%(data[KEY.ID], STATUS.AGREE)
	elif data[KEY.STATE] == 1:
		sql = "select user_a, type, alias from static_relation where user_b = %d and status = %d"%(data[KEY.ID], STATUS.AGREE)
	else:
		return -1

	user_list = []
	if KEY.TYPE in data:
		if data[KEY.TYPE] == 0 or data[KEY.TYPE] ==1 or data[KEY.TYPE] == 2:
			sql += " and type = %d"%data[KEY.TYPE]
	sql_result = dbhelper.execute_fetchall(sql)
	resp = {}
	for each_result in sql_result:
		resp[KEY.ID] = each_result[0]
		resp = get_user_information(resp)
		resp[KEY.SUPPORT_NUMBER] = len(get_join_event_list({KEY.ID: resp[KEY.ID]}))
		resp[KEY.RELATION_TYPE] = each_result[1]
		resp[KEY.ALIAS] = each_result[2]
		user_list.append(resp)
	return user_list

'''
get supporters for an event
@param includes event id
       options  type of supporters
@return a list of supporters
'''
def get_supporters(data):
  sup_list = []
  if KEY.EVENT_ID not in data:
    return sup_list
  sql = "select supporter from support_relation where event_id = %d"%data[KEY.EVENT_ID]
  if KEY.TYPE in data:
    sql += " and type = %d"%data[KEY.TYPE]
  sql_result = dbhelper.execute_fetchall(sql)
  resp = {}
  for each_result in sql_result:
    for each_id in each_result:
      resp[KEY.ID] = each_id
      resp = get_user_information(resp)
      sup_list.append(resp)
  return sup_list

'''
modify information of a health record.
@params  includes: id, user's id.
         options:  height, weight, blood_type,
                   medicine_taken, medical_history, anaphylaxis
@return True if successfully modifies.
        False otherwise.
'''
def update_health_record(data):
  result = True
  if KEY.ID not in data:
    return False
  sql = ""

  if KEY.HEIGHT in data:
    sql = "update health set height = %d where user_id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.HEIGHT], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.WEIGHT in data:
    sql = "update health set weight = %d where user_id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.WEIGHT], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.BLOOD_TYPE in data:
    data[KEY.BLOOD_TYPE] = MySQLdb.escape_string(data[KEY.BLOOD_TYPE].encode("utf8"))
    sql = "update health set blood_type = '%s' where user_id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.BLOOD_TYPE], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.MEDICINE_TAKEN in data:
    data[KEY.MEDICINE_TAKEN] = MySQLdb.escape_string(data[KEY.MEDICINE_TAKEN].encode("utf8"))
    sql = "update health set medicine_taken = '%s' where user_id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.MEDICINE_TAKEN], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.MEDICAL_HISTORY in data:
    data[KEY.MEDICAL_HISTORY] = MySQLdb.escape_string(data[KEY.MEDICAL_HISTORY].encode("utf8"))
    sql = "update health set medical_history = '%s' where user_id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.MEDICAL_HISTORY], data[KEY.ID]))
      result &= True
    except:
      result &= False

  if KEY.ANAPHYLAXIS in data:
    data[KEY.ANAPHYLAXIS] = MySQLdb.escape_string(data[KEY.ANAPHYLAXIS].encode("utf8"))
    sql = "update health set anaphylaxis = '%s' where user_id = %d"
    try:
      dbhelper.execute(sql%(data[KEY.ANAPHYLAXIS], data[KEY.ID]))
      result &= True
    except:
      result &= False

  return result

'''
judge the health_card is in database or not.
if it exist in database, update data.
else, insert data.
@param include: id, user's id
       options: height, weight, blood_type,
                medicine_taken, medical_history, anaphylaxis
@return True if insert or update successfully
        False if fail
'''
def upload_health(data):
  if KEY.ID not in data:
    return False
  sql = "select * from health where user_id = %d"%data[KEY.ID]
  res = dbhelper.execute_fetchone(sql)
  if res is not None:
    return update_health_record(data)
  else:
    if health_record(data) > 0:
      return True
  return False

'''
update information of user's loving bank.
@params  includes: id, user's id.
                   operation, 0 indicates add love_coin & score
                              1 indicates minus love_coin & score
                              //2 indicates transform score to love_coin
                   love_coin, the number of love_coin to add/minus
                   score, the score number to add/minus
                   (the switch score must be the multiple of 100)
@return True if successfully update.
        False otherwise.
'''
def update_loving_bank(data):
  if KEY.ID not in data or KEY.OPERATION not in data:
    return False
  if KEY.LOVE_COIN not in data or KEY.SCORE not in data:
    return False

  user = {}
  user[KEY.USER_ID] = data[KEY.ID]
  bank_info = get_user_loving_bank(user)
  if bank_info is None:
    return False

  '''
  exchange_rate = 0.01
  if data[KEY.OPERATION] == 0:
    update_love_coin = bank_info[KEY.LOVE_COIN] + data[KEY.LOVE_COIN]
    update_score = bank_info[KEY.SCORE] + data[KEY.SCORE]
  elif data[KEY.OPERATION] == 1:
    update_love_coin = bank_info[KEY.LOVE_COIN] - data[KEY.LOVE_COIN]
    update_score = bank_info[KEY.SCORE] - data[KEY.SCORE]
  elif data[KEY.OPERATION] == 2:
    if data[KEY.SCORE] % 100 != 0:
      return False
    update_love_coin = bank_info[KEY.LOVE_COIN] + data[KEY.SCORE] * exchange_rate
    update_score = bank_info[KEY.SCORE] - data[KEY.SCORE]
  '''

  #还没有绑定成员的接口，故暂时不用家庭账户来付款，等绑定模块完成再添加。
  if data[KEY.OPERATION] == 0:
    update_love_coin = bank_info[KEY.LOVE_COIN] + data[KEY.LOVE_COIN]
    update_score = bank_info[KEY.SCORE] + data[KEY.SCORE]
  elif data[KEY.OPERATION] == 1:
    update_love_coin = bank_info[KEY.LOVE_COIN] - data[KEY.LOVE_COIN]
    update_score = bank_info[KEY.SCORE] - data[KEY.SCORE]
  else:
    return False


  if update_love_coin < 0 or update_score < 0:
    return False

  sql = "update loving_bank set love_coin = %d, score_rank = %d where userid = %d"
  try:
    dbhelper.execute(sql%(update_love_coin, update_score, data[KEY.ID]))
    return True
  except:
    return False

'''
user_A transfer the love_coin to user_B
@param includes: sender: user_A's id, who want to transfer the love_coin
                 receiver: user_B's id, who receives the transferred love_coin
                 love_coin: the number of love_coin which would be transferred
@return True if transfer successfully
        False if fails
'''
def love_coin_transfer(data):
  if KEY.SENDER not in data or KEY.RECEIVER not in data:
    return False
  if KEY.LOVE_COIN not in data:
    return False

  sender = {}
  receiver = {}
  sender[KEY.USER_ID] = data[KEY.SENDER]
  receiver[KEY.USER_ID] = data[KEY.RECEIVER]
  sender = get_user_loving_bank(sender)
  receiver = get_user_loving_bank(receiver)

  if sender is None or receiver is None:
    return False
  update_sender_coin = sender[KEY.LOVE_COIN] - data[KEY.LOVE_COIN]
  update_receiver_coin = receiver[KEY.LOVE_COIN] + data[KEY.LOVE_COIN]

  if update_sender_coin < 0 or update_receiver_coin < 0:
    return False

  sql = "update loving_bank set love_coin = %d where userid = %d"
  history_sql = "insert into coin_exchange (sender, receiver, time, lovecoin) values (%d, %d, now(), %d)"
  try:
    dbhelper.execute(sql%(update_sender_coin, data[KEY.SENDER]))
    dbhelper.execute(sql%(update_receiver_coin, data[KEY.RECEIVER]))
    dbhelper.insert(history_sql%(data[KEY.SENDER], data[KEY.RECEIVER], data[KEY.LOVE_COIN]))
    return True
  except Exception, e:
    traceback.print_exc()
    return False


'''
get chat_token of an account.
@params include user's id.
@return chat_token of an account.
        None if account not exists or database query error.
'''
def get_chat_token(data):
  if KEY.ID not in data:
    return None
  sql = "select chat_token from account where id = '%s'"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.ID]))
    if res is None:
      return None
    else:
      return res[0]
  except:
    return None

'''
get the relation between two users(one-sided relation)
@param includes: id, user_a's id
                 user_id, user_b's id
@return 0 indicates families
        2 indicates friends
        -1 query fails
        others indicate no relation
'''
def get_relation(data):
  if KEY.ID not in data or KEY.USER_ID not in data:
    return -1
  sql = "select type from static_relation where user_a = %d and user_b = %d"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.ID], data[KEY.USER_ID]))
    if res is None:
      return -1
    else:
      return res[0]
  except:
    return -1

'''
暂时不会用到
save rewarding love_coin in the exchanged pool
@param includes: id, user's id
                 love_coin, the rewarding love_coin
@return True if saves successfully
        False if fails
''' 
def exchange(data):
  if KEY.ID not in data or KEY.LOVE_COIN not in data:
    return False

  coin_sql = "select love_coin from loving_bank where userid = %d"%data[KEY.ID]
  exchange_sql = "select score_exchange from loving_bank where userid = %d"%data[KEY.ID]
  try:
    coin = dbhelper.execute_fetchone(coin_sql)
    coin_exchange = dbhelper.execute_fetchone(exchange_sql)

    #表示没有收到结果  注意和0区分
    if coin is None or coin_exchange is None:
      return False
    update_love_coin = coin[0] - data[KEY.LOVE_COIN]
    update_exchange_coin = coin_exchange[0] + data[KEY.LOVE_COIN]
    if update_love_coin < 0:
      return False

    update_sql = "update loving_bank set love_coin = %d, score_exchange = %d where userid = %d"
    dbhelper.execute(update_sql%(update_love_coin, update_exchange_coin, data[KEY.ID]))
  except Exception, e:
    print e
    return False

'''
记录爱心币转移的情况
get a history record of a transfer
@param id, transfer_record's id
@return record information
        None if fails
'''
def get_transfer(data):
  record_info = None
  if KEY.ID not in data:
    return record_info
  sql = "select * from coin_exchange where id = %d"
  try:
    sql_result = dbhelper.execute_fetchone(sql%(data[KEY.ID]))
    print sql_result
    if sql_result is not None:
      record_info = {}
      record_info[KEY.ID] = sql_result[0]
      record_info[KEY.SENDER] = sql_result[1]
      record_info[KEY.RECEIVER] = sql_result[2]
      record_info[KEY.LOVE_COIN] = sql_result[3]
      record_info[KEY.TIME] = str(sql_result[4])
    return record_info
  except:
    return None

'''
查询爱心币转送或者接送的记录，返还一个list装着每个字典序
check the history of the transfer
@param  id, user's id
        type, 0 indicates send coins
              1 indicates receive coins
@return h_list, a list of transfer history
        -1 if query fails
'''
def check_transfer(data):
  if KEY.ID not in data or KEY.TYPE not in data:
    return -1
  sql = ""
  if data[KEY.TYPE] == 0:
    sql = "select id from coin_exchange where sender = %d"%data[KEY.ID]
  elif data[KEY.TYPE] == 1:
    sql = "select id from coin_exchange where receiver = %d"%data[KEY.ID]
  else:
    return -1
  sql += " order by time DESC"
  sql_result = dbhelper.execute_fetchall(sql)
  h_list = []
  for each_result in sql_result:
    for each_id in each_result:
      record = {}
      record[KEY.ID] = each_id
      record = get_transfer(record)
      if record is not None:
        h_list.append(record)
  return h_list


'''
reward the love_coin to the supporters when the event stops
@param includes: event_id, event's id
@return True if succeed
        False if fails
'''
def reward(data):
  if KEY.EVENT_ID not in data:
    return False
  event = get_event_information(data)
  if event == None:
    return False
  reward_coin = event[KEY.LOVE_COIN]
  if reward_coin is None:
    return False


  sup_event = {}
  sup_event[KEY.EVENT_ID] = data[KEY.EVENT_ID]
  sup_event[KEY.TYPE] = 2
  supporters = get_supporters(sup_event)
  if supporters is None:
    return False
  num = len(supporters)

  minus_sql = "update loving_bank set love_coin = love_coin - %d where userid = %d"
  #minus_sql = "update loving_bank set score_exchange = score_exchange - %d where userid = %d"
  try:
    userid = event[KEY.LAUNCHER_ID]
    if userid is None:
      return False
    dbhelper.execute(minus_sql%(reward_coin, userid))
  except Exception, e:
    return False

  add_sql = "update loving_bank set love_coin = love_coin + %d where userid = %d"
  history_sql = "insert into coin_trade (eventid, sender, receiver, lovecoin, time) " \
                "values (%d, %d, %d, %d, now())"
  if num == 0:
    try:
      dbhelper.execute(add_sql%(reward_coin, event[KEY.LAUNCHER_ID]))
      dbhelper.insert(history_sql%(data[KEY.EVENT_ID], event[KEY.LAUNCHER_ID], event[KEY.LAUNCHER_ID], reward_coin))
      return True
    except:
      return False
  else:
    # todo If the avg_coin less than 1(which will be zero).
    # 暂时还没考虑评分的高低情况，所以默认都是得到相同的爱心币。
    #avg_coin = reward_coin / num;
    avg_coin = reward_coin
    try:
      for i in range(0, num):
        dbhelper.execute(add_sql%(avg_coin, supporters[i][KEY.ID]))
        dbhelper.insert(history_sql%(data[KEY.EVENT_ID], event[KEY.LAUNCHER_ID], supporters[i][KEY.ID], reward_coin))
      return True
    except Exception, e:
      print e
      return False

'''
get all events by type and state
@param includes: type, the type of events.
                 state, the state of events.
@return id_list, a list of event_id.
        -1 if fails.
'''
def get_all_events(data, limit=0):
	if KEY.TYPE not in data or KEY.STATE not in data:
		return -1
	id_list = []
	sql = "select id from event where type = %d and state = %d"%(data[KEY.TYPE], data[KEY.STATE])
	if KEY.EVENT_ID in data:
		sql += " and id < %d"%data[KEY.EVENT_ID]
	sql += " order by time DESC"
	if limit != 0:
		sql += " limit %d"%limit
	sql_result = dbhelper.execute_fetchall(sql)
	for each_result in sql_result:
		for each_id in each_result:
			id_list.append(each_id)
	return id_list

'''
get the history of coin trade
@param includes: sender, get the history as sender
                 receiver, get the history as receiver
@return h_list, a list of the history of coin trade
        -1, if fails
'''
def get_trade(data):
  if KEY.SENDER not in data and KEY.RECEIVER not in data:
    return -1
  sql = "select * from coin_trade where"
  if KEY.SENDER in data and KEY.RECEIVER in data:
    sql += " sender = %d or receiver = %d"%(data[KEY.SENDER], data[KEY.RECEIVER])
  elif KEY.SENDER in data:
    sql += " sender = %d"%data[KEY.SENDER]
  elif KEY.RECEIVER in data:
    sql += " receiver = %d"%data[KEY.RECEIVER]
  sql += " order by time DESC"
  
  h_list = []
  sql_result = dbhelper.execute_fetchall(sql)
  for each_result in sql_result:
    history = {}
    history[KEY.EVENT_ID] = each_result[1]
    history[KEY.SENDER] = each_result[2]
    history[KEY.RECEIVER] = each_result[3]
    history[KEY.LOVE_COIN] = each_result[4]
    history[KEY.TIME] = str(each_result[5])
    h_list.append(history)
  return h_list

'''
judge someone is the supporter of the event or not
@param id, user's id
       event_id, event's id
@return 0, indicates no relation
        1, indicates follow
        2, indicates supporter
        -1, if fails
'''
def judge_sup(data):
  if KEY.ID not in data or KEY.EVENT_ID not in data:
    return -1
  sql = "select type from support_relation where supporter = %d and event_id = %d"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.ID], data[KEY.EVENT_ID]))
    if res is None:
      return 0
    return res[0]
  except Exception, e:
    print e
    return -1

'''the next part is added by younglee for the web terminal
'''

'''
add a new account to database.
@params a dict data:
        includes account and password.
@return -1 indicates params are not complete. Or account is not unique that leads to database fails.
        other number indicates success and the number is the id of the new account.
'''
def web_add_account(data):
  if KEY.ACCOUNT not in data or KEY.PASSWORD not in data:
    return -1
  
  if KEY.PHONE not in data or KEY.EMAIL not in data:
    return -1

  salt = ''.join(random.sample(string.ascii_letters, 8))
  md5_encode = hashlib.md5()
  md5_encode.update(data[KEY.PASSWORD]+salt)
  password = md5_encode.hexdigest()

  sql_account = "insert into account (account, password, salt) values ('%s', '%s', '%s')"
  sql_user = "insert into user (id, nickname, phone, email) values (%d, '%s', '%s', '%s')"
  sql_user_extra = "insert into user_extension (userId) values (%d)"
  try:
    insert_id = dbhelper.insert(sql_account%(data[KEY.ACCOUNT], password, salt))
    dbhelper.insert(sql_user%(insert_id, data[KEY.ACCOUNT], data[KEY.PHONE], data[KEY.EMAIL]))
    dbhelper.insert(sql_user_extra%(insert_id))
    chat_token = getToken.getToken(insert_id, None, None)
    sql_chat = "update account set chat_token = '%s' where id = %d"
    dbhelper.execute(sql_chat%(chat_token, insert_id))
    return insert_id
  except Exception, e:
    print e
    return -1

'''get user's info by id
'''

def get_userName(data):
	if KEY.ID not in data:
		return None

	sql = "select nickname from user where id = %d"%(data[KEY.ID])
	try:
		res = dbhelper.execute_fetchone(sql)
		return res
	except:
		return None

'''
when user registers in our website, we need to confirm the uniqueness of account
@params include user's account
@return a number: 0 if it is unique
                  > 0 if it is not unique
'''

def isAccountHasExist(data):
  if KEY.ACCOUNT not in data:
    return None
  sql = "select account from account where account = '%s'" % (data[KEY.ACCOUNT])
  try:
    res = dbhelper.execute_fetchall(sql)
    return len(res)

  except Exception, e:
    print e
    return None

'''
get the extra information about the user, such as: checkIn, profile, concernNum and so on
@params include user's id
@return a dict
'''

#这个额外的信息是用来存储使用者的头像等信息的
#profile里面装的是使用者的图片二进制文件 它的类型为mediumblob
#name的意思是图片的名字
def get_user_extra_information(data):
  sql = "select * from user_extension where userId = %d" % (data)
  try:
    res = dbhelper.execute_fetchall(sql)
    res = res[0]
    info = {}
    info["checkIn"] = res[2]
    info["concernNum"] = res[3]
    info["name"] = res[4]
    info["profile"] = res[5]
    return info

  except Exception, e:
    print e
    return None

'''
modify the password
@params include user_id newPassword
@return 1 success -1 fail

'''
def modify_password(data):
    
    if KEY.ACCOUNT not in data or 'newPwd' not in data or KEY.SALT not in data:
        return -1
    sql = "update account set password = '%s' where account = '%s' and salt = '%s'"
    try:
        
        if dbhelper.execute(sql%(data['newPwd'], data[KEY.ACCOUNT], data[KEY.SALT])) > 0:
            return 1
    except:
      return -1


'''
add to email_verify
@params include user_id email
@return 1 success -1 fail

'''    

def add_email_verify(data):

    if KEY.ID not in data or KEY.EMAIL not in data or KEY.IDENCODE not in data:
        return -1
    else:
        sql = "insert into verify_email (id, email, idencode) values (%d, '%s', '%s')"
        try:
            insert_id = dbhelper.insert(sql%(data[KEY.ID], data[KEY.EMAIL], data[KEY.IDENCODE]))
            return insert_id
        except:
            return -1

'''
get latest email_verify
@params include user_id
@return success data info include id and email time
       fail None
''' 

def  get_latest_verify_email(data):

    if KEY.ID not in data:
        return None
    verify_email_info = {}
    sql = "select * from verify_email where id = '%d' order by time DESC"
    try:
        res = dbhelper.execute_fetchone(sql%(data[KEY.ID]))
        verify_email_info[KEY.ID] = res[0]
        verify_email_info[KEY.EMAIL] = res[1]
        verify_email_info[KEY.TIME] = res[2]
        return verify_email_info
    except:
        return None


#--------------------------debug----------------------

'''
get  email_verify by idencode
@params include idencode
@return success data info include id and email time and idencode and time
       fail None
''' 

def  get_verify_email_by_idencode(data):

    if KEY.IDENCODE not in data:
        return None
    verify_email_info = {}
    sql = "select * from verify_email where idencode = '%s' order by time DESC"
    try:
        res = dbhelper.execute_fetchone(sql%(data[KEY.IDENCODE]))
        verify_email_info[KEY.ID] = res[0]
        verify_email_info[KEY.EMAIL] = res[1]
        verify_email_info[KEY.TIME] = res[2]
        verify_email_info[KEY.IDENCODE] = res[3]
        return verify_email_info
    except:
        return None


#--------------------------------


'''
clear_verify_emain_info
@params include user_id
@return success 1
       fail -1
''' 
def clear_verify_email_info(data):

    if KEY.ID not in data:
        return -1
    sql = "delete from verify_email where id = '%d'"
    try:
        dbhelper.execute(sql%(data[KEY.ID]))
        return 1
    except:
        return -1



'''
add to user_verify
@params include user_id name identity_id avatar
@return 1 success -1 fail

'''    

def add_user_verify(data):

    if KEY.ID not in data or KEY.NAME not in data or KEY.IDENTITY_ID not in data or KEY.AVATAR not in data or KEY.IDENCODE not in data or KEY.EMAIL not in data:

        return -1
    else:
        #这里的utf 和 unicode混合在一起 先对含有中文的utf8的字符串进行解码
        #data[KEY.NAME] = MySQLdb.escape_string(data[KEY.NAME].encode("utf8").encode("utf8")
        #由于可能含有中文的params[KEY.NAME]已经是unicode了 所以不需要对其他的utf8(全英的)进行解码

        sql = "insert into verify_user (id, name, identity_id, avatar, status, idencode, email) values (%d, '%s','%s', '%s', 'wait', '%s', '%s')"

        try:
            
            insert_id = dbhelper.insert(sql%(data[KEY.ID], data[KEY.NAME], data[KEY.IDENTITY_ID], data[KEY.AVATAR], data[KEY.IDENCODE], data[KEY.EMAIL]))
            return insert_id
        except Exception, e:
            print e
            return -1



'''
get user_verify
@params include user_id or idencode(only one choose)
@return success data include id status identity_id avatar status and so on
       fail None
''' 

def  get_user_verify_info(data):

    if KEY.ID not in data and KEY.IDENCODE not in data:
        return None
    verify_user_info = {}
    if KEY.ID in data:
      sql = "select * from verify_user where id = %d order by time DESC" %(data[KEY.ID])

    else:
      sql = "select * from verify_user where idencode = '%s' order by time DESC" %(data[KEY.IDENCODE])


    try:
        res = dbhelper.execute_fetchone(sql)
        if len(res) == 0:
          return None
        verify_user_info[KEY.ID] = res[0]
        verify_user_info[KEY.NAME] = res[1]
        verify_user_info[KEY.IDENTITY_ID] = res[2]
        verify_user_info[KEY.AVATAR] = res[3]
        verify_user_info[KEY.STATUS] = res[4]
        verify_user_info[KEY.TIME] = res[5]
        verify_user_info[KEY.IDENCODE] = res[6]
        verify_user_info[KEY.EMAIL] = res[7]
        return verify_user_info
    except:
        return None


'''
clear_verify_user_info
@params include user_id
@return success 1
       fail -1
''' 
def clear_verify_user_info(data):

    if KEY.ID not in data:
        return -1
    sql = "delete from verify_user where id = %d"
    try:
        dbhelper.execute(sql%(data[KEY.ID]))
        return 1
    except:
        return -1

'''
judge a user whether it likes an event.
@params includes user's id and event's id
@return True if it likes.
               False otherwise.
'''
def is_user_like_event(data):
	if KEY.ID not in data or KEY.EVENT_ID not in data:
		return False
	is_like = False
	sql = "select 1 from event_like where user_id = %d and event_id = %d and valid = %d"
	try:
		result = dbhelper.execute_fetchone(sql%(data[KEY.ID], data[KEY.EVENT_ID], 1))
		if result is None:
			is_like = False
		elif result[0] == 1:
			is_like = True
		else:
			is_like = False
	except:
		is_like = False
	finally:
		return is_like
	
'''
user add a like to an event
@params include user’s id, event's id and type of operation.
               operation = 0 means cancel like.
			                   = 1 means add like.
@return True if succeed,
               False otherwise.
'''
def manage_event_like(data):
	if KEY.ID not in data or KEY.EVENT_ID not in data or KEY.OPERATION not in data:
		return False
	try:
		is_like = is_user_like_event(data)
		sql_like = "replace into event_like (user_id, event_id, time, valid) values (%d, %d, now(), %d)"
		if data[KEY.OPERATION] == 0 and is_like is True:
			dbhelper.execute(sql_like%(data[KEY.ID], data[KEY.EVENT_ID], 0))
			sql_event = "update event set follow_number = follow_number - 1 where id = %d and type = %d"
			dbhelper.execute(sql_event%(data[KEY.EVENT_ID], 0))
			return True
		elif data[KEY.OPERATION] == 1 and is_like is False:
			dbhelper.execute(sql_like%(data[KEY.ID], data[KEY.EVENT_ID], 1))
			sql_event = "update event set follow_number = follow_number + 1 where id = %d and type = %d"
			dbhelper.execute(sql_event%(data[KEY.EVENT_ID], 0))
			return True
		else:
			return False
	except Exception, e:
                print e
		return False
