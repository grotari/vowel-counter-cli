def count_vowels(
    input_string: str,
    vowels: str = "aeiou",
    case_sensitive: bool = False,
    chunk_size: int = 1000,
) -> int:
    """
    Count the vowels in a given string using a chunking approach.

    :param input_string: The string to analyze
    :param vowels: A string representing the vowels to count (default: "aeiou")
    :param case_sensitive: Whether to count vowels case-sensitively (default: False)
    :param chunk_size: The size of chunks to process at a time (default: 1000)
    :return: The count of vowels in the string
    :raises TypeError: If input_string is not a string
    :raises ValueError: If vowels is not a valid string or if chunk size is not a positive integer
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    if not vowels or not isinstance(vowels, str):
        raise ValueError("Vowels must be a non-empty string")

    if not isinstance(chunk_size, int) or chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer.")

    vowels_set = set(vowels)

    if not case_sensitive:
        input_string = input_string.lower()
        vowels_set = set(vowel.lower() for vowel in vowels_set)

    total_vowels = 0

    for i in range(0, len(input_string), chunk_size):
        chunk = input_string[i : i + chunk_size]
        total_vowels += sum(1 for char in chunk if char in vowels_set)

    return total_vowels
