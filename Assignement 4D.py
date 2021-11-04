#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 22:09:02 2021

@author: mayaguzunov
"""
import statistics
import numpy as np

def fermentationRate(measuredRate, lowerBound, upperBound):
    arraySum=0
    countArray=0
    for i in range(len(measuredRate)):
        if(lowerBound<(measuredRate[np.array(i)])<upperBound):
            
            averageRate=measuredRate[np.array(i)]
                        
            arraySum=averageRate+arraySum
            
            countArray=countArray+1
            
    averageRate=arraySum/countArray
    return averageRate
print(fermentationRate(np.array([20.1, 19.3, 1.1, 18.2, 19.7, 121.1, 20.3, 20.0]),12,25))