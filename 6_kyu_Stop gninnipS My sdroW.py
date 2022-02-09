# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:23:59 2022

@author: R.U.S.T.E.A.M
"""

def spin_words(sentence):
    s = sentence.split(' ')
    x = []
    for i in s:
        if len(i)>4:
            x.append(i[::-1])
        else:
            x.append(i)
    return ' '.join(x)