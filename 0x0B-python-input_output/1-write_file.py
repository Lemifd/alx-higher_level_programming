#!/usr/bin/python3
"""defining the function write_file"""


def write_file(filename="", text=""):
    """reads filename with utf-8"""
    with open(filename, "w", encoding='utf-8') as my_file:
        return my_file.write(text)
