#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:28:02 2021

@author: mayaguzunov
"""

import math
import numpy as np
def computeProjection(a):
    c=np.size(a)
    b=np.ones(np.size(a))
    
    projection=(np.dot(a,b))/(math.sqrt(np.dot(a,a))**2)*a
    return projection

    
