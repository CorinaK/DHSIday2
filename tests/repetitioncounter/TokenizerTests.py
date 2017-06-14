import unittest

from src.repetitioncounter.count_repetitions import tokenize


class TokenizerTests(unittest.TestCase):
    def test_tokenizer_slits_on_spaces_and_lowercases_string(self):
        test_input = "The quick  brown fox"
        expected_output = ['the', 'quick', 'brown', 'fox']
        actual_output = tokenize(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_tokeizer_disregards_unimportant_punctation(self):
        test_input = "Romeo, Romeo, wherefore art thou Romeo?"
        expected_output = ['romeo', 'romeo', 'wherefore', 'art', 'thou', 'romeo']
        actual_output = tokenize(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_tokenizer_keeps_dashes_within_words_and_apostrophes(self):
        test_input = "Let's meet face-to-face"
        expected_output = ["let's",'meet', 'face-to-face']
        actual_output = tokenize(test_input)
        self.assertEqual(expected_output, actual_output)
