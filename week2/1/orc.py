from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor
        if self.berserk_factor > 2:
            self.berserk_factor = 2
        elif self.berserk_factor < 1:
            self.berserk_factor = 1
