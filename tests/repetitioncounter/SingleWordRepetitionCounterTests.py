import unittest

class SingleWordRepetitionCounterTests(unittest.TestCase):

    def test_single_repeated_word_twice_returns_just_that_word(self):
        test_input = "When I woke up this morning, it was a beautiful morning"
        expected_output = {
            'morning': 2,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output,actual_output)

    def test_single_repeated_word_three_times_returns_just_that_word(self):
        test_input = "Romeo, Romeo, wherefore are thou Romeo?"
        expected_output = {
            'Romeo': 3,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output,actual_output)

    def test_phrase_without_repetition_returns_no_repetition:
        test_input = "Give me a phrase where there's no repetition"
        expected_output = { }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)
