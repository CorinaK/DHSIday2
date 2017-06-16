from src.parts.parts import LineOfDialogue
import re
class LineOfDialogueParser(object):

    NEW_LINE_PATTERN = re.compile(r'^\s\s(?P<character_name>[A-Z ]+)\.\s(?P<dialogue>.*)$')

    def __init__(self, parent, line_of_text):
        self.parent = parent
        # Match is a function of re, checks if the regex matches a string. It also has the function none, see below.
        parsing_results = self.NEW_LINE_PATTERN.match(line_of_text).groupdict()
        self.dialogue = LineOfDialogue(
            parsing_results['character_name']
        )
        self.dialogue.lines.append(
            parsing_results['dialogue']
        )

    def parse(self,line):
        new_line_of_dialogue_results = self.NEW_LINE_PATTERN.match(
            line
        )
        if new_line_of_dialogue_results is None:
            cleaned_text = line.strip()
            self.dialogue.lines.append(cleaned_text)
            return self
        else:
            return self.parent.parse(line)