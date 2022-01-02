# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:49:21 2021

@author: jijoj
"""

tup=(1,2,3,4,5,6,7,8,9,10)
l1 = []
for i in tup:
    if i%2==1:
        l1.append(i)
tup=tuple(l1)
print(tup)
print(sum(tup[3:7]))
        
