"""Peter Rasmussen, Lab 4, memoize.py

This module provides a memoization class that is used to handle issue of hitting maximum recursion
depth.

Class obtained from source cited below.
“Python - anyone have a memoizing decorator that can handle unhashable arguments?" Stack Overflow, 26 April 2021,
https://stackoverflow.com/questions/4669391/python-anyone-have-a-memoizing-decorator-that-can-handle-unhashable-arguments
"""
# Standard library imports
import pickle
import sys


sys.setrecursionlimit(20000)


class MemoizeMutable:
    """
    Memoize mutable objects (e.g., lists).
    Class obtained from source cited below.
    “Python - anyone have a memoizing decorator that can handle unhashable arguments?" Stack Overflow, 26 April 2021,
    https://stackoverflow.com/questions/4669391/python-anyone-have-a-memoizing-decorator-that-can-handle-unhashable-arguments
    """
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args, **kwargs):
        k = pickle.dumps(args, 1) + pickle.dumps(kwargs, 1)
        if not k in self.memo:
            self.memo[k] = self.fn(*args, **kwargs)
        return self.memo[k]