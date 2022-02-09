# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:25:06 2022

@author: R.U.S.T.E.A.M
"""

def move_zeros(array):
    x = l = []
    for i in array:
        if i != 0:
            x.append(i)
    l = [0 for i in range(array.count(0))]
    return x + l