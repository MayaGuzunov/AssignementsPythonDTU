#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:08:27 2021

@author: mayaguzunov
"""
import numpy as np


def computeItemCost(resourceItemMatrix, resourceCost):
    
 x=resourceItemMatrix
 y=resourceCost
 
 x=x.transpose()
 itemCost=np.dot(x,y)
 
 
 return itemCost
print(computeItemCost(np.array([[6,3,0],[17,11,9],[4,2,12]]),np.array([101.25,84.00,75.50])))