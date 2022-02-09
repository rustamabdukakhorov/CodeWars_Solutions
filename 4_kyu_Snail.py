# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:28:05 2022

@author: R.U.S.T.E.A.M
"""

def snail(snail_map):
    array = snail_map[:]
    if array:
        if len(array) == 1:
            return array[0]
        else:
            m = len(array)
            x = []
            while len(array)>1:
                l = len(array)
                for i in range(l):
                    x.append(array[0][i])
                for i in range(1,l):
                    x.append(array[i][l-1])
                for i in range(l-2,-1,-1):
                    x.append(array[l-1][i])
                for i in range(l-2,0,-1):
                    x.append(array[i][0])
                array = [i[1:-1] for i in array[1:-1]]
                if len(array) == 1:
                    x.append(array[0][0])
            return x
    else:
        return []