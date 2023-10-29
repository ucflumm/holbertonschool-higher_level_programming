#!/usr/bin/python3
import unittest
"""
    Unit test for Rectangle class
"""
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for Rectangle class """
    def test_id(self):
        """ Test id attribute """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 17)
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        r1 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r1.id, 0)
        r1 = Rectangle(10, 2, 0, 0, -1)
        self.assertEqual(r1.id, -1)
        r1 = Rectangle(10, 2, 0, 0, float('inf'))
        self.assertEqual(r1.id, float('inf'))
        r1 = Rectangle(10, 2, 0, 0, float('NaN'))
        self.assertNotEqual(r1.id, float('NaN'))
        r1 = Rectangle(10, 2, 0, 0, "string")
        self.assertEqual(r1.id, "string")
        r1 = Rectangle(10, 2, 0, 0, [1, 2, 3])
        self.assertEqual(r1.id, [1, 2, 3])
        r1 = Rectangle(10, 2, 0, 0, (1, 2, 3))
        self.assertEqual(r1.id, (1, 2, 3))
        r1 = Rectangle(10, 2, 0, 0, {"a": 1, "b": 2})
        self.assertEqual(r1.id, {"a": 1, "b": 2})
        r1 = Rectangle(10, 2, 0, 0, None)
        self.assertEqual(r1.id, 18)

    def test_width(self):
        """ Test width attribute """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.width, 10)

    def test_height(self):
        """ Test height attribute """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.height, 2)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.height, 2)

    def test_x(self):
        """ Test x attribute """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(2, 10, 3)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.x, 0)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.x, 0)
        with self.assertRaises(TypeError):
            r7 = Rectangle(10, 2, float('NaN'), 0, 0)
        with self.assertRaises(TypeError):
            r8 = Rectangle(10, 2, "string", 0, 0)
        with self.assertRaises(TypeError):
            r9 = Rectangle(10, 2, [1, 2, 3], 0, 0)
        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 2, (1, 2, 3), 0, 0)
        with self.assertRaises(TypeError):
            r11 = Rectangle(10, 2, {"a": 1, "b": 2}, 0, 0)
        with self.assertRaises(TypeError):
            r12 = Rectangle(10, 2, None, 0, 0)

    def test_y(self):
        """ Test y attribute """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10, 3)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.y, 0)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.y, 0)
        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 2, 0, -1, 0)
        with self.assertRaises(TypeError):
            r6 = Rectangle(10, 2, 0, float('inf'), 0)
        with self.assertRaises(TypeError):
            r7 = Rectangle(10, 2, 0, float('NaN'), 0)
        with self.assertRaises(TypeError):
            r8 = Rectangle(10, 2, 0, "string", 0)
        with self.assertRaises(TypeError):
            r9 = Rectangle(10, 2, 0, [1, 2, 3], 0)
        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 2, 0, (1, 2, 3), 0)
        with self.assertRaises(TypeError):
            r11 = Rectangle(10, 2, 0, {"a": 1, "b": 2}, 0)
        with self.assertRaises(TypeError):
            r12 = Rectangle(10, 2, 0, None, 0)

    def test_area(self):
        """ Test area method """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.area(), 20)

    def test_display(self):
        """ Test display method """
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.display(), None)
        r2 = Rectangle(2, 2)
        self.assertEqual(r2.display(), None)
        r3 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r3.display(), None)
        r4 = Rectangle(3, 2, 1, 0)
        self.assertEqual(r4.display(), None)

    def test_str(self):
        """ Test __str__ method """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (25) 1/0 - 5/5")
        r3 = Rectangle(5, 5)
        self.assertEqual(r3.__str__(), "[Rectangle] (26) 0/0 - 5/5")

#    def test_update(self):
#        """ Test update method """
#        r1 = Rectangle(10, 10, 10, 10)
#        self.assertEqual(r1.__str__(), "[Rectangle] (33) 10/10 - 10/10")
#        r1.update(89)
#        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
#        r1.update(89, 2)
#        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
#        r1.update(89, 2, 3)
#        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
#        r1.update(89, 2, 3, 4)
#        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
#        r1.update(89, 2, 3, 4, 5)
#        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
#        r1.update(89, 2, 3, 4, 5, 6)
#        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
#        r1.update(89, 2, 3, 4, 5, 6, 7)
#        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
#        r1.update(89, 2, 3, 4, 5, 6, 7, 8)
#        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
#        r1.update(89, 2, 3, 4, 5, 6, 7, 8, 9)
#        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """ Test update method with **kwargs """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (32) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (32) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (32) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        r1.update(x=1, height=2, y=3, width=4, id=98)
        self.assertEqual(r1.__str__(), "[Rectangle] (98) 1/3 - 4/2")

    def test_to_dictionary(self):
        """ Test to_dictionary method """
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(),
                         {'x': 1, 'y': 9, 'id': 27, 'height': 2, 'width': 10})
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.to_dictionary(),
                         {'x': 0, 'y': 0, 'id': 28, 'height': 1, 'width': 1})
        r3 = Rectangle(1, 1, 1)
        self.assertEqual(r3.to_dictionary(),
                         {'x': 1, 'y': 0, 'id': 29, 'height': 1, 'width': 1})
        r4 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r4.to_dictionary(),
                         {'x': 1, 'y': 1, 'id': 30, 'height': 1, 'width': 1})
        r5 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r5.to_dictionary(),
                         {'x': 1, 'y': 1, 'id': 1, 'height': 1, 'width': 1})

    def test_to_json_string(self):
        """ Test to_json_string method """
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r1.to_json_string(None), "[]")
        self.assertEqual(r1.to_json_string([]), "[]")
        self.assertEqual(r1.to_json_string([{'id': 1}]), '[{"id": 1}]')
        self.assertEqual(r1.to_json_string([{'id': 1}, {'id': 2}]),
                         '[{"id": 1}, {"id": 2}]')
        self.assertEqual(r1.to_json_string([{'id': 1}, {'id': 2}, {'id': 3}]),
                         '[{"id": 1}, {"id": 2}, {"id": 3}]')
        self.assertEqual(r1.to_json_string([{'id': 1}, {'id': 2}, {'id': 3},
                         {'id': 4}]),
                         '[{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]')
        self.assertEqual(r1.to_json_string([{'id': 1}, {'id': 2}, {'id': 3},
                         {'id': 4}, {'id': 5}]),
                         '[{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, \
{"id": 5}]')

    def test_from_json_string(self):
        """ Test from_json_string method """
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r1.from_json_string(None), [])
        self.assertEqual(r1.from_json_string("[]"), [])
        self.assertEqual(r1.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertEqual(r1.from_json_string('[{"id": 1}, {"id": 2}]'),
                         [{"id": 1}, {"id": 2}])
        self.assertEqual(r1.from_json_string('[{"id": 1}, {"id": 2}, \
{"id": 3}]'), [{"id": 1}, {"id": 2}, {"id": 3}])

    def test_create(self):
        """ Test create method """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), "[Rectangle] (8) 1/0 - 3/5")
        self.assertEqual(r2.__str__(), "[Rectangle] (8) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """ Test load_from_file method """
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].__str__(),
                         "[Rectangle] (19) 2/8 - 10/7")
        self.assertFalse(list_rectangles_output[0] is r1)
        self.assertFalse(list_rectangles_output[0] == r1)
        self.assertEqual(list_rectangles_output[0].id, r1.id)
        self.assertEqual(list_rectangles_output[0].width, r1.width)
        self.assertEqual(list_rectangles_output[0].height, r1.height)
        self.assertEqual(list_rectangles_output[0].x, r1.x)
        self.assertEqual(list_rectangles_output[0].y, r1.y)

#   def test_load_from_file_more_than_one(self):
#        """ Test load_from_file method with more than one rectangle """
#        r1 = Rectangle(10, 7, 2, 8)
#        r2 = Rectangle(2, 4)
#        list_rectangles_input = [r1, r2]
#        Rectangle.save_to_file(list_rectangles_input)
#        list_rectangles_output = Rectangle.load_from_file()
#        self.assertEqual(list_rectangles_output[0].__str__(),
#                         "[Rectangle] (17) 2/8 - 10/7")
#        self.assertEqual(list_rectangles_output[1].__str__(),
#                         "[Rectangle] (18) 0/0 - 2/4")
#        self.assertFalse(list_rectangles_output[0] is r1)
#        self.assertFalse(list_rectangles_output[0] == r1)
#        self.assertEqual(list_rectangles_output[0].id, r1.id)
#        self.assertEqual(list_rectangles_output[0].width, r1.width)
#        self.assertEqual(list_rectangles_output[0].height, r1.height)
#        self.assertEqual(list_rectangles_output[0].x, r1.x)
#        self.assertEqual(list_rectangles_output[0].y, r1.y)
#        self.assertFalse(list_rectangles_output[1] is r2)
#        self.assertFalse(list_rectangles_output[1] == r2)
#        self.assertEqual(list_rectangles_output[1].id, r2.id)
#        self.assertEqual(list_rectangles_output[1].width, r2.width)
#        self.assertEqual(list_rectangles_output[1].height, r2.height)
#        self.assertEqual(list_rectangles_output[1].x, r2.x)
#        self.assertEqual(list_rectangles_output[1].y, r2.y)

    def test_load_from_file_more_than_one_same_id(self):
        """ Test load_from_file method with more than one rectangle with same
            id """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].__str__(),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[1].__str__(),
                         "[Rectangle] (2) 0/0 - 2/4")
        self.assertFalse(list_rectangles_output[0] is r1)
        self.assertFalse(list_rectangles_output[0] == r1)
        self.assertEqual(list_rectangles_output[0].id, r1.id)
        self.assertEqual(list_rectangles_output[0].width, r1.width)
        self.assertEqual(list_rectangles_output[0].height, r1.height)
        self.assertEqual(list_rectangles_output[0].x, r1.x)
        self.assertEqual(list_rectangles_output[0].y, r1.y)
        self.assertFalse(list_rectangles_output[1] is r2)
        self.assertFalse(list_rectangles_output[1] == r2)
        self.assertEqual(list_rectangles_output[1].id, r2.id)
        self.assertEqual(list_rectangles_output[1].width, r2.width)
        self.assertEqual(list_rectangles_output[1].height, r2.height)
        self.assertEqual(list_rectangles_output[1].x, r2.x)
        self.assertEqual(list_rectangles_output[1].y, r2.y)

    def test_load_from_file_more_than_one_same_id(self):
        """ Test load_from_file method with more than one rectangle with same
            id """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].__str__(),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[1].__str__(),
                         "[Rectangle] (2) 0/0 - 2/4")
        self.assertFalse(list_rectangles_output[0] is r1)
        self.assertFalse(list_rectangles_output[0] == r1)
        self.assertEqual(list_rectangles_output[0].id, r1.id)
        self.assertEqual(list_rectangles_output[0].width, r1.width)
        self.assertEqual(list_rectangles_output[0].height, r1.height)
        self.assertEqual(list_rectangles_output[0].x, r1.x)
        self.assertEqual(list_rectangles_output[0].y, r1.y)
        self.assertFalse(list_rectangles_output[1] is r2)
        self.assertFalse(list_rectangles_output[1] == r2)
        self.assertEqual(list_rectangles_output[1].id, r2.id)
        self.assertEqual(list_rectangles_output[1].width, r2.width)
        self.assertEqual(list_rectangles_output[1].height, r2.height)
        self.assertEqual(list_rectangles_output[1].x, r2.x)
        self.assertEqual(list_rectangles_output[1].y, r2.y)

    def test_load_from_file_more_than_one_same_id(self):
        """ Test load_from_file method with more than one rectangle with same
            id """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].__str__(),
                         "[Rectangle] (21) 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[1].__str__(),
                         "[Rectangle] (22) 0/0 - 2/4")
        self.assertFalse(list_rectangles_output[0] is r1)
        self.assertFalse(list_rectangles_output[0] == r1)
        self.assertEqual(list_rectangles_output[0].id, r1.id)
        self.assertEqual(list_rectangles_output[0].width, r1.width)
        self.assertEqual(list_rectangles_output[0].height, r1.height)
        self.assertEqual(list_rectangles_output[0].x, r1.x)
        self.assertEqual(list_rectangles_output[0].y, r1.y)
        self.assertFalse(list_rectangles_output[1] is r2)
        self.assertFalse(list_rectangles_output[1] == r2)
        self.assertEqual(list_rectangles_output[1].id, r2.id)
        self.assertEqual(list_rectangles_output[1].width, r2.width)
        self.assertEqual(list_rectangles_output[1].height, r2.height)
        self.assertEqual(list_rectangles_output[1].x, r2.x)
        self.assertEqual(list_rectangles_output[1].y, r2.y)


if __name__ == '__main__':
    unittest.main()
