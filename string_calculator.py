import re
from collections import Counter


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
    default_delimiter_first_line_flag = re.match(r"//([\W]+)\n", numbers)

    final_delimiters_pattern = r",|\n"  # Default delimiter pattern

    if default_delimiter_first_line_flag:
        # If default delimiter is present in first line of string, then take it
        default_delimiter_data = default_delimiter_first_line_flag.group(1)
        numbers = re.sub(r"^//[\W]+\n", "", numbers)    # Remove first line

        default_delimiter_data_with_count = Counter(default_delimiter_data)

        # Handle scenario where comma is present in first line of string as
        # default delimiter. In such case, take count of comma present in
        # first line as default delimiter for comma delimiter type
        if ',' in default_delimiter_data_with_count:
            final_delimiters_pattern = r"\n"

        # Build the delimiter pattern
        for cur_delimiter, count in default_delimiter_data_with_count.items():
            if cur_delimiter in ('*', '+', '.'):
                # Handled characters which are special in Python Regex
                final_delimiters_pattern += (rf"|\{cur_delimiter}"
                                             + '{' + str(count) + '}')
            else:
                final_delimiters_pattern += (r'|' + cur_delimiter
                                         + '{' + str(count) + '}')

    # Split string based on the derived delimiter pattern which contains
    # different delimiters such as comma, newline or default delimiters
    # given in the first line or combination of these delimiters
    string_numbers = re.split(final_delimiters_pattern, numbers)

    # Check for Negative numbers in input_string
    # If present, then raise error message with negative numbers
    negative_numbers = [string_number for string_number in string_numbers
                        if int(string_number) < 0]

    if negative_numbers:
        error_msg = "Error: Negative numbers are not allowed {0}".format(
            ','.join(negative_numbers))
        raise ValueError(error_msg)

    # Check for numbers > 1000
    # If present, then ignore such numbers which are greater than 1000
    sum_numbers = sum(int(string_number) for string_number in string_numbers
                      if int(string_number) <= 1000)
    return sum_numbers