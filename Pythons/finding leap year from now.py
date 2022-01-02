# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:06:16 2020

@author: jijo
"""
#to find the palindrome of a number

inputnumber = input()
inputnumber = int(inputnumber) 
reversenumber=0
while inputnumber>0:
    digit =inputnumber%10
    reversenumber = reversenumber*10 +digit
    inputnumber = inputnumber//10
print(reversenumber)
