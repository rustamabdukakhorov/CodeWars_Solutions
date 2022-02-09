# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:20:36 2022

@author: R.U.S.T.E.A.M
"""

def is_triangle(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        return True
    else:
        return False