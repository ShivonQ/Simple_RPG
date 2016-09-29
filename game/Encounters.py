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
    monster_level_range = []
    for number in range(hero.level-1,hero.level+3):
        monster_level_range.append(number)

    random_int = randint(hero.level-1,hero.level+2)


