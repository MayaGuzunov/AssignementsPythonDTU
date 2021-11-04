#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 00:22:35 2021

@author: mayaguzunov
"""

def bacteriaGrowth(n0,alpha,K,N):
    tN=1
    nt=0
    result=0
    
    for i in range(500000):
        if(n0<N<K):
            nt=(1+alpha*(1-(n0/K)))*n0
            n0=nt
            if(nt<N):
                tN=tN+1
    if(tN==1):
        tN=0
    
    return tN
print(bacteriaGrowth(100.0, 0.4, 1000.0, 500.0))
print(bacteriaGrowth(100.0, 0.0004, 1000.0, 500.0))
print(bacteriaGrowth(100.0, 0.4, 1000.0, 99.0))