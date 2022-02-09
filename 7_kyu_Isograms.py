# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:29:15 2022

@author: R.U.S.T.E.A.M
"""

def is_isogram(string):
    
    x = [i for i in string.lower()]
    x.sort()
    ans = True
    for i in range(len(x) - 1):
        if x[i] == x[i+1]:
            ans = False
    return ans