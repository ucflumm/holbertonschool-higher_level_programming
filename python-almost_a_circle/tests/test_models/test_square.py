#!/usr/bin/python3
import unittest
"""
    Unit test for Square class
"""
from models.square import Square
import io
import sys
import os
from io import StringIO

class TestSquare(unittest.TestCase):
    """
        Test cases for Square class
    """
    def test_id(self):
        """ Test id attribute """
        s1 = Square(10)
        self.assertEqual(s1.id, 70)
        s2 = Square(2)
        self.assertEqual(s2.id, 71)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.id, 12)
        s4 = Square(10, 0, 0, 0)
        self.assertEqual(s4.id, 0)
        s5 = Square(10, 0, 0, -1)
        self.assertEqual(s5.id, -1)
        s6 = Square(10, 0, 0, float('inf'))
        self.assertEqual(s6.id, float('inf'))
        s7 = Square(10, 0, 0, float('NaN'))
        self.assertNotEqual(s7.id, float('NaN'))
        s8 = Square(10, 0, 0, "string")
        self.assertEqual(s8.id, "string")
        s9 = Square(10, 0, 0, [1, 2, 3])
        self.assertEqual(s9.id, [1, 2, 3])
        s10 = Square(10, 0, 0, (1, 2, 3))
        self.assertEqual(s10.id, (1, 2, 3))
        s11 = Square(10, 0, 0, {"a": 1, "b": 2})
        self.assertEqual(s11.id, {"a": 1, "b": 2})
        s12 = Square(10, 0, 0, None)
        self.assertEqual(s12.id, 72)

    def test_size(self):
        """ Test size attribute """
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        s2 = Square(2)
        self.assertEqual(s2.size, 2)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.size, 10)
        s4 = Square(10, 0, 0, 0)
        self.assertEqual(s4.size, 10)
        s5 = Square(10, 0, 0, -1)
        self.assertEqual(s5.size, 10)
        s6 = Square(10, 0, 0, float('inf'))
        self.assertEqual(s6.size, 10)
        s7 = Square(10, 0, 0, float('NaN'))
        self.assertNotEqual(s7.size, float('NaN'))
        s8 = Square(10, 0, 0, "string")
        self.assertEqual(s8.size, 10)
        s9 = Square(10, 0, 0, [1, 2, 3])
        self.assertEqual(s9.size, 10)
        s10 = Square(10, 0, 0, (1, 2, 3))
        self.assertEqual(s10.size, 10)
        s11 = Square(10, 0, 0, {"a": 1, "b": 2})
        self.assertEqual(s11.size, 10)
        s12 = Square(10, 0, 0, None)
        self.assertEqual(s12.size, 10)

    def test_x(self):
        """ Test x attribute """
        s1 = Square(10)
        self.assertEqual(s1.x, 0)
        s2 = Square(2)
        self.assertEqual(s2.x, 0)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.x, 0)
        s4 = Square(10, 0, 0, 0)
        self.assertEqual(s4.x, 0)
        s5 = Square(10, 0, 0, -1)
        self.assertEqual(s5.x, 0)
        s6 = Square(10, 0, 0, float('inf'))
        self.assertEqual(s6.x, 0)
        s7 = Square(10, 0, 0, float('NaN'))
        self.assertNotEqual(s7.x, float('NaN'))
        s8 = Square(10, 0, 0, "string")
        self.assertEqual(s8.x, 0)
        s9 = Square(10, 0, 0, [1, 2, 3])
        self.assertEqual(s9.x, 0)
        s10 = Square(10, 0, 0, (1, 2, 3))
        self.assertEqual(s10.x, 0)
        s11 = Square(10, 0, 0, {"a": 1, "b": 2})
        self.assertEqual(s11.x, 0)
        s12 = Square(10, 0, 0, None)
        self.assertEqual(s12.x, 0)

    def test_y(self):
        """ Test y attribute """
        s1 = Square(10)
        self.assertEqual(s1.y, 0)
        s2 = Square(2)
        self.assertEqual(s2.y, 0)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.y, 0)
        s4 = Square(10, 0, 0, 0)
        self.assertEqual(s4.y, 0)
        s5 = Square(10, 0, 0, -1)
        self.assertEqual(s5.y, 0)
        s6 = Square(10, 0, 0, float('inf'))
        self.assertEqual(s6.y, 0)
        s7 = Square(10, 0, 0, float('NaN'))
        self.assertNotEqual(s7.y, float('NaN'))
        s8 = Square(10, 0, 0, "string")
        self.assertEqual(s8.y, 0)
        s9 = Square(10, 0, 0, [1, 2, 3])
        self.assertEqual(s9.y, 0)
        s10 = Square(10, 0, 0, (1, 2, 3))
        self.assertEqual(s10.y, 0)
        s11 = Square(10, 0, 0, {"a": 1, "b": 2})
        self.assertEqual(s11.y, 0)
        s12 = Square(10, 0, 0, None)
        self.assertEqual(s12.y, 0)

    def test_area(self):
        """ Test area method """
        s1 = Square(10)
        self.assertEqual(s1.area(), 100)
        s2 = Square(2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.area(), 100)
        s4 = Square(10, 0, 0, 0)
        self.assertEqual(s4.area(), 100)
        s5 = Square(10, 0, 0, -1)
        self.assertEqual(s5.area(), 100)
        s6 = Square(10, 0, 0, float('inf'))
        self.assertEqual(s6.area(), 100)
        s7 = Square(10, 0, 0, float('NaN'))
        self.assertNotEqual(s7.area(), float('NaN'))
        s8 = Square(10, 0, 0, "string")
        self.assertEqual(s8.area(), 100)
        s9 = Square(10, 0, 0, [1, 2, 3])
        self.assertEqual(s9.area(), 100)
        s10 = Square(10, 0, 0, (1, 2, 3))
        self.assertEqual(s10.area(), 100)
        s11 = Square(10, 0, 0, {"a": 1, "b": 2})
        self.assertEqual(s11.area(), 100)
        s12 = Square(10, 0, 0, None)
        self.assertEqual(s12.area(), 100)

    def test_display(self):
        """ Test display method """
        s1 = Square(2)
        self.assertEqual(s1.display(), None)
        s2 = Square(2)
        self.assertEqual(s2.display(), None)
        s3 = Square(2, 2, 2, 12)
        self.assertEqual(s3.display(), None)
        s4 = Square(2, 2, 2, 0)
        self.assertEqual(s4.display(), None)
        s5 = Square(2, 2, 2, -1)
        self.assertEqual(s5.display(), None)
        s6 = Square(2, 2, 2, float('inf'))
        self.assertEqual(s6.display(), None)
        s7 = Square(2, 2, 2, float('NaN'))
        self.assertNotEqual(s7.display(), float('NaN'))
        s8 = Square(2, 2, 2, "string")
        self.assertEqual(s8.display(), None)
        s9 = Square(2, 2, 2, [1, 2, 3])
        self.assertEqual(s9.display(), None)
        s10 = Square(2, 2, 2, (1, 2, 3))
        self.assertEqual(s10.display(), None)
        s11 = Square(2, 2, 2, {"a": 1, "b": 2})
        self.assertEqual(s11.display(), None)
        s12 = Square(2, 2, 2, None)
        self.assertEqual(s12.display(), None)
        with self.assertRaises(TypeError):
            s13 = Square(2, None, None, 13)
            s13.display()
        with self.assertRaises(TypeError):
            s14 = Square(2, 3, None, 14)
            s14.display()
        with self.assertRaises(TypeError):
            s15 = Square(2, None, 3, 15)
            s15.display()

    def test_square_display_missing(self):
        """Test - display as expected without x or y"""
        output = StringIO()
        sys.stdout = output
        s = Square(1)
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")

    def test_str(self):
        """ Test __str__ method """
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")
        s2 = Square(5, 1, 0, 0)
        self.assertEqual(s2.__str__(), "[Square] (0) 1/0 - 5")
        s3 = Square(5, 1, 0, -1)
        self.assertEqual(s3.__str__(), "[Square] (-1) 1/0 - 5")
        s4 = Square(5, 1, 0, float('inf'))
        self.assertEqual(s4.__str__(), "[Square] (inf) 1/0 - 5")
        s5 = Square(5, 1, 0, float('NaN'))
        self.assertNotEqual(s5.__str__(), "[Square] (NaN) 1/0 - 5")
        s6 = Square(5, 1, 0, "string")
        self.assertEqual(s6.__str__(), "[Square] (string) 1/0 - 5")
        s7 = Square(5, 1, 0, [1, 2, 3])
        self.assertEqual(s7.__str__(), "[Square] ([1, 2, 3]) 1/0 - 5")
        s8 = Square(5, 1, 0, (1, 2, 3))
        self.assertEqual(s8.__str__(), "[Square] ((1, 2, 3)) 1/0 - 5")
        s9 = Square(5, 1, 0, {"a": 1, "b": 2})
        self.assertEqual(s9.__str__(), "[Square] ({'a': 1, 'b': 2}) 1/0 - 5")
        s10 = Square(5, 1, 0, None)
        self.assertEqual(s10.__str__(), "[Square] (78) 1/0 - 5")

    def test_update(self):
        """ Test update method """
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 10")
        s1.update(89, 2)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/10 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")
        with self.assertRaises(IndexError):
            s1.update(89, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            s1.update(89, 2, 3, 4, 5, 6)
        with self.assertRaises(IndexError):
            s1.update(89, 2, 3, 4, 5, 6, 7)
        with self.assertRaises(IndexError):
            s1.update(89, 2, 3, 4, 5, 6, 7, 8)
        with self.assertRaises(IndexError):
            s1.update(89, 2, 3, 4, 5, 6, 7, 8, 9)
        with self.assertRaises(IndexError):
            s1.update(89, 2, 3, 4, 5, 6, 7, 8, 9, 10)


    def test_to_dictionary(self):
        """ Test to_dictionary method """
        s1 = Square(10, 2, 1, 9)
        self.assertEqual(s1.__str__(), "[Square] (9) 2/1 - 10")
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 9, 'size': 10, 'x': 2, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        self.assertEqual(s2.__str__(), "[Square] (79) 1/0 - 1")
        s2.update(**s1_dictionary)
        self.assertEqual(s2.__str__(), "[Square] (9) 2/1 - 10")
        self.assertNotEqual(s1, s2)
        self.assertEqual(s1_dictionary, s2.to_dictionary())
        s3 = Square(1, 1)
        self.assertEqual(s3.__str__(), "[Square] (80) 1/0 - 1")
        s3.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s3)
        self.assertEqual(s1_dictionary, s3.to_dictionary())
        self.assertNotEqual(s1, s3)
        self.assertEqual(s1_dictionary, s3.to_dictionary())
        s4 = Square(1, 1)
        self.assertNotEqual(s4.__str__(), "[Square] (4) 1/0 - 1")
        s4.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s4)
        self.assertEqual(s1_dictionary, s4.to_dictionary())
        self.assertNotEqual(s1, s4)
        self.assertEqual(s1_dictionary, s4.to_dictionary())
        s5 = Square(1, 1)
        self.assertNotEqual(s5.__str__(), "[Square] (5) 1/0 - 1")
        s5.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s5)
        self.assertEqual(s1_dictionary, s5.to_dictionary())
        self.assertNotEqual(s1, s5)
        self.assertEqual(s1_dictionary, s5.to_dictionary())
        s6 = Square(1, 1)
        self.assertNotEqual(s6.__str__(), "[Square] (6) 1/0 - 1")
        s6.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s6)

    def test_save_to_file(self):
        """ Test save_to_file method """
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 0, 9)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 77)
            Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 2)
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 2)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 39)
        Square.save_to_file([s2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 77)
        Square.save_to_file([s2, s1])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 77)
        with self.assertRaises(TypeError):
            Square.save_to_file([s1, s2], 1)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 77)
        with self.assertRaises(TypeError):
            Square.save_to_file([s1, s2], 2)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 77)
        with self.assertRaises(TypeError):
            Square.save_to_file([s1, s2], 3)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 77)
        with self.assertRaises(TypeError):
            Square.save_to_file([s1, s2], 4)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 77)
        with self.assertRaises(TypeError):
            Square.save_to_file([s1, s2], 5)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 77)
        with self.assertRaises(TypeError):
            Square.save_to_file([s1, s2], 6)

    def test_extra_tests(self):
        """ Extra tests """
        with self.assertRaises(TypeError):
            s1 = Square("1")
        with self.assertRaises(ValueError):
            s2 = Square(-1)
        with self.assertRaises(ValueError):
            s3 = Square(1, -2)
        with self.assertRaises(ValueError):
            s4 = Square(1, 2, -3)
        with self.assertRaises(ValueError):
            s5 = Square(0)

    def test_create(self):
        """ Test create method """
        s1 = Square(3, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1.__str__(), "[Square] (9) 2/1 - 3")
        self.assertEqual(s2.__str__(), "[Square] (9) 2/1 - 3")
        self.assertNotEqual(s1, s2)
        self.assertEqual(s1_dictionary, s2.to_dictionary())
        s3 = Square(3, 2, 1, 9)
        s3_dictionary = s3.to_dictionary()
        s4 = Square.create(**s3_dictionary)
        self.assertEqual(s3.__str__(), "[Square] (9) 2/1 - 3")
        self.assertEqual(s4.__str__(), "[Square] (9) 2/1 - 3")
        self.assertNotEqual(s3, s4)
        self.assertEqual(s3_dictionary, s4.to_dictionary())
        s5 = Square(3, 2, 1, 9)
        s5_dictionary = s5.to_dictionary()
        s6 = Square.create(**s5_dictionary)
        self.assertEqual(s5.__str__(), "[Square] (9) 2/1 - 3")
        self.assertEqual(s6.__str__(), "[Square] (9) 2/1 - 3")
        self.assertNotEqual(s5, s6)
        self.assertEqual(s5_dictionary, s6.to_dictionary())
        s7 = Square(3, 2, 1, 9)
        s7_dictionary = s7.to_dictionary()
        s8 = Square.create(**s7_dictionary)
        self.assertEqual(s7.__str__(), "[Square] (9) 2/1 - 3")
        self.assertEqual(s8.__str__(), "[Square] (9) 2/1 - 3")
        self.assertNotEqual(s7, s8)
        self.assertEqual(s7_dictionary, s8.to_dictionary())
        s9 = Square(3, 2, 1, 9)
        s9_dictionary = s9.to_dictionary()

    def test_square_save_to_file_empty(self):
        """Test - saves empty square to file"""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file([])
        with open("Square.json", 'r', encoding="utf-8") as file:
            s = file.read()
            self.assertEqual(s, '[]')
            os.remove("Square.json")

    def test_save_to_file_none(self):
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            square_1 = file.read()
            self.assertEqual(square_1, "[]")

        def test_square_save_to_file(self):
            """Test - save square to file"""
        Square.save_to_file([Square(1, 2)])
        with open("Square.json", 'r', encoding="utf-8") as file:
            s = file.read()
        self.assertEqual(s, '[{"id": 73, "size": 1, "x": 2, "y": 0}]')
        os.remove("Square.json")

    def test_square_load_no_file(self):
        """Test - load from non-existent file"""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        self.assertEqual(Square.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()


# missing Test of Square.save_to_file([]) in Square exists
# missing Test of Square.load_from_file() when file doesn’t exist exists
# Test of Square.load_from_file() when file exists exists
