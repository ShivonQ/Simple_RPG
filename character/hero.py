import Character
import data
class Hero(Character):
    def __init__(self):
        Character.__init__(self)
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

    def gain_xp(self, xp):
        self.xp += xp
        print('{} gained {} xp!'.format(self.name, xp))

    def gain_level(self):
        # Sort through the Dictionary of Levels,
        levels = data.get_levels()
        next_level_xp = levels[self.level+1]
        # check for if the next hero level has been reached.
        if next_level_xp <= self.xp:
            self.level += 1
            print('{} Gained a Level! {} is now level {}!\n')
            self.next_level = next_level_xp
    #TODO:   THIS WILL ALSO INCREASE VARIOUS ABILITIES FOR THE HERO

    def status(self):
        print('_________HERO_STATUS__________\n'
              ' HP {}/{}   Level {}   XP {}/{}\n'
              '______________________________'
              .format(self.hp, self.max_hp, self.level,
                      self.xp, self.next_level))
