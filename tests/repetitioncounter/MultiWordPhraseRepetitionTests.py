import unittest

#add edge cases, i.e. try to think of a phrase that might blow stuff up
from src.repetitioncounter.count_repetitions import count_repetitions, tokenize

class MultiWordPhraseRepetitionTests(unittest.TestCase):

    def test_repetition_is_discovered_when_first_instance_is_later_in_sentence(self):
        test_input = tokenize("He looked at the beautiful morning and said \"What a beautiful morning!\"")
        expected_output = {
            'beautiful morning': 2,
            'beautiful': 2,
            'morning': 2,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_that_a_repeated_phrase_is_discovered_when_seperated_by_more_than_one_word(self):
        test_input = tokenize("To be or not to be, that is the question")
        expected_output = {
            'to be': 2,
            'to': 2,
            'be': 2,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_that_a_phrase_that_is_repeated_immediately_is_reported(self):
        test_input = tokenize("O yes, o yes, what a beautiful morning")
        expected_output = {
            'o yes': 2,
            'o': 2,
            'yes': 2,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_that_a_complete_phrase_that_is_nothing_but_repetition_is_reported(self):
        test_input = tokenize("O yes, o yes")
        expected_output = {
            'o yes': 2,
            'o': 2,
            'yes': 2,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_that_words_that_repeat_and_are_part_of_longer_phrases_are_reported(self):
        test_input = tokenize("To-morrow yes to-morrow yes I love you to-morrow")
        expected_output = {
            'to-morrow yes': 2,
            'to-morrow': 3,
            'yes': 2,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_that_words_with_hypens_are_not_equivalent_to_words_without_hyphens(self):
        test_input = tokenize("To-morrow yes tomorrow yes to-morrow creeps past the break of day")
        expected_output = {
            'to-morrow': 2,
            'yes': 2,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

if __name__ == "__main__":
    unittest.main()