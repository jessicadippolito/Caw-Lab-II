from cow import Cow
from dragon import Dragon

class IceDragon(Dragon):
    def __init__(self, name, image):
        Cow.__init__(self, name)
        self.image = image

    def can_breathe_fire(self):
        return False