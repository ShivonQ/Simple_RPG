from character.Character import *


class Monster(Character):
    def __init__(self, name, xp_val, money, level):
        super().__init__(name)
        # self.name = name
        # self.armor = armor
        # self.strength = strength
        self.xp_val = xp_val
        self.money = money
        self.level = level


    def set_str_and_armor(self, str, arm,max_hp):
        self.strength = str
        self.armor = arm
        self.max_hp = max_hp