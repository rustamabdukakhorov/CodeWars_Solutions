# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:38:00 2022

@author: R.U.S.T.E.A.M
"""

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result