# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:45:48 2016

@author: pchambers
"""
from my_pymodule.functions import sum_custom as f
import pytest


def test_positive():
    # partitioning n
    assert f(2) == 0 + 1 + 2
    assert f(3) == 0 + 1 + 2 + 3
    assert f(5) == 15
    assert f(10) == 55


def test_negative():
    assert f(-1) == -1
    assert f(-10) == -1


def test_border_case():
    assert f(1) == 1
    assert f(0) == 0
    assert f(-1) == -1
    assert f(-2) == -1


def test_raises_exception():
    with pytest.raises(TypeError):
        f(1.0)
    with pytest.raises(TypeError):
        f("This is a string")
