# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:59:34 2020

@author: jijoj
"""
#python program to find factorial of a number
factorial = 1
number = input("give a number to find factorial")
number =int(number)
if number<0:
    print("factorial not available for negative number")

else:
    for i in range(1,number+1):
        factorial = factorial*i
 print("factorial of ", number,"is",factorial)