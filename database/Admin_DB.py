from database import admin_displays
from database.db import *
import sys
from sqlite3 import IntegrityError
from character.Monster import *
from database.peewee_model import *
from database.Admin_User import *


def admin_db():
    while True:
        admin_displays.display_admin_menu()
        choice = 0
        try:
            choice = int(input('What is your choice Admin?\n'))
        except ValueError:
            print('That was not a valid Integer.')
        if choice == 1:
            insert_monster_loop()
        elif choice == 2:
            delete_monster_loop()
        elif choice == 3:
            delete_hero_loop()
        elif choice == 4:
            create_admin_loop()
        elif choice == 5:
            sys.exit()
        else:
            print('That was not an option.')


def login_loop():
    valid_or_not = False
    while valid_or_not == False:
        admin_displays.display_admin_login()
        u_name = input('Please enter your username.\n')
        pw = input('Please enter your password\n')
        valid_or_not = db.check_for_admin_priveleges(u_name,pw)
    admin_db()


def insert_monster_loop():
    print('Here we insert a monster')
    name = input('Please Give Monster Name')
    while True:
        try:
            max_hp = int(input('What is the monsters Max HP? Minimum of 1.'))
            if max_hp<1:
                print('That was not greater than 0')
            else:
                break
        except ValueError:
            print('Sorry that was not an Integer.')
    while True:
        try:
            strength = int(input('what is this monsters strength? Minimum is 1.'))
            if strength<1:
                print('Sorry that was not 1 or greater.')
            else:
                break
        except ValueError:
            print('Sorry, that wasn\'t a Integer.')
    while True:
        try:
            armor = int(input('What is the monsters Strength? Minimum of 0.'))
            if armor<0:
                print(' That was an invalid number, positive numbers only.')
            else:
                break
        except ValueError:
            print('Sorry that was not an Integer.')
    while True:
        try:
            xp_val = int(input('What is the monsters XP Value? Minimum of 1.'))
            if xp_val < 0:
                print(' That was an invalid number, positive numbers only, greater than 0.')
            else:
                break
        except ValueError:
            print('That is not an integer.')
    while True:
        try:
            money = int(input('Ho much Money does the monster have? Minimum of 0.'))
            if money < 0:
                print(' That was an invalid number, positive numbers only.')
            else:
                break
        except ValueError:
            print('Sorry that was not an Integer.')
    while True:
        try:
            level = int(input('What is the monsters level? Minimum of 1.'))
            if level < 0:
                print(' That was an invalid number, positive numbers only.')
            else:
                break
        except ValueError:
            print('Sorry that was not an Integer.')

    new_monster = Monster(name,max_hp,xp_val,money,armor,strength,level)
    add_monster(new_monster)


def delete_monster_loop():
    print('Here we Delete a monster')
    # Call the show monster function from db.py
    delete_loop = True
    while delete_loop:
        show_all_monsters()
        to_delete = input('Which monster do you want to delete? Enter it\'s name.')
        while True:
            y_o_n = input('You are trying to delete {}, is that the record you mean to delete?'.format(to_delete))
            if y_o_n.lower() == 'y' or y_o_n.lower == 'yes':
                this_record = Monster_Model.get(Monster_Model.name.startswith(to_delete))
                this_record.delete_instance()
                # TODO: Make sure that if there are no records at all this either stops or doesn't begin at all.
                delete_loop = False
                break
            else:
                print('The delete was aborted.')
                break




def delete_hero_loop():
    print('Here we delete a hero')


def create_admin_loop():
    print('here we make more admins')


admin_db()