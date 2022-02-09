# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:49:12 2022

@author: R.U.S.T.E.A.M
"""

def no_space(x):
    s = ''
    for i in x:
        if i != ' ':
            s+=i
    return s