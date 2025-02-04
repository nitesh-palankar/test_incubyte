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

    # Check for given default delimiter in first line of string
    default_delimiter = None
    default_delimiter_first_line_flag = re.match(r"//(.)\n", numbers)

    if default_delimiter_first_line_flag:
        # If default delimiter is present in first line of string, then take it
        default_delimiter = default_delimiter_first_line_flag.group(1)
        numbers = re.sub(r"^//.\n", "", numbers)    # Remove first line

    # Split string based on different delimiters
    # such as comma, newline or default delimiter given in first line
    # or combination of these delimiters
    string_numbers = re.split(rf",|\n|{default_delimiter}", numbers)

    # Check for Negative numbers in input_string
    # If present, then raise error message with negative numbers
    negative_numbers = [string_number for string_number in string_numbers
                        if int(string_number) < 0]

    if negative_numbers:
        error_msg = "Error: Negative numbers are not allowed {0}".format(
            ','.join(negative_numbers))
        raise ValueError(error_msg)

    sum_numbers = sum(int(string_number) for string_number in string_numbers)
    return sum_numbers