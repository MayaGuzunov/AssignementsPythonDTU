#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:27:26 2021

@author: mayaguzunov
"""
import math
import numpy as np
def boxArea(boxCorners, area):

    x1=boxCorners[np.array([0])]
    x2=boxCorners[np.array([1])]
    x3=boxCorners[np.array([2])]
    x4=boxCorners[np.array([3])]
    y1=boxCorners[np.array([4])]
    y2=boxCorners[np.array([5])]
    y3=boxCorners[np.array([6])]
    y4=boxCorners[np.array([7])]
    
    if area=="Box1":
        A=(x2-x1)*(y2-y1)
        
    elif area=="Box2":
        A=(x4-x3)*(y4-y3)
        
    elif area=="Intersection":
        A=max(0,min(x2,x4)-max(x1,x3))*max(0,min(y2,y4)-max(y1,y3))
        
    elif area=="Union":
       A=((x2-x1)*(y2-y1)+(x4-x3)*(y4-y3))-max(0,min(x2,x4)-max(x1,x3))*max(0,min(y2,y4)-max(y1,y3))
        

    return A
