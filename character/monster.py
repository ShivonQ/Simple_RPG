from character.Character import *


class Monster(Character):
    def __init__(self, name, max_hp, xp_val, money, armor, strength, level):
        super().__init__(name)
        self.max_hp = max_hp
        # self.name = name
        # self.armor = armor
        # self.strength = strength
        self.xp_val = xp_val
        self.money = money
        self.level = level
        self.set_str_and_armor(strength,armor)


    def set_str_and_armor(self, str, arm):
        self.strength = str
        self.armor = arm