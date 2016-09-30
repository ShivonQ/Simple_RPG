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
        for participant in list_of_participants:
            self.take_a_turn(participant)
    #     one of them will go first, fortunatly they both have the same attack and damage methods


    def take_a_turn(self,participant):
        if isinstance(participant, Hero):
            print('HERO TURN METHOD CALLED')
        elif isinstance(participant, Monster):
            print('MONSTER TURN METHOD')

    def hero_turn(self):

        while True:
            display_fight_menu()
            try:
                choice = int(input('{} is going to :').format(self.hero.name))
                break
            except ValueError:
                print('{} is baffled by your choice, and looks beseechingly towards the sky for guidance.'.format(
                    self.hero.name))
