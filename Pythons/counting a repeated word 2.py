# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:57:02 2021

@author: jijoj
"""

def check(string , sub_str):
    print(string.count(sub_str))
    print(string.find(sub_str))
    
        

input = "welcome to python. python is used in many ML programms"
substring = "python"
print(check(input , substring))
