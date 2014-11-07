from weapon import Weapon
class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def take_demage(self, demage_points):
        self.health -= demage_points
        if self.health < 0:
            self.health = 0
        return self.health

    def take_healing(self, healing_points):
        if self.is_alive() == False:
            return False

        if self.health + healing_points > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing_points
        return True

    def has_weapon(self):
        return self.weapon

    def equip_weapon(self, weapon):
        self.weapon = weapon
    def attack(self):
        if self.has_weapon():
            if self.weapon.critical_hit():
                return self.weapon.demage*2
            else:
                return self.weapon.demage
        else: 
            return 0