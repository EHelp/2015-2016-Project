'''
definition for sessions.
'''
import KEY
import datetime
import redis
import time


class Session:

	ONLINE_LAST_MINUTES = 5

	@classmethod
	def insert_session(self, data):
		r = redis.Redis(host='localhost', port=6379, db=0)
                now = int(time.time())
                expires = now + (self.ONLINE_LAST_MINUTES * 60) + 10

                r.set(data[KEY.TEMP_ID], data[KEY.SMSCODE])
                r.expireat(data[KEY.TEMP_ID], expires)

	@classmethod
	def exists(self, flag):
		if KEY.TEMP_ID not in flag:
			return False
		r = redis.Redis(host='localhost', port=6379, db=0)
                sms = r.get(flag[KEY.TEMP_ID])
                if sms:
                        return True
                else:
                        return False

	@classmethod
	def confirm_by_flag(self, flag):
		print flag
		if KEY.TEMP_ID not in flag or KEY.SMSCODE not in flag:
			return False
		r = redis.Redis(host='localhost', port=6379,db=0)
		sms = r.get(flag[KEY.TEMP_ID])
		if sms:
			if sms == flag[KEY.SMSCODE]:
				return True
		return False

'''
class Session:
	
	@classmethod
	def insert_session(self, data):

		if len(self.storage) > 1000:
			self.storage = self.storage[-100:]

		now = datetime.datetime.now()
		life_circle = now + datetime.timedelta(seconds=600)
		data[KEY.LIFECIRCLE] = life_circle
		self.storage.append(data)

	@classmethod
	def confirm_by_flag(self, flag):
		if KEY.COOKIE not in flag or KEY.PHONE not in flag:
			return False

		for item in self.storage:
			now = datetime.datetime.now()
			if item[KEY.COOKIE] == flag[KEY.COOKIE] and item[KEY.SMSCODE] == flag[KEY.SMSCODE]:
				if now < item[KEY.LIFECIRCLE]:
					return True
		return False

	@classmethod
	def verify_by_flag(self, flag):
		if KEY.COOKIE  not in flag:
			return False
		for item in self.storage:
			now = datetime.datetime.now()
			if item[KEY.COOKIE] == flag[KEY.COOKIE]:
				if now < item[KEY.LIFECIRCLE]:
					return True
		return False'''
