# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:33:09 2022

@author: R.U.S.T.E.A.M
"""

def find_short(s):
    n = s.split(' ')
    x = []
    for i in n:
        x.append(len(i))
    return min(x)