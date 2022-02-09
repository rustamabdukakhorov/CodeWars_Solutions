# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:56:49 2022

@author: R.U.S.T.E.A.M
"""

def digitize(n):
    x = []
    if n>0:
        while n > 0:
            x.append(n%10)
            n=n//10
    else:
        x = [0]
    return x