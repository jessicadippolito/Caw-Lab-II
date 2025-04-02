from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        Cow.__init__(self,name)
        self. image = None

    def can_breath_fire(self):
        return True