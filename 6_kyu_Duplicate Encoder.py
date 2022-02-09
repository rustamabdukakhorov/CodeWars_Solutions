# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:22:13 2022

@author: R.U.S.T.E.A.M
"""

def duplicate_encode(word):
    text = word.lower()
    s = ''
    for i in text:
        if text.count(i) > 1:
            s+=')'
        else:
            s+='('
    return s