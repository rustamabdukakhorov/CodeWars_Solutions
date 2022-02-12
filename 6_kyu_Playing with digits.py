# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 00:37:36 2022

@author: R.U.S.T.E.A.M
"""

def dig_pow(n, p):
    a = n
    n = [int(i) for i in str(n)]
    s = 0
    for i in range(len(n)):
        s+= n[i]**(p+i)
    if s%a == 0:
        return s//a
    else:
        return -1