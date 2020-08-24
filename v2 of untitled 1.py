# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:01:28 2020

@author: user
"""

eng=int(input("plz input eng score:"))
math=int(input("plz input math score:"))
if eng>=90 and math>=90:
    print('prizes guranteed')
elif eng<=60 or math<=60:
    print('punishment')
elif eng>=60 or math>=60:
    print('get better')