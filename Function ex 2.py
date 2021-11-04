#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:55:49 2021

@author: mayaguzunov
"""
import numpy as np
v1=np.array([1,2,3,4,5])
v2=np.array([3,4,5,6,7])
v3=np.ones(4)
ex1=np.dot(v1,v2)
print(ex1)
ex2=v1*v2
print(ex2)
ex3=np.sin(v1)
print(ex3)
ex4=np.size(v1)
print(ex4)
ex5=np.dot(v1,v3)
print(ex5)




