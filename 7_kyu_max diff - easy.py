# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:42:38 2022

@author: R.U.S.T.E.A.M
"""

def max_diff(lst):
    if lst == []:
        return 0
    else:
        lst.sort()
        return lst[len(lst)-1] - lst[0]