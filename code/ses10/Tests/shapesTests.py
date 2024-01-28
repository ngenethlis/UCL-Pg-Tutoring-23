import unittest
import parameterized
from shapes import Rectangle, Square


class TestRectangle(unittest.TestCase):

    @parameterized.parameterized.expand([
        (2, 3, 10),
        (1, 1, 4),
        (5, 10, 30),
        (0.5, 0.5, 2)
    ])
    def test_getPerimeter(self, height, width, area):
        rect = Rectangle(height, width)
        self.assertEqual(rect.getPerimeter(), area)

    @parameterized.parameterized.expand([
        (2, 3, 6),
        (1, 1, 1),
        (5, 10, 50),
        (0.5, 0.5, 0.25)
    ])
    def test_getArea(self, height, width, area):
        rect = Rectangle(height, width)
        self.assertEqual(rect.getArea(), area)


    def test_negHeight(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
    def test_negWidth(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -1)


    def test_negHeightWidth(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, -1)

