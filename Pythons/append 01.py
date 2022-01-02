# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:58:28 2020

@author: jijoj
"""

listitem = [1,2,3]
for i in range(3):
    #value inside range represents the number of input values we can give 
    print("enter a value")
    item = input()
    listitem.append(item)
    #append is used to add an item to a list
print(listitem)