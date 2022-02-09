# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:29:33 2022

@author: R.U.S.T.E.A.M
"""

def filter_list(l):
    x = []
    s = 'rustam'
    for i in l:
        if type(i) != type(s):
            x.append(i)
    return x