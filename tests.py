import unittest
from converter import roman_to_decimal


class TestConverter(unittest.TestCase):
    def test_basic_convertion(self):
        self.assertEqual(8, roman_to_decimal('VIII'))

    def test_large_number_conversion(self):
        self.assertEqual(3918, roman_to_decimal('MMMCMXVIII'))

    def test_too_many_x(self):
        self.assertEqual('not a valid Roman number', roman_to_decimal('XXXXX'))

    def test_incorrect_subtraction(self):
        self.assertEqual('not a valid Roman number', roman_to_decimal('IC'))

    def test_multiple_subtraction(self):
        self.assertEqual('not a valid Roman number', roman_to_decimal('XCM'))

    def test_convert_empty(self):
        self.assertEqual('there is no number', roman_to_decimal(''))

    def test_repeating_subtraction(self):
        self.assertEqual('not a valid Roman number', roman_to_decimal('XCXCXCXC'))
