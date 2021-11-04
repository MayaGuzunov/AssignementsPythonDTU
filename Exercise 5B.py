#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:42:43 2021

@author: mayaguzunov
"""

print("Please input a temperature: ")
x = float(input())
print(x)

print('Please input the unit of temperature(Celsius,Fahrenhei, or Kelvin)')
y=input()
print(y)

print('Please input the unit to convert to(Celsius,Fahrenhei, or Kelvin)')
z=input()
print(z)
           
           
           
  


def convertTemperature(T, unitFrom, unitTo):
    #Now I define the integer and units.
    x=T
    f=str(unitFrom)
    t=str(unitTo)
        #The next step is to give commands for conversion.
    if f=='Celsius': #First for Celsius
            if t=='Fahrenheit':
                T=1.8*x+32
            else:
                t=x+273.15 
    if f=='Fahrenheit': #Then to Farenheit
            if t=='Celsius':
                T=(x-32)/1.8
            else:
                T=(x+459.67)/1.8
    if f=='Kelvin': #Finally for K
            if t=='Celsius':
                T=x-273.15 
            else:
                T=1.8*x-459.67
    return str(x)+" " +str(unitFrom) + " = " + str(T) +" "+ str(unitTo)

print(convertTemperature(x, y, z))
