from character.Character import Character
from character import data


class Hero(Character):
    def __init__(self, name):
        super().__init__(name)
        # in the future a additional Class class will grant further inheritence
        # Which will make many of these happen there, not here.
        self.state = 'normal'
        self.armor = 1  # Used to figure out if you missed
        self.strength = 3  # Used for the max on damage
        self.xp = 0
        self.level = 1
        self.money = 5
        self.next_level = 100
        '''self.killcount = 0'''

    # TODO: Add a kill Counter for additional Highscore info

    def set_state(self, new_state):
        self.state = new_state



    def set_starter_stats(self):
        self.armor = 1
        self.strength = 3
        self.max_hp = 10

    def set_opened_save_stats(self,hp,max_hp,armor,strength,xp,level,money,next_level):
        self.hp = hp
        self.max_hp=max_hp
        self.armor = armor
        self.strength = strength
        self.xp = xp
        self.level = level
        self.money = money
        self.next_level = next_level
        '''self.killcount=killcount'''

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
        self.max_hp += 3
        self.strength += 1
        if self.level % 3 == 0:
            self.armor += 1
        self.level += 1
        print('{} Gained a Level! {} is now level {}!\n')
        self.next_level = next_level_xp
    """What about +3 max_hp, +1 Damage (Base), +1 Armor (every 3 levels {if level%3 == 0})"""

    def status(self):
        print('_________HERO_STATUS__________\n'
              ' HP {}/{}   Level {}   XP {}/{}\n'
              '______________________________'
              .format(self.hp, self.max_hp, self.level,
                      self.xp, self.next_level))

    def gain_hp_from_rest(self, full_rest):
        # full_rest is a boolean
        if full_rest:
            self.current_hp += self.level*2
            print('By getting a full nights sleep you gained {} hitpoints.'.format(self.level*2))
        else:
            self.current_hp += self.level
            print("By being interrupted by an attack you only gained {} hitpoints.".format(self.level))

