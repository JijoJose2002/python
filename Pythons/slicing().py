# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:31:43 2020

@author: jijoj
"""
#slicing is used to make a new sub list from our current list
listitem=["a","b","c","d","e","f"]
list2 = listitem[2:5]
print(list2)

#if we need to select alternate items in a list
listitem=["a","b","c","d","e","f"]
list2 = listitem[2:6:2]
#similar to alt numbers in range()
print(list2)