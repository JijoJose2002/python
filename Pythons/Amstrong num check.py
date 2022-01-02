# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:56:12 2020

@author: jijoj
"""
 
num = input("give me a number : ")
num = int(num)
sum = 0
tmp = num 
while tmp>0:
    digit = tmp%10
    sum =sum+digit**3
    tmp=tmp//10
if num ==sum:
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number") 
    