# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:52:41 2022

@author: R.U.S.T.E.A.M
"""

def validate_pin(pin):
    number = [i for i in range(48, 58)]
    if len(pin) in [4, 6]:
        pin = [i for i in pin]
        for i in pin:
            if not ord(i) in number:
                return False
        return True
    else:
        return False