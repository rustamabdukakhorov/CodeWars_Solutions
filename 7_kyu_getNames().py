# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:44:11 2022

@author: R.U.S.T.E.A.M
"""

def get_names(data):
    ls = []
    for x in range(len(data)):
        ls.append(data[x].get('name'))
    return ls