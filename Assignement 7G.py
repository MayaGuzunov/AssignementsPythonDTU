#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:49:28 2021

@author: mayaguzunov
"""

import numpy as np
import matplotlib.pyplot as plt
x = (1, 3, 4, 5)
y = (2, 3, 3, 4)
plt.plot(x, y)
plt.title("Simple line graph")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.xlim([0, 6])
plt.ylim([0, 5])
plt.show()
