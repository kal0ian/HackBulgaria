from hero import Hero
from orc import Orc


class Dungeon:

    def __init__(self, mappath):
        self.mappath = mappath

    def print_map(self):
        file = open(self.mappath, "r")
        print (file.read())
        file.close()

    def spawn(self, player_name, entity):

        file = open(self.mappath, "r+")
        dungeon_map = file.read()
        if type(entity) is Hero:
            if 'S' in dungeon_map:
                dungeon_map.replace('S', 'H', 1)
                file.write(dungeon_map)
                file.close()
                return True
        if entity is Orc:
            if 'S' in dungeon_map:
                dungeon_map.replace('S', 'O', 1)
                file.write(dungeon_map)
                file.close()
                return True
        file.close()
        return False
