import string
import unittest
from unittest import result
from String_calculator import String_calculator
class Test_string_calculator(unittest.TestCase):
    def test_empty_string(self):
        result=String_calculator.add("")
        self.assertEqual(result,0)
    def test_one_string(self):
        result=String_calculator.add("1")
        self.assertEqual(result,1)
    def test_multiple_coma_seperated_string(self):
        result=String_calculator.add("1,2,3")
        self.assertEqual(result,6)
    
        