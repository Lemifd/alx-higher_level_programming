#!/usr/bin/python3
"""This is the say my name module"""


def say_my_name(first_name, last_name=""):
    """function prints name (first name and second name)"""
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
