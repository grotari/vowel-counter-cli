import unittest
from my_project.vowel_counter import count_vowels


class TestVowelCounter(unittest.TestCase):
    # Tests for the count_vowels function

    # Basic Functionality Tests
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_with_whitespace(self):
        self.assertEqual(count_vowels("H e l l o  W o r l d"), 3)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_only_vowels(self):
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_mixed_characters(self):
        self.assertEqual(count_vowels("Hello World!"), 3)

    def test_numbers_and_special_chars(self):
        self.assertEqual(count_vowels("123!@#"), 0)

    # Case-Sensitive Tests
    def test_case_sensitive(self):
        self.assertEqual(count_vowels("hEllo World", case_sensitive=True), 2)

    def test_case_sensitive_no_match(self):
        self.assertEqual(count_vowels("HELLO", case_sensitive=True), 0)

    # Tests for Invalid Input
    def test_integer_input_error(self):
        with self.assertRaises(TypeError):
            count_vowels(12345)

    def test_float_input_error(self):
        with self.assertRaises(TypeError):
            count_vowels(3.14159)

    def test_empty_vowels(self):
        with self.assertRaises(ValueError):
            count_vowels("Hello World", vowels="")

    def test_chunk_size_invalid(self):
        # Test with an invalid chunk_size (should raise ValueError)
        test_string = "Hello World!"
        with self.assertRaises(ValueError):
            count_vowels(test_string, chunk_size=0)  # Invalid chunk_size (0)

        with self.assertRaises(ValueError):
            count_vowels(test_string, chunk_size=-1)  # Invalid chunk_size (-1)
