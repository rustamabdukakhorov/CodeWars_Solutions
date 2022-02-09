# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:47:01 2022

@author: R.U.S.T.E.A.M
"""

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i>0:
            sum+=i
    return sum