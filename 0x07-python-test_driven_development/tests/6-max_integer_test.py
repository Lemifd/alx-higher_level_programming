#!/usr/bin/python3
"""Unittest for max_integer"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class Max_integer_test(unittest.TestCase):
    """provide test cases for max_integer"""

    def test_ordered_list(self):
        """test an ordered list"""
        ordered_list = [1, 2, 3, 4]
        result = max_integer(ordered_list)
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """test an unordered list"""
        unordered_list = [3, 1, 4, 2]
        result = max_integer(unordered_list)
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """test an empty list"""
        empty_list = []
        result = max_integer(empty_list)
        self.assertEqual(result, None)

    def test_list_with_one_item(self):
        """test a list with one item"""
        one_item_list = [3]
        result = max_integer(one_item_list)
        self.assertEqual(result, 3)

    def test_list_of_floats(self):
        """test a list of floating numbers"""
        float_list = [1.22, 4.5, 2.3, 0.5]
        result = max_integer(float_list)
        self.assertEqual(result, 4.5)

    def test_list_of_char(self):
        """test a list of characters"""
        char_list = ["c", "r", "n", "e"]
        result = max_integer(char_list)
        self.assertEqual(result, "r")

    def test_list_of_string(self):
        """test a list of string"""
        string_list = ["home", "none", "list", "find", "risk"]
        result = max_integer(string_list)
        self.assertEqual(result, "risk")

    def test_ints_and_floats(self):
        """test a mixed list of float and integer"""
        int_float_list = [10, -3, 2.5, 18, -19, 23.5]
        result = max_integer(int_float_list)
        self.assertEqual(result, 23.5)

    def test_string(self):
        """test a string"""
        string = "python"
        result = max_integer(string)
        self.assertEqual(result, "y")

    def test_empty_string(self):
        """test an empty string"""
        result = max_integer("")
        self.assertEqual(result, None)
