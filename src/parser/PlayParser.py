from src.parser.ActParser import ActParser
from src.parts.parts import Play
import re

class PlayParser(object):

    TITLE_PATTERN = re.compile(r'^[A-Z ]+$')

    def __init__(self, parent, line_of_text):
        self.parent = parent
        self.play = Play(line_of_text)
        pass

    def parse(self,text):
        if ActParser.ACT_AND_SCENE_HEADING_PATTERN.match(text):
            act_parser = ActParser(self,text)
            self.play.acts.append(act_parser.act)
            return act_parser
        elif self.TITLE_PATTERN.match(text):
            return self.parent.parse(text)
        else:
            return self

class RootParser(object):

    def __init__(self):
        self.plays = []

    def parse(self,text):
        if PlayParser.TITLE_PATTERN.match(text):
            play_parser = PlayParser(self, text)
            self.plays.append(play_parser.play)
            return play_parser
        else:
            return self