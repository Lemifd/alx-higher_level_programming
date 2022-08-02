#!/usr/bin/python3
"""contains the Mylist class"""


class MyList(list):
    """this is a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
