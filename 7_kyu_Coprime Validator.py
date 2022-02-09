# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:44:28 2022

@author: R.U.S.T.E.A.M
"""

def are_coprime(n,m):
    def f(n):
        ls = []
        for i in range(2,n+1):
            if n%i == 0:
                ls.append(i)
        return ls
    result = False
    a = f(n) + f(m)
    a.sort()
    for x in range(1,len(a)):
        if a[x-1] == a[x]:
            return False
        else:
            result = True
    return result