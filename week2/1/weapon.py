import random

class Weapon:

    def __init__(self, type, demage, critical_strike_percent):
        self.__set_critical_strike_percent(critical_strike_percent)
        self.type = type
        self.demage = demage
    def __set_critical_strike_percent(self, critical_strike_percent):
        if critical_strike_percent > 0 and critical_strike_percent < 1:
            self.critical_strike_percent = critical_strike_percent
        else:
        	raise ValueError
    def critical_hit(self):
    	return random.random() < self.critical_strike_percent