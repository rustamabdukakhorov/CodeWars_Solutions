# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:22:44 2022

@author: R.U.S.T.E.A.M
"""

def duplicate_count(text):
    if text:
        s = [i for i in text.lower()]
        s.sort()
        text = ''.join(s)
        w = [text[0]]
        for i in range(len(text)-1):
            if text[i] != text[i+1]:
                w.append(text[i+1])
        k = 0
        for i in w:
            if text.count(i) > 1:
                k += 1
        return k
    else:
        return 0