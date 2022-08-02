#!/usr/bin/python3
"""defines the function json_string"""


import json


def to_json_string(my_obj):
    """returns JSON representation of an object"""
    return json.dumps(my_obj)
