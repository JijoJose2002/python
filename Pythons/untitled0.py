# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:17:38 2021

@author: jijoj
"""

athletics=[("a",1,"z"),("b",2,"y"),("c",3,"x")]
#open and write
file = open("c:/Users/jijoj/Onedrive/Desktop/sports.csv",'w')
    #header
file.write("name,rank,alpha")
file.write('\n')
#rest of the rows
for i in athletics:
    row='{},{},{}'.format(i[0],str(i[1]),i[2])
    file.write(row)
    file.write('\n')
file.close()











