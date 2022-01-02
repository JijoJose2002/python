# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:20:19 2020
program to check the given number is odd or even
@author: jijoj
"""
def check_odd_even(number):
    if (number%2==0):
       return True
    else:
        return False       
mylist=[]
k=int(input("type something"))
mylist.append()

for i in mylist:
    
    if check_odd_even(i):
        print (i,"is divisible")
    else:
        print(i,"is not divisible")