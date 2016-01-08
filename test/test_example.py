# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:45:48 2016

@author: pchambers
"""
from my_pymodule.functions import sum_custom, product_custom
import pytest


def test_positive():
    # partitioning n
    assert sum_custom(2) == 0 + 1 + 2
    assert sum_custom(3) == 0 + 1 + 2 + 3
    assert sum_custom(5) == 15
    assert sum_custom(10) == 55


def test_negative():
    assert sum_custom(-1) == -1
    assert sum_custom(-10) == -1


def test_border_case():
    assert sum_custom(1) == 1
    assert sum_custom(0) == 0
    assert sum_custom(-1) == -1
    assert sum_custom(-2) == -1


def test_raises_exception():
    with pytest.raises(TypeError):
        sum_custom(1.0)
    with pytest.raises(TypeError):
        sum_custom("This is a string")


def test_failure():
    """tests a feature of the function sum_custom which does not exist:
    This is just to test Jenkins will throw a bad build message"""
    assert product_custom(2) == 1*2
