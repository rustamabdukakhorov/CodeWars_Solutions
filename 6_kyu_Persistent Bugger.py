# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:18:48 2022

@author: R.U.S.T.E.A.M
"""

def persistence(n):
    k = 0
    if n>9:
        while n>9:
            s = str(n)
            t = 1
            for i in s:
                t*=int(i)
            n = t
            k += 1
    return k