# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:30:49 2022

@author: R.U.S.T.E.A.M
"""

def get_middle(s):
    l = len(s)
    if l==1 or l==2:
        return s
    else:
        if l%2 == 1:
            return s[l//2]
        else:
            return s[(l//2 - 1): (l//2 + 1)]