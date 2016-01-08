# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:51:38 2016

@author: pchambers
"""

def sum_custom(n):
    """
    Given an integer n:
    - return the sum from 0 to n if n >= 0
    - return -1 for n < 0
    - raise a TypeError if a is not of type int
    """
    if type(n) is not int:
        raise TypeError("f(n) expects integer, not {}".format(type(n)))
        
    if n >= 0:
        s = 0
        for i in range(1, n + 1):
            s = s + i
        return s
    else:
        return -1
