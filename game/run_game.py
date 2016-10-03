from database.peewee_model import *
from database.Admin_User import Admin
from database.Admin_DB import *
from sqlite3 import *
import peewee
from database.db import db
from game.displays import *
from game.Combat import Combat
import sys

#   print('|    1) Drink a Potion Before Bed          2) Go to Bed                        |')

def run_program():
    print('The game is running theoretically.')
    root_loop()
# Find a better place for this DB enabling stuff
# db.connect()
# db.create_tables([Hero_Model,Monster_Model,Admin_User], safe=True)

def root_loop():
    while True:
        display_root_menu()
        # '|      1) New Game     2) Open Saved Game     3) Enter Admin Section           |'
        try:
            user_choice = int(input('|    What would you like to do brave warrior?                                  |'))
            if user_choice in (1,2,3):
                root_menu_methods(user_choice)
            if user_choice == 4:
                sys.exit()
            else:
                pass
        except ValueError:
            print('| Before we can begin you need to actually select one of these options!        |\n'
                  ' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ')
#                  |    What would you like to do brave warrior?                                  |


def root_menu_methods(choice):
    if choice == 1:
        print('| Make a new Hero and begin.                                                   |')
        our_hero = new_hero_creation()
        run_game(our_hero)

    if choice == 2:
        # If the user has a hero already, check for it, then open that game
        hero_name = input('|                  What is your hero known as in this realm?                   |')
        saved_hero = fetch_hero_make_object(hero_name)
        if saved_hero!=False:
            run_game(saved_hero)
        else:
            print('|                     That hero is not in this realm.                          |')

    if choice == 3:
        login_loop()


def run_game(hero):
    print('|         Welcome brave {} to the real world, you gaze upon \n'
          '|             it ready to take your place in legend.                           |'.format(hero.name))
    display_base_hero_options()
    #     '|      1) New Game     2) Open Saved Game     3) Enter Admin Section           |'
    while True:
        try:
            choice = int(input('|                          What is your choice Hero?                           |'))
            if choice in (1, 2, 3, 4, 5):
                base_hero_options_loop(hero, choice)
            else:
                pass
        except ValueError:
            print('|{} points at a random object nearby, looks up into the sky then shrugs.'.format(hero.name))


def base_hero_options_loop(hero, choice):
    if choice == 1:
        # This option in the future will be availiable, but you won't always be able to find a merchant.
        #     '| Before we can begin you need to actually select one of these options!        |\n'
        print('| You search and Search for a merchant but do not find one!                    |')
    if choice == 2:
        #         This option will let the user drink one of their potions.
        # in the next version any combat potioins will check to see if the users state == 'combat'
        print('| {} doesn\'t have any potions. They have\'t even heard of potions before now.'.format(hero.name))
    if choice == 3:
        rest_option(hero)
    if choice == 4:
        # Add in the location generator here later
        #         Normal Combat Occurrs Here
        combat_sequence(hero)
    if choice == 5:
        exists = check_if_hero_exists(hero)
        if exists:
            modify_hero_save(hero)
            sys.exit()
        else:
            create_hero_save(hero)
            sys.exit()


def combat_sequence(hero):
    monster = random_monster_encounter(hero)
    reg_combat = Combat(hero, monster)
    reg_combat.battle_time()


def rest_option(hero):
    #         Rest the night
    rest_enc = did_random_rest_encounter_occur()
    if rest_enc:
        monster = random_monster_encounter(hero)
        rest_combat = Combat(hero, monster)
        rest_combat.battle_time()
    else:
        hero.gain_hp_from_rest(True)


def new_hero_creation():
    #            '|      1) New Game     2) Open Saved Game     3) Enter Admin Section           |'
    name = input('|                  What is your name Hero?                                     |')
    # Make that hero!
    new_hero = Hero(name)
    # Modify that Hero!
    new_hero.set_starter_stats()
    return new_hero


run_program()
