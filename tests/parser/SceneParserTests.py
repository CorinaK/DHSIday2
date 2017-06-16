import unittest

from src.parser.ActParser import ActParser
from src.parser.LineOfDialogueParser import LineOfDialogueParser
from src.parser.SceneParser import SceneParser

class SceneParserTests(unittest.TestCase):

    def test_recognizes_line_of_dialogue(self):
        scene_parser = SceneParser(None,'SCENE I.')
        text = '  FIRST LORD. Our remedies oft in ourselves do lie,'
        new_parser = scene_parser.parse(text)
        if isinstance(new_parser, LineOfDialogueParser):
            self.assertTrue(True)
        else:
            self.fail()

    def test_parser_skips_lines_that_are_not_dialogue(self):
        scene_parser = SceneParser(None, 'SCENE IV.')
        stage_direction = "Enter BERTRAM, the COUNTESS OF ROUSILLON, HELENA, and LAFEU, all in black"
        new_parser = scene_parser.parse(stage_direction)
        self.assertEqual(new_parser, scene_parser)

    def test_parser_skips_blank_line(self):
        scene_parser = SceneParser(None, 'SCENE 78.')
        blank_line = ''
        new_parser = scene_parser.parse(blank_line)
        self.assertEqual(new_parser, scene_parser)

    def test_parser_skips_exit_line(self):
        scene_parser = SceneParser(None, 'SCENE XX.')
        exit_line= " Exit"
        new_parser = scene_parser.parse(exit_line)
        self.assertEqual(new_parser, scene_parser)

    def test_recognizes_start_of_scene_with_arabic_numeral(self):
        start_of_scene = "SCENE 4."
        scene_parser = SceneParser(None, start_of_scene)
        self.assertEqual(scene_parser.scene.number,'4')

    def test_recognize_start_of_scene_with_roman_numeral(self):
        start_of_scene = "SCENE IV."
        scene_parser = SceneParser(None, start_of_scene)
        self.assertEqual(scene_parser.scene.number, 'IV')

    def test_recognizes_end_of_scene(self):
        start_of_scene = 'SCENE IV.'
        act_parser = ActParser(None, 'ACT I.')
        scene_parser = SceneParser(act_parser, start_of_scene)
        start_of_a_new_scene = 'SCENE V.'
        next_parser = scene_parser.parse(start_of_a_new_scene)
        # isinstance asks: is the next parser an ActParser?
        if isinstance(next_parser, ActParser):
            self.assertTrue(True)
        else:
            self.fail()