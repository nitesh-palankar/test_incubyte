from string_calculator import string_calculator
import unittest


class TestStringCalculator(unittest.TestCase):
    def test_string_calculator_with_empty_string(self):
        """
        This test method is used to check,
             if input_string is empty:
                then string_calculator() function should return 0
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator(""), 0)

    def test_string_calculator_without_delimiter_and_with_single_number(self):
        """
        This test method is used to check,
             if input_string contains only one number and No delimiter:
                then string_calculator() function simply returns that number
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("1"), 1)

    def test_string_calculator_with_only_comma_delimiter(self):
        """
        This test method is used to check,
             if input_string is comma separated:
                then string_calculator() function should separate numbers on
                     basis of comma and add them as final output
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("1,2"), 3)


if __name__ == '__main__':
    unittest.main()
