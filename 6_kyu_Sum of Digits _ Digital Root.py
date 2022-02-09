# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:28:49 2022

@author: R.U.S.T.E.A.M
"""

def digital_root(n):
    while n>9:
        s = str(n)
        x = [int(i) for i in s]
        n = sum(x)
    return n