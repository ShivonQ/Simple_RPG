from character.Character import *


class Merchant(Character):
    def __init__(self, name, money, inventory):
        super().__init__(name)
        # self.name = name
        # self.armor = armor
        # self.strength = strength
        self.money = money
        self.inventory = inventory


    def set_armor_max_hp(self, arm, max_hp):

        self.armor = arm
        self.max_hp = max_hp

    def set_inventory (self, inventory):

        self.inventory = inventory