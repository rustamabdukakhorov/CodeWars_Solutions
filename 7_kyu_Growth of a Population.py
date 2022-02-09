# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:21:20 2022

@author: R.U.S.T.E.A.M
"""

def nb_year(p0, percent, aug, p):
    i = 0
    n_p = p0
    while n_p < p:
        n_p = n_p + (n_p * percent)//100 + aug
        i += 1
    return i