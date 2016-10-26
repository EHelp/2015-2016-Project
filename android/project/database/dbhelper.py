#!/usr/python
# -*- coding: utf-8 -*-

import MySQLdb
from DBUtils.PooledDB import PooledDB

#pooldb = PooledDB(creator=MySQLdb, mincached=5, host='127.0.0.1', user='root', passwd='root', db='ehelp', charset='utf8')
pooldb = PooledDB(creator=MySQLdb, mincached=5, host='127.0.0.1', user='root', db='ehelp', charset='utf8')
class dbhelper:

  '''
  connect to database and return a connection instance.
  '''
  @staticmethod
  def connect():
    return pooldb.connection()

  
  '''
  execute update and delete operation on database.
  '''
  @staticmethod
  def execute(sql):
    conn = dbhelper.connect()
    cursor = conn.cursor()
    try:
      n = cursor.execute(sql)
      conn.commit()
    except:
      n = 0
    finally:
      cursor.close()
      conn.close()
      return n

  '''
  execute insert operation on database.
  '''
  '''
  @staticmethod

  def insert(sql):

    conn = dbhelper.connect()
    cursor = conn.cursor()
    try:
      cursor.execute(sql)
      #MySQLdb插入后 取得插入记录主键id的方法
      insert_id = conn.insert_id()
      conn.commit()
    except Exception, e:
      print "err"
      print e
      insert_id = -1
    finally:
      cursor.close()
      conn.close()
      print "final"
      return insert_id'''

  @staticmethod
  def insert(sql):
    conn = dbhelper.connect()
    cursor = conn.cursor()
    insert_id = -1
    try:
      cursor.execute(sql)
      insert_id = cursor.lastrowid  
      conn.commit()
    except Exception, e:
      insert_id = -1
      print e
    finally:
      cursor.close()
      conn.close()
      return insert_id

  '''
  execute query operation on database and return only one result.
  result may be None.
  '''
  @staticmethod
  def execute_fetchone(sql):
    conn = dbhelper.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


  '''
  execute query operation on database and return all results.
  '''
  @staticmethod
  def execute_fetchall(sql):
    conn = dbhelper.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


