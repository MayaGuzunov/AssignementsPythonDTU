#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 17:22:48 2021

@author: mayaguzunov
"""
import numpy as np

def count_unique_rows(x):
    row=x
    unique_rows=0
    row_del=x
    for i in range(len(row)):
        if row[i,0]==2:
            row_del=np.delete(row,i,axis=0)
            i=i+1
    new_array=np.sum(row_del,axis=1)
    count=len(np.unique(new_array,axis=0))
    

    return count


print(count_unique_rows(np.array([[1,2,3],[1,2,3],[2,2,3],[3,2,1],[1,2,4],[4,2,3],[2,2,3],[1,4,2]])))




    

