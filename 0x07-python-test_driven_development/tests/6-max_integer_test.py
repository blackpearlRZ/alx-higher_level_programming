#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_value(self):
        """ Test random order list """
        self.assertEqual(max_integer([65, 54, 98, 51, 0, -65]), 98)

        """ Test max integer at the beginning """
        self.assertEqual(max_integer([98, 65, 54, 51, 0, -65]), 98)

        """ Test max integer at the end """
        self.assertEqual(max_integer([65, 54, 51.54, 0, -65, 98]), 98)

        """ Test negative integers list """
        self.assertEqual(max_integer([-15, -848.54, -65, -2]), -2)

        """ Test empty list """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

        """ Test a string """
        self.assertEqual(max_integer(
            "This test file just broke my brain"), "y")

        """ Test a list with a string(s) in it """
        self.assertEqual(max_integer(["one", "two", "three"]), "two")

        """ Test a list of lists """
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])


if __name__ == '__main__':
    unittest.main()
