import unittest
from entity import Entity
from weapon import Weapon

class TestEntity(unittest.TestCase):

    def setUp(self):
        self.pesho = Entity("Pesho", 100)

    def test_orc_init(self):
        self.assertEqual(self.pesho.name, "Pesho")
        self.assertEqual(self.pesho.health, 100)


    def test_get_health(self):
        self.assertEqual(100, self.pesho.get_health())

    def test_is_alive(self):
        self.assertTrue(self.pesho.is_alive())

    def test_is_alive_dead(self):
        self.pesho.health = 0
        self.assertFalse(self.pesho.is_alive())

    def test_take_demage(self):
        self.pesho.take_demage(10)
        self.assertEqual(90, self.pesho.health)

    def test_take_demage_two(self):
        self.pesho.take_demage(110)
        self.assertEqual(0, self.pesho.health)

    def test_take_healing(self):
        self.pesho.take_demage(100)
        self.assertFalse(self.pesho.take_healing(10))

    def test_take_healing_two(self):
        self.pesho.take_demage(10)
        self.pesho.take_healing(200)
        self.assertEqual(100, self.pesho.health)

    def test_take_healing_three(self):
        self.pesho.take_demage(10)
        self.pesho.take_healing(200)
        self.assertTrue(self.pesho.is_alive())
    def test_has_weapon(self):
        self.pesho.weapon =True
        self.assertTrue(self.pesho.has_weapon())
    def test_equip_weapon(self):
        axe = Weapon("axe",20,0.3)
        self.pesho.weapon=axe
        self.assertTrue(self.pesho.has_weapon())
    def test_attack(self):
        axe = Weapon("axe",20,0.1)
        self.pesho.weapon=axe
        self.assertEqual(20,self.pesho.attack())
if __name__ == '__main__':
    unittest.main()
