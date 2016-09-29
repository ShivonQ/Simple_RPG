from peewee import *
from tabulate import tabulate
from database.peewee_model import *
from database.admin_displays import *
from character.Monster import Monster
import sqlite3
# TODO: Add try Excepts to all saves,
# this is our database handler, it calls on the peewee data models that are set up
db = SqliteDatabase('simple_rpg.db')


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
    this_monster = Monster_Model.get(Monster_Model.level(level))
# name, max_hp, xp_val, money, armor, strength, level
    final_monster = Monster(this_monster.name,this_monster.max_hp, this_monster.xp_value,this_monster.money,this_monster.strength, this_monster.level)
    return final_monster


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
        admin = Admin_User.get(Admin_User.startswith(username))
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


def compile_hero_record(record):
    small_list = [record.name,record.level, record.xp, record.next_level, record.money]
    return small_list


def compile_monster_record(record):
    small_list = [record.name, record.level, record.max_hp, record.strength, record.armor, record.xp_value, record.money]
    return small_list
