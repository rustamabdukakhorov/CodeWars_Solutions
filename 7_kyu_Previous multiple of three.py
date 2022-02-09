# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:46:23 2022

@author: R.U.S.T.E.A.M
"""

def prev_mult_of_three(n):
    if n%3==0:
        return n
    else:
        a = None
        while n > 9:
            n = n//10
            if n%3==0:
                return n
        return a