from random import randint


class Character:
    def __init__(self, name):
        self.name = name
        self.strength = 1 # This is the base damage
        self.armor = 0 # This is the base armor rating
    # #     Damage vs Armor, if damage <= armor 'You Missed'
    #     self.money = 0
        self.current_hp = 1
        self.max_hp = 1

    def attack_enemy(self, enemy):
        damage_amount = randint(1, self.strength)
        if damage_amount <= enemy.armor:
            #     '|   1) Attack   2) Drink Potion   3) Check Hero Status    4) Flee the Battle   |'
            print('|                            {}\'s attack misses!                          |'.format(self.name))
        else:
            damage_amount = damage_amount-enemy.armor
            #     '|   1) Attack   2) Drink Potion   3) Check Hero Status    4) Flee the Battle   |'
            print('|                     {} hits for {} damage!                  |'.format(self.name, damage_amount))
            enemy.take_damage(damage_amount)

    def take_damage(self, damage_dealt):
        # This takes into account any armor that caused a miss
        self.current_hp -= damage_dealt

    def am_I_dead(self):
        if self.current_hp <= 0:
            print('{} has died from their wounds.'.format(self.name))

