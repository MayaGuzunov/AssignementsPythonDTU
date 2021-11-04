#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:45:42 2021

@author: mayaguzunov
"""

import numpy as np
import math
def acuteAngle(v1,v2):  
    totalv = math.acos(np.dot(v1,v2))
    if totalv > math.pi/2:
        theta = math.pi - totalv
    elif totalv > 0:
        theta = totalv
    elif totalv < (3*math.pi)/2:
        theta = totalv
    elif totalv < math.pi:
            theta = totalv
    return theta


