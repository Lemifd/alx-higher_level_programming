#!/usr/bin/python3
"""module contains the function inherit_from"""


def inherits_from(obj, a_class):
    """returns true if an object is instance of a_class
    inherited directly or indirectly from a class
    otehrwise return false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
