# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:45:26 2022

@author: R.U.S.T.E.A.M
"""

def is_prime(n):
    if n < 2:
        result = False
    else:
        result = True
    for i in range(2, n//2):
        if (n % i == 0):
            return False
    return result