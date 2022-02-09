# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:19:48 2022

@author: R.U.S.T.E.A.M
"""

def longest(a1, a2):
    s = [i for i in (a1+a2)]
    s.sort()
    x = [s[0]]
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            x.append(s[i+1])
    return ''.join(x)