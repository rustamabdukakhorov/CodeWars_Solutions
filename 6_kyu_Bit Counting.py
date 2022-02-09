# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:23:31 2022

@author: R.U.S.T.E.A.M
"""

def count_bits(n):
    s = bin(n).replace("0b", "")
    s = str(s)
    return s.count('1')