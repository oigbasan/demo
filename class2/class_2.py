# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 11:50:20 2018

@author: owner
"""
''' while iteraiton''' # careful not to get into an infinite loop, here while can be used with a < sign

n=input("you are in a lost forest, go right or left:")
while n =="right":
    n=input(" you are still lost, go right or left:")
print("you got out")
""" Recall when using for loops and range function, the stop element is not included
Break takes you out of a block

"""
mysum=0
count=0
for i in range(5,11,2):
    mysum+=i
    count+=1
    if mysum==12:
        print("out of loop on the " + str(count) + " count(s)")
        break
    mysum
print(mysum)

if len(list(range(5,11,2)))==count:
    print("Completed the iteration in " +str(count)+" counts")
   