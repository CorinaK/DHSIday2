import re

from src.parser.SceneParser import SceneParser
from src.parts.parts import Act

class ActParser(object):

    ACT_HEADING_PATTERN = re.compile(
        r'^ACT\s*(?P<act_number>[IV]+)\.'
    )
    ACT_AND_SCENE_HEADING_PATTERN = re.compile(
        r'^ACT\s*(?P<act_number>[IV]+)\. SCENE (?P<scene_number>[1-9IXV]+)\.'
    )

    def __init__(self, parent, line_of_text):
        self.parent = parent
        parsing_results = self.ACT_HEADING_PATTERN.match(line_of_text).groupdict()
        self.act = Act(parsing_results['act_number'])

    def parse(self,text):
        if (
                    self.ACT_AND_SCENE_HEADING_PATTERN.match(text)
        ):
            act_and_scene = self.ACT_AND_SCENE_HEADING_PATTERN.match(text).groupdict()
            if act_and_scene['act_number'] == self.act.number:
                scene_parser = SceneParser(
                    self, 'SCENE ' + act_and_scene['scene_number'] + '.'
                )
                return scene_parser
            else:
                return self.parent.parse(text)
        elif SceneParser.SCENE_HEADING_PATTERN.match(text):
            scene_parser = SceneParser(
                self, text
            )
            return scene_parser
        else:
            return self.parent.parse(text)