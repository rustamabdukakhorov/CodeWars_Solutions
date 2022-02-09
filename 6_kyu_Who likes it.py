# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:32:48 2022

@author: R.U.S.T.E.A.M
"""

def likes(names):
    x = names[:]
    l = len(x)
    if x:
        if l==1:
            s = x[0] + " likes this"
        elif l==2:
            s = " and ".join(x) + " like this"
        elif l==3:
            s = ", ".join(x[:(l-1)]) + ' and ' + x[l-1] + " like this"
        else:
            s = ", ".join(x[:2])
            s = f"{s} and {l-2} others like this"
    else:
        s = "no one likes this"
    return s