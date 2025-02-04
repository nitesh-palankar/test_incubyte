def string_calculator(numbers):
    """
    This function is used to parse the input_string based on the given
    Delimiters and criteria. And it will return the sum of numbers present in
    the given string(separated by delimiters).

    :param numbers: str, Input String which contains Numbers with Delimiters
    :return: int, Sum of Numbers present in the given input string
    """

    if len(numbers.strip()) == 0:
        return 0

    return