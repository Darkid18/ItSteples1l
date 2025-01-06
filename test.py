import unittest
from lesson8 import *

class My_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2), 4)
    def test_kwargs(self):
        self.assertEqual(adder(a = 10,b = 1), 11)
    def test_mixed(self):
        self.assertEqual(adder(1,a = 2), 3)
    def test_diff(self):
        self.assertEqual(adder(0, -5, y, a=x), x + y)
    def test_wrong(self):
        self.assertEqual(adder("5", "abc", "c", 10), 15)