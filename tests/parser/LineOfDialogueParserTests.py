import unittest
from src.parser.SceneParser import SceneParser
from src.parser.LineOfDialogueParser import LineOfDialogueParser

# Je kopieert steeds alles naar een nieuwe test omdat de tests volledig onafhankelijk van elkaar moeten opereren.

class LineOfDialogueParserTests(unittest.TestCase):
    def test_create_new_line_of_dialogue_recognizes_parent_and_dialogue_components(self):
        scene_parser = SceneParser(None, 'SCENE 2.')
        text = '  FIRST LORD. Our remedies oft in ourselves do lie,'
        parser = LineOfDialogueParser(
            scene_parser, text
        )
        self.assertEqual(
            parser.parent, scene_parser
        )
        self.assertEqual(
            parser.dialogue.character_name, "FIRST LORD"
        )
        self.assertEqual(
            parser.dialogue.lines, [
                'Our remedies oft in ourselves do lie,'
            ]
        )

    def test_add_new_line_of_text_appends_to_existing_dialogue(self):
        scene_parser = SceneParser(None, 'SCENE 2.')
        text = '  HELENA. Our remedies oft in ourselves do lie,'
        parser = LineOfDialogueParser(
            scene_parser, text
        )
        parser.parse('    Which we ascribe to heaven. The fated sky')
        self.assertEqual(
            parser.dialogue.lines, [
                'Our remedies oft in ourselves do lie,',
                'Which we ascribe to heaven. The fated sky',
            ]
        )

    def test_add_additional_lines_appends_to_current_dialogue(self):
        scene_parser = SceneParser(None, 'SCENE 2.')
        text = '  HELENA. Our remedies oft in ourselves do lie,'
        parser = LineOfDialogueParser(
            scene_parser, text
        )
        parser.parse('    Which we ascribe to heaven. The fated sky')
        parser.parse('    Gives us free scope; only doth backward pull')
        self.assertEqual(
            parser.dialogue.lines, [
                'Our remedies oft in ourselves do lie,',
                'Which we ascribe to heaven. The fated sky',
                'Gives us free scope; only doth backward pull',
            ]
        )

    def test_that_handles_new_character_name(self):
        scene_parser = SceneParser(None, 'SCENE 2.')
        text = '  HELENA. Our remedies oft in ourselves do lie,'
        parser = LineOfDialogueParser(
            scene_parser, text
        )
        parser.parse('    Which we ascribe to heaven. The fated sky')
        parser.parse('    Gives us free scope; only doth backward pull')
        next_parser = parser.parse('  PAROLLES. I am so full of business I cannot answer thee acutely. I')
        self.assertEqual(
            parser.dialogue.lines, [
                'Our remedies oft in ourselves do lie,',
                'Which we ascribe to heaven. The fated sky',
                'Gives us free scope; only doth backward pull',
            ]
        )
        self.assertEqual(
            next_parser, scene_parser
        )

# Still need to handle: 'Exit' within dialogue
# Still need to handle: Stage directions in dialogue