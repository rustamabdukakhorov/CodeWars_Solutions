# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:26:27 2022

@author: R.U.S.T.E.A.M
"""

def array_diff(a, b):
    x = []
    for i in a:
        if i in b:
            pass
        else:
            x.append(i)
    return x