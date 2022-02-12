# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:40:58 2022

@author: R.U.S.T.E.A.M
"""

def add_binary(a,b):
    a = a + b
    b = ''
    while a > 0:
        b += str(a%2)
        a //=2
    if b[::-1]:
        return b[::-1]
    else:
        return '0'