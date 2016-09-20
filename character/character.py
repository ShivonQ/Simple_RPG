from random import randint

class Character:
    def __init__(self):
        self.name = ''
        self.hp = 1
        self.max_hp = 1
        self.strength = 1 #This is the base damage
        self.armor = 0 #This is the base armor rating

    def attack_enemy(self, enemy):
        damage_amount = min(max(randint(0)))