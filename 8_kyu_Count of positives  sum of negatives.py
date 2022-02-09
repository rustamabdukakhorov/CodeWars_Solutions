# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:41:23 2022

@author: R.U.S.T.E.A.M
"""

def count_positives_sum_negatives(arr):
    if arr == []:
        result = []
    else:
        n, s = 0, 0
        for i in arr:
            if i > 0:
                n += 1
            if i < 0:
                s += i
        result = [n, s]
    return result