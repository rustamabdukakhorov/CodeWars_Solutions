# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:32:29 2022

@author: R.U.S.T.E.A.M
"""

def find_it(seq):
    x = seq[:]
    x.sort()
    m = [x[0]]
    for i in range(1,len(x)-1):
        if x[i] != x[i+1]:
            m.append(x[i+1])
    l = []
    for i in m:
        if x.count(i)%2 == 1:
            return i