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


if __name__ == '__main__':
    unittest.main()
