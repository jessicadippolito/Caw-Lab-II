from cow import Cow

class Dragon(Cow):
    def __init__(self, name):
        super().__init__(name)

    def can_breath_fire(self):
        return True