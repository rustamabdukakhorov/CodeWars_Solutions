# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:53:54 2022

@author: R.U.S.T.E.A.M
"""

def square_digits(num):
    s = ''
    num = str(num)
    for i in range(len(num)):
        s += str(int(num[i])**2)
    return int(s) 