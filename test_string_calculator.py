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

    def test_string_calculator_with_only_comma_delimiter_two_numbers(self):
        """
        This test method is used to check,
             if input_string is comma separated(only two numbers):
                then string_calculator() function should separate numbers on
                     basis of comma and add them as final output
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("1,2"), 3)

    def test_string_calculator_with_only_comma_delimiter_multiple_numbers(self):
        """
        This test method is used to check,
             if input_string is comma separated(multiple numbers):
                then string_calculator() function should separate numbers on
                     basis of comma and add them as final output
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("1,2,7,5"), 15)

    def test_string_calculator_with_comma_newline_delimiter(self):
        """
        This test method is used to check,
             if input_string is comma or newline separated:
                then string_calculator() function should separate numbers on
                     basis of comma or newline and add them as final output
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("1,2\n5"), 8)
        self.assertEqual(string_calculator("1\n2,5"), 8)
        self.assertEqual(string_calculator("1\n2\n5"), 8)
        self.assertEqual(string_calculator("1,2,5"), 8)

    def test_string_calculator_with_default_delimiter_at_first_line(self):
        """
        This test method is used to check,
             if input_string is “//[delimiter]\n[numbers…]”
                for example “//;\n1;2”
                should return three where the default delimiter is ‘;’
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("//;\n1;2"), 3)
        self.assertEqual(string_calculator("//;\n1;2,5"), 8)
        self.assertEqual(string_calculator("//;\n1;2\n5"), 8)
        self.assertEqual(string_calculator("//:\n1:2"), 3)


if __name__ == '__main__':
    unittest.main()
