#!/usr/python
# -*- coding: utf-8 -*-

from __future__ import division
import random
import string
import hashlib
import MySQLdb
import ast
import traceback

from dbhelper import dbhelper
from utils import KEY
from utils import STATUS
from utils import VALUE
from database import db


def modify_reward_factor(data):
	VALUE.reward_factor = VALUE.reward_factor*1.0 / data																		
	

def modify_default_coin(data):
	VALUE.default_coin = data

'''
	设置求救事件的默认币值
'''
def set_emergence_event_default_lovecoin():

	return VALUE.default_coin 

'''
	每次用户登录即插入数据，方便为统计用户的登录情况
	参数： 用户的id
	返回： 插入成功即返回True，否则返回False 
'''
def record_login(data):
	if KEY.ID not in data: 
		return False

	sql = "insert into sign_in (user_id, time) values (%d, now())"
	result = -1

	try:
		result = dbhelper.insert(sql%(data[KEY.ID]))
		if result > 0:
			return True
		else:
			return False
	except:
		return False

'''
	计算系统中用户的数量
	无需传入参数
	返回： int，用户数量
'''
def calculate_number_of_user():
	sql = "select count(*) from user"
	try:
		result = dbhelper.execute_fetchone(sql)[0]
		return result
	except:
		return -1

'''
	计算当天用户的登录情况，算出数量
	无需传入参数
	返回： int，当天用户登录的数量
'''
def calculate_number_of_login():
	sql = "select count(*) from sign_in where to_days(time) = to_days(now())"
	try:
		result = dbhelper.execute_fetchone(sql)[0]
		return result
	except:
		return -1

'''
	计算最近一周用户的登录数据
	无需传入参数
	返回： 一个数组，记录最近7天用户登录的数据
'''
def calculate_number_of_login_weekly():
	result = []
	result.append(calculate_number_of_login())
	sql = "select count(*) from sign_in where to_days(now())-to_days(time) <= %d"

	try:
		for num in range (0,6):
			temp1 = dbhelper.execute_fetchone(sql%(num))[0]
			temp2 = dbhelper.execute_fetchone(sql%(num+1))[0]
			result.append(temp2-temp1)
		return result
	except:
		return None


'''
	计算当天爱心币的流通数量，包括事件的爱心币和转账的爱心币
	无需传入参数
	返还：int ，一个币值
'''
def calculate_currency():
	
	trade = 0
	exchange = 0

	sql = "select lovecoin from coin_exchange where to_days(time) = to_days(now())"

	try:
		exchange_result = dbhelper.execute_fetchall(sql)
		for each_result in exchange_result:
			exchange += each_result[0]
	except:
		return None

	sql = "select lovecoin from coin_trade where to_days(time) = to_days(now())"

	try:
		trade_result = dbhelper.execute_fetchall(sql)
		for each_result in trade_result:
			trade += each_result[0]
	except:
		return None

	return exchange + trade

'''
	计算最近一周爱心币流通数量情况
	无需传入参数
	返回：一个数组，记录一周7天，每天爱心币的流通数量
'''
def calculate_currency_weekly():
	
	result = []

	sql_exchange = "select lovecoin from coin_exchange where to_days(now())-to_days(time) <= %d"
	sql_trade = "select lovecoin from coin_trade where to_days(now())-to_days(time) <= %d"

	result.append(calculate_currency())
	try:
		for num in range(0,6):

			exchange = 0
			trade = 0

			temp1 = 0
			exchange_result1 = dbhelper.execute_fetchall(sql_exchange%(num))
			for each_result in exchange_result1:
				temp1 += each_result[0]

			temp2 = 0
			exchange_result2 = dbhelper.execute_fetchall(sql_exchange%(num+1))
			for each_result in exchange_result2:
				temp2 += each_result[0]

			exchange = temp2 - temp1

			temp3 = 0
			trade_result1 = dbhelper.execute_fetchall(sql_trade%(num))
			for each_result in trade_result1:
				temp3 += trade_result1[0]

			temp4 = 0
			trade_result2 = dbhelper.execute_fetchall(sql_trade%(num+1))
			for each_result in trade_result2:
				temp4 += each_result[0]

			trade = temp4 - temp3
			result.append(exchange + trade)

		return result
	except:
		return None

'''
	计算当天涉及爱心币交易的用户数量
	无需传入参数
	返回：int， 用户数量
'''
def calclulate_user_involve_lovecoin():
	
	result = set()

	sql = "select sender,receiver from coin_exchange where to_days(time) = to_days(now())"

	try:
		temp1 = dbhelper.execute_fetchall(sql)
		for each_result in temp1:
			result.add(each_result[0])
			result.add(each_result[1])
	except:
		return None

	sql = "select sender,receiver from coin_trade where to_days(time) = to_days(now())"
	try:
		temp2 = dbhelper.execute_fetchall(sql)
		for each_result in temp2:
			result.add(each_result[0])
			result.add(each_result[1])
	except:
		return None

	return len(result)

