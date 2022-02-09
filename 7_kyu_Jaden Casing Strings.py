# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:30:30 2022

@author: R.U.S.T.E.A.M
"""

def to_jaden_case(string):
    x = string.split(' ')
    for i in range(len(x)):
        x[i] = x[i].capitalize()
    return ' '.join(x)