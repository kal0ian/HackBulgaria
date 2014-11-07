from fight import Fight
from orc import Orc
from hero import Hero
from weapon import Weapon
import random
import unittest


class FightTest(unittest.TestCase):

    def setUp(self):
        self.orc = Orc("PeshoOrc", 100, 1.2)
        self.hero = Hero("PeshoHero", 100, "peshooo")
        self.weapon1 = Weapon("axe", 50, 0.5)
        self.weapon2 = Weapon("axe2", 70, 0.3)
        self.fighting = Fight(self.hero, self.orc)
        self.orc.weapon = self.weapon1

    def test_init(self):
        self.assertEqual(self.fighting.Orc,self.orc)
        self.assertEqual(self.fighting.Hero,self.hero)

    def test_coin(self):
        arr = []
        flag = [False, False]
        for i in range(1, 100):
            arr.append(self.fighting.coin())

        for i in arr:
            if i:
                flag[0] = True
            else:
                flag[1] = True
        self.assertEqual(flag, [True, True])

    def test_simulate_fight(self):
        self.assertEqual("PeshoOrc", self.fighting.simulate_fight())

if __name__ == '__main__':
    unittest.main()
