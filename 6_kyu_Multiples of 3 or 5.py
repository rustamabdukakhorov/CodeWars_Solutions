# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:56:27 2022

@author: R.U.S.T.E.A.M
"""

def solution(number):
    s = 0
    for i in range(number):
        if i%3 == 0 or i%5 == 0:
            s+=i
    return s