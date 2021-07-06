from object import Object


class Monster(Object):

    def __init__(self, name):
        super().__init__(name)
        self.alive = True

