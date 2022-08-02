#!/usr/bin/python3
"""module contains the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """returns true if the object is an instance of a_class
    or if objecgt is an instance of inherited class
    otherwise return false
    """
    return isinstance(obj, a_class)
