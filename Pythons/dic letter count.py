# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 00:12:32 2021

@author: jijoj
"""

file=open("c:/users/jijoj/onedrive/desktop/pp/ss.txt" , 'r')
txt=file.read()
lettercount={}
for var in txt:
    if var not in lettercount:
        lettercount[var]=0
    lettercount[var]=lettercount[var]+1
for c in lettercount:
    print(c,lettercount[c])