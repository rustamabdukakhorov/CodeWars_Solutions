# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:50:58 2022

@author: R.U.S.T.E.A.M
"""

def century(year):
    if year%100 == 0:
        return int(year//100)
    else:
        return int(year//100 + 1)