# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:21:31 2020

@author: jijoj
"""

#while loop factorial
factorial = 1
number = input("give a number")
number = int(number)
count = 1
while count<=number:
    factorial = factorial*count
    count = count+1
    print(factorial)