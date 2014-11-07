from hero import Hero
import unittest


class TestHero(unittest.TestCase):

    def test_hero_init(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        self.assertEqual(bron_hero.name, "Bron")
        self.assertEqual(bron_hero.health, 100)
        self.assertEqual(bron_hero.nickname, bron_hero.nickname)

    def test_known_as(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        self.assertEqual(bron_hero.known_as(), "Bron the DragonSyler")

    def test_get_health(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        self.assertEqual(100, bron_hero.get_health())

    def test_is_alive(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        self.assertTrue(bron_hero.is_alive())

    def test_is_alive_dead(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        bron_hero.health = 0
        self.assertFalse(bron_hero.is_alive())

    def test_take_demage(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        bron_hero.take_demage(10)
        self.assertEqual(90, bron_hero.health)

    def test_take_demage_two(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        bron_hero.take_demage(110)
        self.assertEqual(0, bron_hero.health)

    def test_take_healing(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        bron_hero.take_demage(100)
        self.assertFalse(bron_hero.take_healing(10))

    def test_take_healing_two(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        bron_hero.take_demage(10)
        bron_hero.take_healing(200)
        self.assertEqual(100, bron_hero.health)

    def test_take_healing_three(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        bron_hero.take_demage(10)
        bron_hero.take_healing(200)
        self.assertTrue(bron_hero.is_alive())


if __name__ == '__main__':
    unittest.main()
