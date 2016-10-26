#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import trust

def runtest():
    evaluation = []
    direct_trust = []
    
    evaluation_times = 200
    fail_counts = 0
    for i in range(evaluation_times):
        #eva = random.randint(1,3)
        eva = 0.9
        if i > 100:
            eva = 0.1
        evaluation.append(eva)
        if eva < 0.5:
            fail_counts += 1
        
        DT = trust.direct_trust(164, 165, eva, fail_counts)
        direct_trust.append(DT)
   
    plt.figure(num=1, figsize=(16, 12))
    plt.title('Direct Trust', size=14)
    plt.xlabel('evaluation', size=14)
    plt.ylabel('direct trust value', size=14)
    plt.plot(np.arange(1, 201, 1), evaluation, color='r', linestyle='--', marker='o', label='evaluation value')
    plt.plot(np.arange(1, 201, 1), direct_trust, color='b', linestyle='-', label='direct trust value')
    #plt.legend(loc='upper left')
    plt.savefig('direct_trust_result.png', format='png')

        

if __name__ == "__main__":
    runtest()