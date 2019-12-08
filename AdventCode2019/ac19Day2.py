# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:22:19 2019

@author: Sophie
"""
from itertools import product
myList = []
file = open("C:/Users/Sophie/Documents/PythonScripts/adventCode2019/input2.txt", "r")
for line in file:
    myList= line.split(",")

myList = list(map(int, myList))

    
def opCode(theList, noun, verb):
    lst = theList.copy()
    lst[1] = noun
    lst[2] = verb
    #print("ugh")
    for i in range(0, len(lst), 4):    
        if lst[i] == 99:
            print("99 problems")
            return lst[0]
        if lst[i]==1:
            #print("before op1 ", lst[lst[i+3]])
            try:
                lst[lst[i+3]] = lst[lst[i+1]] + lst[lst[i+2]]
            except:
                return -1
            #print("after op1 ", lst[lst[i+3]])
        if lst[i] ==2:
            #print("before op2 ", lst[lst[i+3]])
            try:
                lst[lst[i+3]] = lst[lst[i+1]] * lst[lst[i+2]]
            except:
                return -1
            #print("after op2 ", lst[lst[i+3]])
            
    return -1

for noun, verb in product(range(0, 100), range(0, 100)):
    if opCode(myList, noun, verb) ==19690720:
        print(f"2. {100 * noun + verb}")
        break