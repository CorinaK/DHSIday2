import unittest

from src.parser.ActParser import ActParser
from src.parser.PlayParser import PlayParser, RootParser


class PlayParserTest(unittest.TestCase):

    def test_create_play_parser(self):
        play_title = "ALLS WELL THAT ENDS WELL"
        play_parser = PlayParser(None, play_title)
        self.assertEqual(
            play_parser.play.title,
            play_title
        )

    def test_ignore_non_act_lines(self):
        play_parser = PlayParser(None, 'REVENGE OF THE DHSI BUNNIES')
        next_parser = play_parser.parse('Rousillon; Paris; Florence; Marseilles')
        self.assertEqual(next_parser, play_parser)

    def test_create_act_parser(self):
        play_parser = PlayParser(None, 'REVENGE OF THE DHSI BUNNIES')
        line_of_text = 'ACT I. SCENE 1.'
        next_parser = play_parser.parse(line_of_text)
        self.assertIsInstance(next_parser, ActParser)

    def test_discover_new_play(self):
        root_parser = RootParser()
        play_parser = PlayParser(root_parser, 'REVENGE OF THE DHSI BUNNIES')
        line_of_text = 'THE TEMPEST'
        next_parser = play_parser.parse(line_of_text)
        self.assertEqual(next_parser, root_parser)