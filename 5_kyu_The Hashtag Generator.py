# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:43:38 2022

@author: R.U.S.T.E.A.M
"""

def generate_hashtag(s):
    if s == '' or len(s) >=140:
        return False
    else:
        ls = s.split(' ')
        result = '#'
        for ch in ls:
            result += ch.capitalize()
        return result