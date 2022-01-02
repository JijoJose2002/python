# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:15:01 2021

@author: jijoj
"""

def split_string(string):
    #split the string based on space delimiter
    list_string = string.split(' ')
    return list_string
input = "welcome to python"
list = split_string(input)
for i in list:
    print(i )
print(list)   