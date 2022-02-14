# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:39:35 2022

@author: R.U.S.T.E.A.M
"""

def rgb(r, g, b):
    if r > 255:
        r = 255
    elif r < 0:
        r = 0
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    if b > 255:
        b = 255
    elif b < 0:
        b = 0
    r = hex(r).replace('0x','')
    g = hex(g).replace('0x','')
    b = hex(b).replace('0x','')
    s = (2-len(r))*'0' + r + (2-len(g))*'0' + g + (2-len(b))*'0' + b
    return s.upper()