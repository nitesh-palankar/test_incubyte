from string_calculator import string_calculator
import unittest


class TestStringCalculator(unittest.TestCase):
    def test_string_calculator_without_return(self):
        """
        This method is used to show that if string_calculator method does not
        return anything(i.e. None) then it will throw an Assertion Error
        """
        self.assertEqual(string_calculator("1,2"), 3)


if __name__ == '__main__':
    unittest.main()
