#!/usr/bin/python3
"""module contains function is_same_class"""


def is_same_class(obj, a_class):
    """function returns true if object is instance
    of a_class
    otherwise it returns false
    """
    return type(obj) == a_class
