from hero import Hero
from orc import Orc
import random


class Fight:

    def __init__(self, Hero, Orc):
        self.Hero = Hero
        self.Orc = Orc

    def coin(self):
        coin = True
        if random.randint(0, 100) < 50:
            coin = True
        else:
            coin = False
        return coin

    def simulate_fight(self):
        if not self.Hero.has_weapon() and not self.Orc.has_weapon():
            return

        turnHero = False
        turnOrc = False

        if self.coin():
            turnHero = True
        else:
            turnOrc = True
        while (self.Orc.is_alive() and self.Hero.is_alive()):
            if turnHero == True:
                self.Orc.take_demage(self.Hero.attack())
                turnHero = False
                turnOrc = True
            else:
                self.Hero.take_demage(self.Orc.attack())
                turnHero = True
                turnOrc = False
        if self.Orc.is_alive():
            return self.Orc.name
        else:
            return self.Hero.name
