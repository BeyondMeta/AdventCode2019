# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:08:41 2019

@author: Sophie
"""
newList = []
file = open("C:/Users/Sophie/Documents/PythonScripts/AdventCode2019/input1.txt", "r")
for line in file:
    newList.append(int((line)))


def FuelRequired(num):
    return (num // 3) -2

def FuelRequired2(num):
    total = 0
    fr = num
    while(fr > 8):
        fr = FuelRequired(fr)
        total += fr
    return total
    
    
val = 0
for i in newList:
    val += FuelRequired2(i)
    
print(val)