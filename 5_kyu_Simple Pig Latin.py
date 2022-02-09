# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:32:08 2022

@author: R.U.S.T.E.A.M
"""

def pig_it(text):
    s = text[:]
    x = s.split(' ')
    l = []
    for i in x:
        if len(i) != 1:
            l.append(i[1:] + i[0] + 'ay')
        else:
            if i.lower() in list(map(chr, range(97,123))):
                l.append(i[1:] + i[0] + 'ay')
            else:
                l.append(i)
    s = ' '.join(l)
    return s