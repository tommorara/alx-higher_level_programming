#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        """Test with regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([]))

    def test_with_floats(self):

        """Test with floats in the list"""
        self.assertEqual(max_integer([1.5, 2.3, 3.1]), 3.1)
        self.assertEqual(max_integer([-1.5, -2.3, -3.1]), -1.5)
        self.assertEqual(max_integer([1.5, 2, 3]), 3)

    def test_with_strings(self):
        """Test with strings in the list"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")
        self.assertEqual(max_integer(["alpha", "beta", "gamma"]), "gamma")

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["My", "name", "is", "Emyjakarta"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)
