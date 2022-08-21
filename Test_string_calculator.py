import string
import unittest
from unittest import expectedFailure, result
from unittest.case import _AssertRaisesContext
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
    def test_multiple_coma_seperated_alphanumeric_string(self):
        result=String_calculator.add("1,2,a,c")
        self.assertEqual(result,7)
    #def test_negative_value_raise_exception(self):
    #    result=String_calculator.add("1,-1,2,3")
    #    expected = -1
    #    self.assertEqual(result,expected)
    def test_morethanthousand_should_be_ignored(self):
        result=String_calculator.add("1000,1001")
        self.assertEqual(result,1000) 
           
        