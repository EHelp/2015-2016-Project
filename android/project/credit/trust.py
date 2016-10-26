#!/usr/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from math import e
import math
import decimal

import database
from database.dbhelper import dbhelper

def direct_trust(userA, userB, evaluation, n):
    sql = "select value, weight, growth_factor from trust where _from = %d and _to = %d"
    result = dbhelper.execute_fetchone(sql%(userA, userB))
    if result is None:
        sql = "insert into trust(_from, _to, value, weight, growth_factor) values (%d, %d, %f, %f, %f)"
        dbhelper.insert(sql%(userA, userB, evaluation, 0.5, 0.05))
        return evaluation
    else:
        history_trust = result[0]
        current_weight = weight = result[1]
        growth_factor = result[2]
        if evaluation < 0.5:
            weight = calculate_new_weight_for_test(userA, userB, n)
            growth_factor = growth_factor / 4
            current_weight = 1 - weight
        else:
            current_weight = weight = min(0.5, weight + growth_factor)
        new_trust = decimal.Decimal(current_weight) * decimal.Decimal(evaluation) + decimal.Decimal(1 - current_weight) * history_trust
        sql = "update trust set value = %f, weight = %f, growth_factor = %f where _from = %d and _to = %d"
        dbhelper.execute(sql%(new_trust, weight, growth_factor, userA, userB))

        return new_trust
        
def calculate_new_weight(userA, userB):
    sql = "select count(*) from evaluation where evaluation.from = %d and evaluation.to = %d and evaluation.value < 0.5"
    result = dbhelper.execute_fetchone(sql%(userA, userB))
    return 1 - ( 1 / (1 + e ** -(2 ** (result[0]-1)) ) )
    
def calculate_new_weight_for_test(userA, userB, n):
    return 1 - ( 1 / (1 + e ** -(2 ** (n-1)) ) )

def evaluation_similarity(userA, userB):
    sql = "select E1.value, E2.value from evaluation E1, evaluation E2 where E1.to = E2.to and E1.from = %d and E2.from = %d"
    result = dbhelper.execute_fetchall(sql%(userA, userB))
    similarity = 0.0
    dot_product = 0.0
    lengthA = lengthB = 0.0
    for each_result in result:
        dot_product += each_result[0] * each_result[1]
        lengthA += each_result[0] * each_result[0]
        lengthB += each_result[1] * each_result[1]
    lengthA = math.sqrt(lengthA)
    lengthB = math.sqrt(lengthB)
    if lengthA * lengthB == 0:
        similarity = 0.0
    else:
        similarity = dot_product / (lengthA * lengthB)
    if similarity == 1:
        similarity = 1 - abs(lengthA - lengthB)
    return similarity

def recommend_trust(userA, userB, threshold=0.5):
    sql = "select T1.value, T1.to, T2.value from trust T1, trust T2 where T1._to = T2._from and T1._from = %d and T1.value > %f and T2._to = %d"
    result = dbhelper.execute_fetchall(sql%(userA, threshold, userB))
    rcmd_trust = weights = 0.0
    for each_result in result:
        sim_eva = evaluation_similarity(userA, result[1])
        rcmd_trust += result[0] * sim_eva * result[2]
        weights += result[0] * sim_eva
    if weights == 0:
        rcmd_trust = 0.0
    else:
        rcmd_trust /= weights
    return (rcmd_trust, len(result))
    
def get_cooperation_times(userA, userB):
    sql = "select count(*) from evaluation where evaluation.from = %d and evaluation.to = %d"
    return dbhelper.execute_fetchone(sql%(userA, userB))[0]