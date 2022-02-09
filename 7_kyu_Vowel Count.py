# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:50:03 2022

@author: R.U.S.T.E.A.M
"""

def get_count(sentence):
    s = 0
    l = ['a','e','i','o','u']
    for i in sentence:
        if i in l:
            s+=1
    return s