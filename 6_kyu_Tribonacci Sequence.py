# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:36:41 2022

@author: R.U.S.T.E.A.M
"""

def tribonacci(signature, n):
    #your code here
    fib = []
    fib = signature
    if n>=1 and n<=3:
        return fib[0:n]
    else:
        x = int()
        for x in range(3,n):
            fib.append(fib[x-3]+fib[x-2]+fib[x-1])
        return fib[0:n]