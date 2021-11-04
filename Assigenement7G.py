#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:04:38 2021

@author: mayaguzunov
"""
import numpy as np
def textToNato(plainText):
  plainText=plainText.lower()
  
  natoText=plainText
  empty=np.array([])
  normal=np.array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
  NATOalphabet=np.array(['Alpha','Bravo','Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliet','Kilo','Lima','Mike','November','Oscar','Papa','Quebec','Romeo','Sierra','Tango','Uniform','Victor','Whiskey','Xray','Yankee','Zulu'])
  for i in range(len(plainText)):
      a=NATOalphabet[normal==plainText[i]]
      empty=np.append(empty,a)
  natoText="-".join(empty)
    
  
    
  return natoText
print(textToNato('aa'))