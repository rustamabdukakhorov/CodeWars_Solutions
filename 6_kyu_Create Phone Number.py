# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:34:10 2022

@author: R.U.S.T.E.A.M
"""

def create_phone_number(n):
    s = ''
    for i in n:
        s += str(i)
    number = f"({s[:3]}) {s[3:6]}-{s[6:]}"
    return number