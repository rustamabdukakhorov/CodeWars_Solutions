# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:43:54 2022

@author: R.U.S.T.E.A.M
"""

def get_sum(a,b):
    if a==b:
        return a
    else:
        s = 0
        for i in range(min(a,b), max(a, b)+1):
            s+=i
        return s