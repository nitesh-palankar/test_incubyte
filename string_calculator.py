import re

def string_calculator(numbers):
    """
    This function is used to parse the input_string based on the given
    Delimiters and criteria. And it will return the sum of numbers present in
    the given string(separated by delimiters).

    :param numbers: str, Input String which contains Numbers with Delimiters
    :return: int, Sum of Numbers present in the given input string
    """

    numbers = numbers.strip()   # Removed leading/trailing whitespaces if any

    # Check if string is empty, simply return 0
    if len(numbers) == 0:
        return 0

    # Check for comma and newline separated numbers
    string_numbers = re.split(r",|\n", numbers)
    sum_numbers = sum(int(string_number) for string_number in string_numbers)
    return sum_numbers