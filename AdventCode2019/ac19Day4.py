# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:08:01 2019

@author: Sophie
"""

def validPassword(num):
    myStr = str(num)
    doubleDigit = False
    previousDigit = str(num)[0]
    futureDigit = str(num)[2]
    for i in range(1, 4):
        if previousDigit == myStr[i] and futureDigit  != myStr[i]:
            doubleDigit = True
        if previousDigit > myStr[i]:
            return False
        previousDigit = myStr[i]
        futureDigit = myStr[i +2]
    return doubleDigit


number = 0
for i in range(134564, 585159):
    if validPassword(i):
        number += 1
print(number)