# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:24:21 2022

@author: R.U.S.T.E.A.M
"""

def maskify(cc):
    if len(cc)<=4:
        return cc
    else:
        return '#'*(len(cc)-4) + cc[-4:]