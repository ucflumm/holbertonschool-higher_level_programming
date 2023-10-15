#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function"""

    def test_max(self):
        """Test for max_integer function"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 70000]), 70000)
        self.assertEqual(max_integer([1, 3, 4, 4]), 4)
        self.assertEqual(max_integer([4, 3, 4, 2]), 4)
    def test_empty(self):
        """Test for max_integer function"""
        self.assertEqual(max_integer([]), None)
        self.assertIsNone(max_integer([]))
    def test_mixed_sign_int(self):
        """Test for max_integer function"""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -3, 4, 70000]), 70000)
        self.assertEqual(max_integer([1, -3, 4, 4]), 4)
        self.assertEqual(max_integer([4, -3, 4, 2]), 4)
    def test_negative(self):
        """Test for max_integer function"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -4, -2]), -2)
    def test_single_element(self):
        """Test for max_integer function"""
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([0]), 0)
    def test_string(self):
        """Test for max_integer function"""
        self.assertEqual(max_integer(["hello", "world"]), "world")
        self.assertEqual(max_integer(["hello", "world", "hi", "longlongstring", "zebra"]), "zebra")
        self.assertEqual(max_integer(["hello", "world", "hi", "longlongstring", "zebra", ""]), "zebra")

if __name__ == '__main__':
    unittest.main()
