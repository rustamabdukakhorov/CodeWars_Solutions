# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:21:00 2022

@author: R.U.S.T.E.A.M
"""

def two_sum(numbers, target):
    num_lst = list(range(len(numbers)))
    
    for indx, num in enumerate(num_lst):
        for num_other in num_lst[indx+1:]:
            if numbers[num] + numbers[num_other] == target:
                return [num, num_other]
            else: 
                continue
    return None