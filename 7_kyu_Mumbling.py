# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:56:07 2022

@author: R.U.S.T.E.A.M
"""

def accum(s):
    s = s.lower()
    l = []
    for i in range(len(s)):
        l.append(s[i]*(i+1))
    for i in range(len(l)):
        l[i] = l[i].capitalize()
    ans = '-'.join(l)
    return ans