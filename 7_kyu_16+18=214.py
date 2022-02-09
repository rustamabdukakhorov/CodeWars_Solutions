# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:46:03 2022

@author: R.U.S.T.E.A.M
"""

def add(num1, num2):
    num1, num2 = str(num1), str(num2)
    if len(num1) > len(num2):
        num2 = '0'*(len(num1) - len(num2)) + num2
    else:
        num1 = '0'*(len(num2) - len(num1)) + num1
    l = max(len(num1), len(num2))
    ans = ''
    for i in range(l):
        ans += str(int(num1[i])+int(num2[i]))
    return int(ans)