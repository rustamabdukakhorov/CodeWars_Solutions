# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:54:13 2022

@author: R.U.S.T.E.A.M
"""

def high_and_low(numbers):
    x = numbers.split()
    for i in range(len(x)):
        x[i] = int(x[i])
    x.sort()
    return f"{x[-1]} {x[0]}"