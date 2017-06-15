class Play(object):

    def __init__(self, title):
        self.title = title
        self.acts = []

class Act(object):

    def __init__(self, number):
        self.number = number
        self.scenes = []

class Scene(object):

    def __init__(self, number):
        self.number = number
        self.lines_of_dialogue = []

class LineOfDialogue(object):
    def __init__(self, character_name):
        self.character_name = character_name
        self.lines = []

