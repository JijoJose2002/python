# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:18:24 2021

@author: jijoj
"""

import hashlib

pass_hass=input("enter md5 hash:")
wordlist=input("file name:")
try:
    pass_file = open(wordlist,"r")
except:
    print("no file found:")
    quit()
for word in pass_file:
    
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd,strip()).hexdigest()
    
    if digest ==pass_hass:
        print("password found")
