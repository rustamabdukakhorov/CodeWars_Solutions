# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:42:19 2022

@author: R.U.S.T.E.A.M
"""

def hotpo(n):
    m = int(n)
    x = 0
    while m != 0:
        if m == 1:
            m = 0
        else:
            if m%2==1:
                m=3*m+1
            else:
                m=m//2
            x+=1
    return x