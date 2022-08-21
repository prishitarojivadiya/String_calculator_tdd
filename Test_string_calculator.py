import unittest
from unittest import result
from String_calculator import String_calculator
class Test_string_calculator(unittest.TestCase):
    def test_empty_string(self):
        result=String_calculator.add("1")
        self.assertEqual(result,0)
        