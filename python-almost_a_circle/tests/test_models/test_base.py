#!/usr/bin/python3
import unittest
"""
    Unit test for Base class
"""
from models.base import Base
import io
import sys
import os


class TestBase(unittest.TestCase):
    """ Test cases for Base class """
    def test_id(self):
        """ Test id attribute """
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b5 = Base(-1)
        self.assertEqual(b5.id, -1)
        b6 = Base(0)
        self.assertEqual(b6.id, 0)
        b7 = Base(12.5)
        self.assertEqual(b7.id, 12.5)
        b8 = Base("string")
        self.assertEqual(b8.id, "string")
        b9 = Base([1, 2, 3])
        self.assertEqual(b9.id, [1, 2, 3])
        b10 = Base((1, 2, 3))
        self.assertEqual(b10.id, (1, 2, 3))
        b11 = Base({"a": 1, "b": 2})
        self.assertEqual(b11.id, {"a": 1, "b": 2})
        b13 = Base(float('inf'))
        self.assertEqual(b13.id, float('inf'))
        b14 = Base(float('NaN'))
        self.assertNotEqual(b14.id, float('NaN'))

    def test_to_json_string(self):
        """
            Test to_json_string method
        """
        b1 = Base()
        self.assertEqual(b1.to_json_string(None), "[]")
        self.assertEqual(b1.to_json_string([]), "[]")
        self.assertEqual(b1.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(b1.to_json_string([{"id": 1}, {"id": 2}]),
                         '[{"id": 1}, {"id": 2}]')
        self.assertEqual(b1.to_json_string([{"id": 1}, {"id": 2}, {"id": 3}]),
                         '[{"id": 1}, {"id": 2}, {"id": 3}]')
        self.assertEqual(b1.to_json_string([{"id": 1}, {"id": 2}, {"id": 3},
                                           {"id": 4}]),
                         '[{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]')
        self.assertEqual(b1.to_json_string([{"id": 1}, {"id": 2}, {"id": 3},
                         {"id": 4}, {"id": 5}]),
                         '[{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, \
{"id": 5}]')

    def test_from_json_string(self):
        """
            Test from_json_string method
        """
        b1 = Base()
        self.assertEqual(b1.from_json_string(None), [])
        self.assertEqual(b1.from_json_string("[]"), [])
        self.assertEqual(b1.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertEqual(b1.from_json_string('[{"id": 1}, {"id": 2}]'),
                         [{"id": 1}, {"id": 2}])
        self.assertEqual(b1.from_json_string('[{"id": 1}, {"id": 2}, \
{"id": 3}]'), [{"id": 1}, {"id": 2}, {"id": 3}])
        self.assertEqual(b1.from_json_string('[{"id": 1}, {"id": 2}, \
{"id": 3}, {"id": 4}]'), [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}])
        self.assertEqual(b1.from_json_string('[{"id": 1}, {"id": 2}, \
{"id": 3}, {"id": 4}, {"id": 5}]'),
                         [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4},
                          {"id": 5}])

# missing Test of display() without x and y exists
# missing Test of display() without y exists
# missing Test of display() exists
    if __name__ == "__main__":
        unittest.main()