'''
	计算当天爱心币的流通次数，通过 流通的爱心币/必要的爱心币 求得
	无需传入参数
	返回：一个2位小数的浮点数（float）
'''

def calculate_circulation_times():
	
	circulation_coin = calculate_currency()

	necessary_coin = 0
	sql = "select lovecoin from coin_exchange where to_days(time) = to_days(now())"

	try:
		exchange_result = dbhelper.execute_fetchall(sql)
		for each_result in exchange_result:
			necessary_coin += each_result[0]
	except:
		return None

	sql_event = "select love_coin from event where to_days(time) = to_days(now())"

	try:
		event_result = dbhelper.execute_fetchall(sql_event)
		for each_result in event_result:
			necessary_coin += each_result[0]
	except:
		return None
	
	if necessary_coin == 0:
		return 0
	else:
		return ('%.2f'%(circulation_coin/necessary_coin))

'''
	计算系统所有的爱心币数量
	无需传入参数
	返回： int， 系统爱心币的数量
'''
def calcultae_system_lovecoin():
	
	result = 0
	sql = "select love_coin from loving_bank"

	try:
		sql_result = dbhelper.execute_fetchall(sql)
		for each_result in sql_result:
			result += each_result[0]

		return result
	except:
		return None

'''
	计算系统人均耗费的爱心币数量，算法如下：
	求出所有求助求救事件所花费的爱心币数量，再求出事件的数量，爱心币数量/事件的数量 即得
	无需传入参数
	返回：一个2位小数的浮点数（float）
'''

def user_consume_coin():
	
	result = 0
	sql = "select love_coin from event"

	try:
		sql_result = dbhelper.execute_fetchall(sql)
		for each_result in sql_result:
			result += each_result[0]	
	except:
		return None

	sql_event_num = "select count(*) from event"

	try:
		event_num = dbhelper.execute_fetchone(sql_event_num)[0]
	except:
		return None

	if event_num == 0:
		return 0
	else:
		return ('%.2f'%(result/event_num))

'''
	计算系统人均产出爱心币数量，算法如下：
	求出整个系统的爱心币数量，减去初始化爱心币的数量，即为用户赚得的，再除以人数即求得
	无需传入参数
	返回：一个浮点数
'''

def user_earn_coin():
	
	num_of_coin = calcultae_system_lovecoin()
	num_of_user = calculate_number_of_user()
	result = '%.2f'%((num_of_coin - num_of_user * 20) / num_of_user)

	return result

'''
	因为现在还没有提供真正可以兑换的服务，所以这里默认提供的服务为用户初始化货币
	的一半。
'''
def user_exchange_coin():
	
	exchange_coin = 10
	return exchange_coin

'''
	获取一个事件悬赏的币值，
	传入： 事件的id
	返回： 事件的币值
'''
def get_coin_from_event(eventId):
	
	sql = "select love_coin from event where id = %d"

	try:
		result = dbhelper.execute_fetchone(sql%(eventId))[0]
		return result
	except:
		return None

'''
	获取事件有多少人响应并帮助求助人
	传入： 事件的id
	返回： 帮助的人数
'''

def get_supporter_num_from_event(eventId):
	
	sql = "select count(*) from support_relation where event_id = %d"
	try:
		result = dbhelper.execute_fetchone(sql%(eventId))[0]
		return result
	except:
		return None

'''
	算法分析：
	无需传入参数
	返回：一个浮点数，表明系统最近一个月的通货膨胀率
'''

def algorithm_analysis():
	'''
		时间范围：30天内
		type为1或者2，这是求助，或者求救事件，才有爱心币
		state：2 说明为正常结束事件的。
	'''
	sql = "select id from event where date_sub(curdate(),interval 30 day) <= date(time) and (type = 1 or type = 2) and state = 2"
	
	earn_coin = 0
	try:
		result = dbhelper.execute_fetchall(sql)
		for each_result in result:
			user_num = get_supporter_num_from_event(each_result[0])
			event_coin = get_coin_from_event(each_result[0])
			if user_num is None or event_coin is None:
				return None

			if user_num == 0 :
				earn_coin += 0
			else:
				earn_coin += event_coin * (user_num - 1)
	except:
		return None

	basic_coin = calcultae_system_lovecoin() - earn_coin

	analyse_result = (earn_coin * 1.0) / basic_coin

	return '%.4f'%analyse_result

def welfare_coin(data):
	
	sql = "select userid from loving_bank where love_coin <= 5"

	try:
		result = dbhelper.execute_fetchall(sql)
		for each_result in result:
			info = {}
			info[KEY.ID] = each_result[0]
			info[KEY.OPERATION] = 0
			info[KEY.SCORE] = 0
			info[KEY.LOVE_COIN] = data
			if(not db.update_loving_bank(info)):
				return None
		return True
	except:
		return None













