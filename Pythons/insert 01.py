# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:28:15 2020

@author: jijoj
"""

listitem=["apple","orange","grape"]
print(listitem)
list2 = ["a","b","c"]
listitem.extend(list2)
#extend is used to add multiple items to a list or add a list to another list
print(listitem)
listitem.insert(2,"banana")
#insert is used to add an item to a list at a particular location
print(listitem)