import unittest
from unittest import TestCase

from src.parser.ActParser import ActParser
from src.parser.PlayParser import PlayParser
from src.parser.SceneParser import SceneParser

class ActParserTests(unittest.TestCase):

    def test_create_act_parser_recognizes_parent_and_number(self):
        play_parser = PlayParser(None, 'REVENGE OF THE DHSI BUNNIES')
        act_parser = ActParser(play_parser, 'ACT I. SCENE 1.')
        self.assertEqual(act_parser.parent, play_parser)
        self.assertEqual(act_parser.act.number, 'I')

    def test_act_parser_recgonizes_act_and_scene_heading(self):
        play_parser = PlayParser(None, 'REVENGE OF THE DHSI BUNNIES')
        act_parser = ActParser(play_parser, 'ACT I. SCENE 1.')
        next_parser = act_parser.parse('ACT I. SCENE 1.')
        self.assertIsInstance(next_parser, SceneParser)

    def test_create_act_parser_recognizes_new_scene(self):
        act_parser = ActParser(None, 'ACT I.')
        scene_heading = 'SCENE 1.'
        next_parser = act_parser.parse(scene_heading)
        self.assertIsInstance(next_parser,SceneParser)

    def test_create_act_parser_recognizes_end_of_act(self):
        play_parser = PlayParser(None, 'REVENGE OF THE DHSI BUNNIES')
        act_parser = ActParser(play_parser, 'ACT I.SCENE 2.')
        next_parser = act_parser.parse('ACT II. SCENE 1.')
        self.assertIsInstance(next_parser, PlayParser)
        self.assertEqual(next_parser, play_parser)