import unittest
from orc import Orc


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.pesho = Orc("Pesho", 100, 2.2)

    def test_orc_init(self):
        self.assertEqual(self.pesho.name, "Pesho")
        self.assertEqual(self.pesho.health, 100)
        self.assertEqual(self.pesho.berserk_factor, 2)

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

if __name__ == '__main__':
    unittest.main()
