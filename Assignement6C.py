#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:52:20 2021

@author: mayaguzunov
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def movingAvg():
    # newarray=[]
    # v=2
    # lettercount=np.ones(len(y))

    # for i in range(6):
    #     for j in range(len(y)):
    #         newarray=newarray.append(y)
    x=[1, 2, 3]
    y = np.array([[1, 2], [3, 4], [5, 6]])
    z=plt.plot(x,y)
    print(z)
    return z



# print(movingAvg(np.array([0.8, 0.9, 0.7, 0.6, 0.3, 0.4])))