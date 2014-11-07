import unittest
from dungeon import Dungeon
from hero import Hero


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.dungeonMap = Dungeon("basic_dungeon.txt")

    def test_init(self):
        self.assertEqual(self.dungeonMap.mappath, "basic_dungeon.txt")

    def test_print_map(self):

        pass
    def test_spawn(self):
        bron_hero = Hero("Bron", 100, "DragonSyler")
        print (self.dungeonMap.spawn("pesho", bron_hero))

if __name__ == '__main__':
    unittest.main()
