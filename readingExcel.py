#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:12:59 2019

@author: nsdeveloper

import pandas as pd
translation = pd.read_excel(r'translation.xlsx')
"""
excel = pd.read_excel(r'translation.xlsx')

#key_column = excel['key']
#print(key_column)

df = pd.DataFrame(excel)


for row in excel.itertuples(index=False): 
    for key, val in row._asdict().items():
        print(key, val)
    #for i in row:
     #   print(i)

"""
for key, val in row._asdict():
        print(key, val)
"""
#for i, j in df.iterrows(): 
 #   print(i, j)
  #  print()

#a = translation.to_dict()
#print(translation)
#for i in translation:

#    for k in translation:
#        print(i)
        
#print()
#print(a)