# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:40:13 2021

@author: jijoj
"""

#welcome to python. Python is used in many ML programms
# function to check if a string is present in a sub string

def check(string , sub_str):
    # return string
    if (string.count(sub_str)>0):
        return "YES"
    else:
        return "NO"

input = "welcome to python. python is used in many ML programms"
substring = "python"
print(check(input , substring))

    