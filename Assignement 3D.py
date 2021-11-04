#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:26:47 2021

@author: mayaguzunov
"""

def gravitationalPull(x):
    
    R=6.371e6
    g0=9.82
  
    if R<=x:
        g=g0*(R**2/x**2)
             
       
        
    elif x>=0 and x<R:
        g=g0*(x/R)
    
    
    return g
