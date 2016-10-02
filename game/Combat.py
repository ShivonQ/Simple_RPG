'''This combat Object handles the operatinos of a combat scene.
    It will be passed the Hero and The Monster and the battle will play out here.
    That way at every stage of combat each method only needs to reference itself.
    Making the Monster and The Hero 'Transient Global Variables'''

from character.Monster import Monster
from character.Hero import Hero
from random import shuffle
from random import randint
from game.displays import *

class Combat:
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster


    def battle_time(self):
        list_of_participants = [self.hero, self.monster]
        shuffle(list_of_participants)
        while self.hero.current_hp >= 1 or self.monster.current_hp >= 1:
            round_counter = 0
            # for each person in combat, let them take their turn
            for participant in list_of_participants:
                # This variable is for implementatino of potions (since they last a limited time)
                round_counter += 1
                self.take_a_turn(participant)
        #         if you are dead... exit combat after calling a HighScoreSave() method
        if self.hero.current_hp <= 0:
            print('{} has died. The {} picks over the corpse.'.format(self.hero.name,self.monster.name))
            '''This part here will be where the hall of fame stuff happens.  To be figured out later.
            My need to add 'state' to the DB in order to track who has died and who hasnt.'''
        #     If the monster is dead, get that cash and xp
        if self.monster.current_hp <= 0:
            self.hero.gain_xp(self.monster.xp_val)
            self.hero.money += self.monster.money
    #     one of them will go first, fortunatly they both have the same attack and damage methods


    def take_a_turn(self,participant):
        # is it the monsters turn or the players turn?
        # check if they are dead
        if participant.current_hp <= 0:
            pass
        else:
            if isinstance(participant, Hero):
                print('HERO TURN METHOD CALLED')
                self.hero_turn()
            elif isinstance(participant, Monster):
                print('MONSTER TURN METHOD')

    def hero_turn(self):
        while True:
            display_fight_menu()
            try:
                choice = int(input('{} is going to :').format(self.hero.name))
                if choice == 1:
                    print('Begin fight mode')
                    self.hero.attack_enemy(self.monster)
                    break
                if choice == 2:
                    print('Potion Drinking Menu')
                    # TODO: Fred's Potion Drinking
                    break
                if choice == 3:
                    print('RUN AWAYYY RUN AWAYYYY')

                    break
            except ValueError:
                print('{} is baffled by your choice, and looks beseechingly towards the sky for guidance.'.format(
                    self.hero.name))


    def monster_turn(self):
        self.monster.attack_enemy(self.hero)