import Character

class Monster(Character):
    def __init__(self, name, max_hp, xp_val, money, armor, strength):
        super.__init__(name)
        self.max_hp = max_hp
        self.name = name
        self.armor = armor
        self.strength = strength
        self.xp_val = xp_val
        self.money = money