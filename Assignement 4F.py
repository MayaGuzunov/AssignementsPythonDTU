#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 15:37:22 2021

@author: mayaguzunov
"""
import numpy as np
def removeIncomplete(id):
    
    newArray = np.ones(np.size(id), dtype=(bool))
    value=False
    
    for i in range(len(id)):
        
     num=np.floor(id[i])
     
     separate=np.sum(np.floor(id)==num)
     
     if separate!=3:
         
         newArray[i]=value
         
    idComplete=id[newArray]
    
    return idComplete

print(removeIncomplete(np.array([1.3, 2.2, 2.3, 4.2, 5.1, 3.2, 5.3, 3.3, 2.1, 1.1, 5.2, 3.1])))