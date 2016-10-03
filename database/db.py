from peewee import *
from tabulate import tabulate
from database.peewee_model import *
from database.admin_displays import *
from character.Monster import Monster
from character.Merchant import Merchant
from random import randint
from character.Hero import Hero
from time import sleep
import sqlite3
# TODO: Add try Excepts to all saves,
# this is our database handler, it calls on the peewee data models that are set up
db = SqliteDatabase('./game/simple_rpg.db')


def did_random_rest_encounter_occur():
    chance = randint(1, 100)
    chance_range = (10)
    if chance <= chance_range:
        print('A random encounter happens while you were sleeping')
        encounter_chance = randint (1,100)
        monster_chance = (50)
        if encounter_chance <= monster_chance:
            print('You are attacked by a monster while you were trying to sleep!')
            random_monster_encounter()
            return True
        else:
            print('A wandering merchant approaches your camp')
            return True

    else:
        print('You sleep peacefully.')
        Hero.gain_hp_from_rest()
        return False


def random_monster_encounter(hero):
    # figure out the levels the monster can be, not too low or too high
    random_level = randint(hero.level - 1, hero.level + 2)
    # grab a monster, send it back for fighting
    monster = fetch_monster_make_object(random_level)
    # return that monster so the Encounters File can use them
    return monster


# and adds or modifies them.
def add_monster(monster_object):
    print('Adding a Monster')
    new_monster = Monster_Model.create(name=monster_object.name,
                                                    max_hp=monster_object.max_hp,
                                                    xp_val=monster_object.xp_val,
                                                    money=monster_object.money,
                                                    armor=monster_object.armor,
                                                    strength=monster_object.strength,
                                                    level=monster_object.level
                                                    )
    new_monster.save()


def create_hero_save(hero_object):
    print('Create a Save Game')
    new_save = Hero_Model.create(name=hero_object.name,
                                              current_hp=hero_object.hp,
                                              max_hp=hero_object.max_hp,
                                              armor=hero_object.armor,
                                              strength=hero_object.strength,
                                              xp=hero_object.xp,
                                              level=hero_object.level,
                                              money=hero_object.money,
                                              next_level=hero_object.next_level)
    new_save.save()

def fetch_monster_make_object(level):
    '''THE ONLY REAL FIX FOR THIS IS TO DO MULTITHREADING APPARENTLY
        SINCE I PUT IN THE PAUSES IT IS FAR MORE LIKELY TO SUCCEED THAN NOT.  BUT IT STILL CRASHES SOMETIMES'''
    # TODO: Make this Multithreaded for true success
    error = True
    if level <= 0:
        level = 1
    list_o = []
    while error:
        try:
            for monster in Monster_Model.select():
                print('Made it into the loop1')
                if monster.level == level:
                    print('made it into the loop')
                    loop_mon = Monster(monster.name,monster.xp_value,monster.money,monster.level)
                    loop_mon.set_str_and_armor(monster.strength, monster.armor, monster.max_hp)
                    sleep(0.1)
                    list_o.append(loop_mon)
            sleep(1)

            rand_mons = randint(0, len(list_o))
            final_mons = list_o[rand_mons]
            error = False
            return final_mons
        except IndexError:
            print('Test Index Error')


def fetch_hero_make_object(name):
    # get the save data
    this_hero = Hero_Model.get(Hero_Model.name.startswith(name))
    # initialize the object
    hero_object = Hero(name)
    # call the set_opened_save function
    hero_object.set_opened_save_stats(this_hero.current_hp,
                                      this_hero.max_hp,
                                      this_hero.armor,
                                      this_hero.strength,
                                      this_hero.xp,
                                      this_hero.level,
                                      this_hero.money,
                                      this_hero.next_level)
    return hero_object


def modify_hero_save(hero_object):
    # This will overwrite anything in the old file with the new info
    this_hero = Hero_Model.get(Hero_Model.name.startswith(hero_object.name))
    this_hero.current_hp = hero_object.hp
    this_hero.max_hp = hero_object.max_hp
    this_hero.armor = hero_object.armor
    this_hero.strength = hero_object.strength
    this_hero.xp = hero_object.xp
    this_hero.level = hero_object.level
    this_hero.money = hero_object.money
    this_hero.next_level = hero_object.next_level
    this_hero.save()


def add_admin_user(user_object):
    this_admin = Admin_User.create(username=user_object.username,
                                                password=user_object.password)
    this_admin.save()


def check_for_admin_priveleges(username, password):
    try:
        admin = Admin_User.get(Admin_User.username.startswith(username))
        if admin.password == password:
            display_successful_login()
            return True
        else:
            display_invalid_pw()
            return False
    except DoesNotExist:
        display_invalid_login_attempt()
        return False


def delete_hero(hero_name):
    try:
        this_record = Hero_Model.get(Hero_Model.name.startswith(hero_name))
        this_record.delete_instance()

    except DoesNotExist:
        print('Sorry, but {} doesn\'t exist, and cannot be deleted.'.format(hero_name))


def show_all_heroes():
    big_list = []
    for record in Hero_Model:
        small_list = compile_hero_record(record)
        big_list.append(small_list)
    #     TODO: add an empty list stopper or something
    print(tabulate(big_list, headers=['Hero Name', 'Level', 'XP', 'Next Level', 'Money'], tablefmt='pipe'))
    if len(big_list)<1:
        return False
    else:
        return True


def show_all_monsters():
    big_list = []
    for monster in Monster_Model:
        small = compile_monster_record(monster)
        big_list.append(small)
    #     TODO: Add a if table is empty dont print anything/skip it all
    print(tabulate(big_list, headers=['Name', 'Level', 'Max HP', 'Strength', 'Armor', 'XP Value', 'Money'],
                   tablefmt='pipe'))
    if len(big_list)<1:
        return False
    else:
        return True

#start of the merchant block

def add_merchant(merchant_object):
    print('Adding a Merchant')
    new_merchant = Merchant_Model.create(name=merchant_object.name,
                                                    max_hp=merchant_object.max_hp,
                                                    money=merchant_object.money,
                                                    armor=merchant_object.armor,
                                                    inventory=merchant_object.inventory
                                                    )
    new_merchant.save()

def fetch_merchant_make_object(name):

    this_merchant = Merchant_Model.get(Merchant_Model.name)
    Merchant_object = Merchant(name)

    Merchant_object.set(this_merchant.max_hp,
                                      this_merchant.armor,
                                      this_merchant.money,
                                      this_merchant.inventory)
    return Merchant_object

def show_all_merchants():
    big_list = []
    for merchant in Merchant_Model:
        small = compile_merchant_record(Merchant)
        big_list.append(small)
    print(tabulate(big_list, headers=['Name', 'Max HP', 'Armor', 'Money', 'Inventory'],
                   tablefmt='pipe'))
    if len(big_list)<1:
        return False
    else:
        return True

def compile_merchant_record(record):
    small_list = [record.name, record.max_hp, record.armor, record.money, record.inventory]
    return small_list

def compile_hero_record(record):
    small_list = [record.name,record.level, record.xp, record.next_level, record.money]
    return small_list


def compile_monster_record(record):
    small_list = [record.name, record.level, record.max_hp, record.strength, record.armor, record.xp_value, record.money]
    return small_list

# show_all_monsters()