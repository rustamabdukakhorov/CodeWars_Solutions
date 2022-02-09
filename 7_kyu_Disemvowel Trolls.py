# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:53:24 2022

@author: R.U.S.T.E.A.M
"""

def disemvowel(string_):
    n = ""
    l = ['a','e','o','i','u','A','E','O','I','U']
    for i in range(len(string_)):
        if string_[i] not in l:
            n += string_[i]
    return n