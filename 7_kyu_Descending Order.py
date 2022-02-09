# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:55:18 2022

@author: R.U.S.T.E.A.M
"""

def descending_order(num):
    s = str(num)

    s = sorted(s)

    s = reversed(s)

    ans = ''.join(s)

    return int(ans)