# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:52:29 2021

@author: jijoj
"""

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
ex_lst.sort(reverse = True ,key = lambda x:x[1])
print(ex_lst)