import unittest

from src.repetitioncounter.count_repetitions import count_repetitions

class SingleWordRepetitionCounterTests(unittest.TestCase):

    def test_single_repeated_word_twice_returns_just_that_word(self):
        test_input = [
            'when', 'I', 'woke', 'up', 'this', 'morning', 'beautiful', 'morning',
            ]
        expected_output = {
            'morning': 2,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output,actual_output)

    def test_single_repeated_word_three_times_returns_just_that_word(self):
        #test_input = "Romeo, Romeo, wherefore are thou Romeo?".split(' ')
        test_input = [
            'Romeo', 'Romeo', 'wherefore', 'are', 'thou', 'Romeo'
            ]
        expected_output = {
            'Romeo': 3,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output,actual_output)

    def test_phrase_without_repetition_returns_no_repetition(self):
        test_input = [
            'Give', 'me', 'a', 'phrase', 'where', 'there', 'is', 'no', 'repetition'
            ]
        expected_output = { }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

if __name__ == "__main__":
    unittest.main()