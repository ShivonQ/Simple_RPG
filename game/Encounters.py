'''THIS PORTION MUST BE COMPLETED IN ORDER FOR THE GAME TO WORK AT ALL'''

# This is where the actual encounter types will go
# Someone needs to use the methods attatched to the base class in order to have fights occur
from database.db import *
from character.Monster import *
from character.Hero import *
import random.randint


def did_random_rest_encounter_occur(hero):
    chance = randint(1, 100)
    chance_range = (1,13,37,57,68)
    if chance in chance_range:
        print('A wild Monster attacked while you rest!')
#         TODO: Call monster encounter method
    else:
        print('You sleep peacefully.')


def random_monster_encounter(hero):
    print('Placeholder Print from random_monster_encounter method')
    # figure out the levels the monsters can be, not too low or too high
    random_level = randint(hero.level - 1, hero.level + 2)
    # grab a monster, send it back for fighting
    monster = fetch_monster_make_object(random_level)
    return monster

# def set_up_battle

def battle_time(hero,monster):






