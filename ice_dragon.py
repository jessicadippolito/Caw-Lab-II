from dragon import Dragon

class IceDragon(Dragon):
    def __init__(self, name):
        Cow.__init__(self, name)
        self.image = None

    def can_breathe_fire(self):
        return False