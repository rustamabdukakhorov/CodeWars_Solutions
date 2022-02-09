# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:53:09 2022

@author: R.U.S.T.E.A.M
"""

def abbrev_name(name):
    l = name.upper()
    n = l.split()
    return f"{n[0][0]}.{n[1][0]}"