# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:42:59 2022

@author: R.U.S.T.E.A.M
"""

def grid(N):
    text = ''
    if N < 0:
            return None
    else:
        for j in range(N):
            ch = 97 + j%26
            for i in range(N):
                text+=chr((97 + ((ch + i%26)%97)%26))
                if i != N-1:
                    text+=' '
                else:
                    text+='\n'
    return text[:-1]