# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:49:47 2022

@author: R.U.S.T.E.A.M
"""

def count_sheeps(sheep):
    n = 0
    for i in sheep:
        if i:
            n+=1
    return n