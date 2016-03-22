import sys
import unittest

from say_hello import *

class TestMorning(unittest.TestCase):

    def test_say_hello_with_args(self):
        self.assertEqual(say_hello("Haviva"), "Hello Haviva!")
        self.assertEqual(say_hello("Ricardo"), "Hello Ricardo!")
        self.assertEqual(say_hello("Larry"), "Hello Larry!")

    def test_say_hello_with_args(self):
        self.assertEqual(say_hello(), "Hello Python Programmer!")


if __name__ == '__main__':
    unittest.main()
