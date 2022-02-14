# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:35:23 2022

@author: R.U.S.T.E.A.M
"""

def make_readable(seconds):
    x = [0,0,0]
    sec, men, hor = seconds%60, (seconds//60)%60, (seconds//3600)%100
    x[2] = (2 - len(str(sec)))*'0' + str(sec)
    x[1] = (2 - len(str(men)))*'0' + str(men)
    x[0] = (2 - len(str(hor)))*'0' + str(hor)
    return ':'.join(x)