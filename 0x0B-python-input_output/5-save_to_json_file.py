#!/usr/bin/python3
"""defines the function save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """writes an objct to a text file
    with utf-8
    """
    with open(filename, "w", encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
