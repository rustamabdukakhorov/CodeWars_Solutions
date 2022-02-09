# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:23:10 2022

@author: R.U.S.T.E.A.M
"""

def find_outlier(integers):
    def find(l,n):
        for i in l:
            if i%2 == n:
                return i
        
    k = 0
    for i in integers:
        if i%2 == 0:
            k+=1
    if k<=1:
        return find(integers, 0)
    else:
        return find(integers, 1)