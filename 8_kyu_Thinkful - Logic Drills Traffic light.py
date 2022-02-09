# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:37:39 2022

@author: R.U.S.T.E.A.M
"""

def update_light(current):
    r, g, y = 'red', 'green', 'yellow'
    if current == r:
        return g
    elif current == y:
        return r
    else:
        return y
    