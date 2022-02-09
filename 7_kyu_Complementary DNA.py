# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:26:07 2022

@author: R.U.S.T.E.A.M
"""

def DNA_strand(dna):
    s = ''
    if dna:
        for i in dna:
            if 'A' == i:
                s+='T'
            elif 'C' == i:
                s+='G'
            elif 'G' == i:
                s+='C'
            elif 'T' == i:
                s+='A'
            else:
                s+=i
        return s
    else:
        return dna