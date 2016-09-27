from character import Character
from character import data


class Hero(Character):
    def __init__(self, name, hp, max_hp, armor, strength, xp, level, money, next_level):
        super.__init__(name)
        # in the future a additional Class class will grant further inheritence
        # Which will make many of these happen there, not here.
        self.state = 'normal'
        self.hp = 10
        self.max_hp = 10
        self.armor = 1  # Used to figure out if you missed
        self.strength = 3  # Used for the max on damage
        self.xp = 0
        self.level = 1
        self.money = 5
        self.next_level = 100

    # TODO: Add a kill Counter for additional Highscore info

    def set_starter_stats(self):
        self.armor = 1
        self.strength = 3

    def set_opened_save_stats(self,hp,max_hp,armor,strength,xp,level,money,next_level):
        self.hp = hp
        self.max_hp=max_hp
        self.armor = armor
        self.strength = strength
        self.xp = xp
        self.level = level
        self.money = money
        self.next_level = next_level

    def gain_xp(self, xp):
        self.xp += xp
        if xp >= self.next_level:
            # If the Heros XP is more than the next level
            # Level him up
            self.gain_level()
        else:
            pass
        print('{} gained {} xp!'.format(self.name, xp))

    def gain_level(self):
        # Sort through the Dictionary of Levels,
        levels = data.get_levels()
        next_level_xp = levels[self.level+1]
        # check for if the next hero level has been reached.
        if next_level_xp <= self.xp:
            #
            self.level += 1
            print('{} Gained a Level! {} is now level {}!\n')
            self.next_level = next_level_xp
    #TODO:   THIS WILL ALSO INCREASE VARIOUS ABILITIES FOR THE HERO
    # At a certain Rate
    """What about +2 max_hp, +1 Damage (Base), +1 Armor (every other level {if level%2 == 0})"""

    def status(self):
        print('_________HERO_STATUS__________\n'
              ' HP {}/{}   Level {}   XP {}/{}\n'
              '______________________________'
              .format(self.hp, self.max_hp, self.level,
                      self.xp, self.next_level))
