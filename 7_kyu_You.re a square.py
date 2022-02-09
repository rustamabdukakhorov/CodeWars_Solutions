# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:54:30 2022

@author: R.U.S.T.E.A.M
"""

def is_square(n):    
    if n >= 0: 
        if int(n**0.5)**2 == n:
            return True
        else:
            return False
    else:
        return False