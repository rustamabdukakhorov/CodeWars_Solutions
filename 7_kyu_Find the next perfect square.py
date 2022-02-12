# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:40:35 2022

@author: R.U.S.T.E.A.M
"""

def find_next_square(sq):
    if int(sq**0.5) **2 != sq:
        return -1
    else:
        return (int(sq**0.5) + 1)**2
