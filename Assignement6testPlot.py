#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:52:20 2021

@author: mayaguzunov
"""
import numpy as np
import math


def movingAvg(y):
    
    
    newarray=np.zeros((5,10))
    # newarray[0]=[0.8, 0.9, 0.7, 0.6, 0.3, 0.4]
  
    # print(len(y[0]))

    b=0
    for i in range(5):
        v=0
        for j in range(b,10,1):
            if(v < len(y)):
                newarray[i,j]=y[v]
                v=v+1
        i=i+1
        b=b+1
        
    z=np.array([1,2,3,2,1])
    y=(newarray.T * z).T
    y=y[:,2:8]
    y=(np.sum(y,axis=0))/9
  
    
    return y



print(movingAvg(np.array([0.8, 0.9, 0.7, 0.6, 0.3, 0.4])))