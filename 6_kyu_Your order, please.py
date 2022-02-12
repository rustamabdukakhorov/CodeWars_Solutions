# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 00:24:32 2022

@author: R.U.S.T.E.A.M
"""

def order(sentence):
    l = sentence.split(" ")
    x = []
    for i in l:
        for j in i:
            if 48<=ord(j)<=58:
                x.append(j + i)
    x.sort()
    l = [i[1:] for i in x]
    if sentence:
        return " ".join(l)
    else:
        return ""