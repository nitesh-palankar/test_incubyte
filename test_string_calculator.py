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

    def test_string_calculator_with_negative_numbers(self):
        """
        This test method is used to check,
             if input_string contains negative numbers:
                then string_calculator() function should throw an error saying
                that "negative numbers not allowed <negative_number>"
             else:
                it will throw an Assertion Error
        """
        with self.assertRaisesRegex(ValueError,
            "Error: Negative numbers are not allowed -1"):
            string_calculator("-1,2")

        with self.assertRaisesRegex(ValueError,
            "Error: Negative numbers are not allowed -1,-5"):
            string_calculator("-1,2,-5")

        with self.assertRaisesRegex(ValueError,
            "Error: Negative numbers are not allowed -2"):
            string_calculator("1\n-2")

        with self.assertRaisesRegex(ValueError,
            "Error: Negative numbers are not allowed -2,-5"):
            string_calculator("//;\n1;-2,-5")

        with self.assertRaisesRegex(ValueError,
            "Error: Negative numbers are not allowed -1,-5,-6"):
            string_calculator("//;\n-1;2,-5\n-6")

    def test_string_calculator_with_numbers_greater_than_thousand(self):
        """
        This test method is used to check,
             if input_string contains number > 1000:
                then string_calculator() function should ignore such >1000
                     numbers and add rest of the numbers as final output
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("2,1001"), 2)
        self.assertEqual(string_calculator("2,1001,1000"), 1002)
        self.assertEqual(string_calculator("2,1001,1000\n5"), 1007)
        self.assertEqual(string_calculator("//;\n1;2\n5;1001"), 8)
        self.assertEqual(string_calculator("1001"), 0)

    def test_string_calculator_with_default_delimiter_multiple_length(self):
        """
        This test method is used to check,
             if input_string is “//[delimiter]\n[numbers…]” and delimiter can
                be of any length
                for example “//***\n1***2”
                should return three where the default delimiter is ‘***’
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("//***\n1***2"), 3)
        self.assertEqual(string_calculator("//;;;;\n1;;;;2,5"), 8)
        self.assertEqual(string_calculator("//,,\n1\n2,,5"), 8)
        self.assertEqual(string_calculator("//:::\n1:::2,4"), 7)

    def test_string_calculator_multiple_default_delimiter_single_length(self):
        """
        This test method is used to check,
             if input_string is “//[delimiter][delimiter]\n[numbers…]”
                for example “//[*][%]\n1*2%3”
                should return six
                where the default delimiters are ‘*’ and '%'(single-length)
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("//;%\n1;2%3"), 6)
        self.assertEqual(string_calculator("//,;\n1;2,5"), 8)
        self.assertEqual(string_calculator("//;*,\n1;2\n5*2"), 10)

    def test_string_calculator_multiple_default_delimiter_multi_length(self):
        """
        This test method is used to check,
             if input_string is “//[delimiter][delimiter]\n[numbers…]”
                for example “//[***][%%]\n1***2%%3”
                should return six
                where the default delimiters are ‘***’ and '%%' (multi-length)
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("//;;%%\n1;;2%%3"), 6)
        self.assertEqual(string_calculator("//,,;;;\n1;;;2,,5"), 8)

    def test_string_calculator_multiple_default_delimiter_single_multi_length(
            self):
        """
        This test method is used to check,
             if input_string is “//[delimiter][delimiter]\n[numbers…]”
                for example “//[***][%]\n1***2%3”
                should return six
                where the default delimiters are ‘***’ and '%'
                     (both single and multiple length)
             else:
                it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("//;***%%,\n1;2\n6%%5***2,4"), 20)


if __name__ == '__main__':
    unittest.main()
