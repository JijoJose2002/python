# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:46:29 2020

@author: jijoj
"""
#write a program to check whether a number is divisible by 5
 
def div5(number):
    if number%5==0:
        return True
    else:
        return False
    
list1=[11,22,55,70,604,115]
for i in list1:
    if div5(i):
        print(i,"is divisible by 5")
    else:
        print(i,"is not divisible by 5")
for i in range(3):
    
    item=int(input("new "))
    list1.append(item)