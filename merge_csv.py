# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:28:49 2015

@author: cdick
"""

import pandas as pd
import csv

xy = pd.read_csv('dia.csv')
xy2 = pd.read_csv('csr_was_exception_but_passed_in_data.csv')

cmbn_xy = pd.DataFrame(xy,xy2)
mrg_xy = xy.merge(xy2, on=['SEDOL'])
mrg_xy[['scores']] = mrg_xy[['scores']].astype(float)

#mrg_xy.convert_objects(convert_numeric=True)

x = mrg_xy['scores'].mean()
xlow = mrg_xy['scores'].min()


print("average ESG", '% 20.2f' % x)
print("lowest ESG", '% 20.2f' % xlow)
mrg_xy.to_csv('test.csv')
print(mrg_xy.describe())

