# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 02:01:57 2021

@author: jijoj
"""
olympians = [("jijo",1,"100m sprint"),("jimmy",1,"1500m marathon"),("jiji",1,"50km walking"),("jose",1,"weight lifting")]
output=open("C:/Users/jijoj/OneDrive/Desktop/outfile.csv","w")
#header
output.write('name,rank,item')
output.write('\n')
#output for row
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    output.write(row_string)
    output.write('\n')
output.close()


















