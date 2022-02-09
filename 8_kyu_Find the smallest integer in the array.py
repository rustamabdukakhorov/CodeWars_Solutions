# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:48:30 2022

@author: R.U.S.T.E.A.M
"""

def find_smallest_int(arr):
    min = arr[0]
    for i in arr:
        if i <min:
            min = i
    return min