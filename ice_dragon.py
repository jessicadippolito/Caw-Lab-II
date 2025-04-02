from dragon import Dragon

class IceDragon(Dragon):
    def __init__(self, name):
        super().__init__(name)
        self.image = None

    def can_breathe_fire(self):
        return False