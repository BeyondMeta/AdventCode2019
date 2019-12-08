# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:23:26 2019

@author: Sophie
"""

import math

myList = []
file = open("C:/Users/Sophie/Documents/PythonScripts/adventCode2019/input3.txt", "r")
for line in file:
    myList.append(line.split(','))
    
#    myList.append([line[0], int(line[1:])])
    
dct = {
       'U': (0, 1),
       'D': (0, -1),
       'L': (-1, 0),
       'R': (1, 0)
           }
#Function takes a set of directions and generates 
#a set with every unique point that would be crossed 
def GeneratePoints(lst):
    currentCoord = (0, 0)
    points = set(currentCoord)
    for i in lst:
        direction = dct[i[0]]
        movement = int(i[1:])
        for j in range(0,movement):
            currentCoord = (currentCoord[0] +direction[0] , 
                            currentCoord[1] +direction[1])
            points.add(currentCoord)
    return points

#takes the directions for two wires. Finds the intersection. 
# and returns the manhattan distance of nearest crossed wire 
#from the starting point
    
def CrossWires(list1, list2):
    set1 = GeneratePoints(list1)
    set2 = GeneratePoints(list2)
    intersection = set1.intersection(set2)
    intersection.remove(0)
    print(intersection)
    myMin = math.inf
    for i in intersection:
        manhattanDist = i[0] + i[1]
        if manhattanDist < myMin:
            myMin = manhattanDist
    return myMin
    
    
#I don't need to write additional code to get this as CrossWires printed when I ran it    
myIntersection = {(2119, 3700), (1327, 1787), (890, 1208),
                  (2119, 3779), (2727, 2990), (2065, 2757), 
                  (2290, 2018), (433, 0), (5702, 3178), (2478, 3463),
                  (2242, 1348), (990, 153), (2308, 3999), (1389, 3807),
                  (3026, 2719), (890, 754), (2478, 3499), (4888, 3326),
                  (1327, 1848), (2419, 2151), (1327, 1888), (639, 408),
                  (1435, 2340), (731, 683), (1327, 1961), (738, 408),
                  (3714, 3889), (496, 683), (2862, 2719), (3031, 2719),
                  (4093, 3912), (5702, 3531), (1327, 2147), (3240, 3670),
                  (2194, 1454), (3476, 2719), (1938, 1348), (2727, 2855),
                  (2290, 1530), (1938, 1454), (2744, 1188), (433, 408),
                  (2400, 1348), (2313, 3999), (890, 915), (2104, 3700),
                  (2119, 3988), (1327, 1942), (2290, 1474), (2371, 2231),
                  (2906, 3463), (258, 0), (2290, 1469), (939, 1367),
                  (3272, 1352), (890, 708), (1435, 2757), (2119, 3996),
                  (5581, 3167), (1166, 1367), (890, 1260), (3272, 1220)}
    
#Given directions Generates a dict of points with the time
#it takes to get to every point on the list    
def StepsToIntersection(directions, intersection):
    currentCoord = (0, 0)
    points = set(currentCoord)
    numberSteps =1
    dictionary = {}
    for i in directions:
        direction = dct[i[0]]
        movement = int(i[1:])
        for j in range(0,movement):
            currentCoord = (currentCoord[0] +direction[0] , 
                            currentCoord[1] +direction[1])
            if currentCoord in intersection:
                if currentCoord not in dictionary:
                    dictionary[currentCoord] = numberSteps 
            points.add(currentCoord)
            numberSteps += 1
    return dictionary

def ShortestIntersection(direct1, direct2):
    dict1 = StepsToIntersection(direct1, myIntersection)
    print(dict1)
    dict2 = StepsToIntersection(direct2, myIntersection)
    shortestDist = math.inf
    for i in myIntersection:
        if dict1[i] + dict2[i] <shortestDist:
            shortestDist = dict1[i] + dict2[i]
    return shortestDist


