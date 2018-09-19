# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:25:12 2018

@author: segun

"""

"""34*x^2+ 64*x -510=0 """
"""
import math
a=34
b=68
c=-510
x1=(-b+math.sqrt(b**2 - 4*a*c))/(2*a)
print(x1)
print("This is my first exercise")
mynum=0
count=0
for i in range(5):
    mynum+=1
    count+=1
    if mynum==3:
        print("here you go "+ str(mynum))
        break
    
print("out of loop after " +str(count) + " counts")
print("testing") """
mysum=0
count=0
n=int(input("enter number: "))
for i in range(1,n+1):
    if i % 7 == 0 and i % 2 == 0:
        print(i)
        mysum += i
        count += 1
print("the average is " + str(mysum/count)) #comment