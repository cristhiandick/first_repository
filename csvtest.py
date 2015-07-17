# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:47:51 2015

@author: cdick
"""


import csv
import pandas as pd


f = open('dia.csv')
csv_f = csv.reader(f,delimiter=',')

xy = []

for row in csv_f:
    xy.append(row[4])
    

f = open('csrhub_detailed.csv')
csv_f = csv.reader(f,delimiter=',')

xy2 = []

for row in csv_f:
    xy2.append(row[1])

f.close()

combine_series = pd.DataFrame([xy,xy2])

#print(xy)
#print(xy2)
#print (pd)
print (combine_series.data)



