#!/usr/bin/python3
"""defining function append_write"""


def append_write(filename="", text=""):
    """reads filename with utf-8"""
    with open(filename, "a", encoding='utf-8') as my_file:
        return my_file.write(text)
