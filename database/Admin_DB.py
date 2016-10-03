from database import admin_displays
from database.db import *
import sys
from sqlite3 import IntegrityError
from character.Monster import *
from character.Merchant import *
from database.peewee_model import *
from database.Admin_User import *


def make_default_admin():
    u = 'admin'
    pw = 'password'
    try:
        new_admin = Admin_User(u,pw)
        new_admin.save()
    except IntegrityError:
        print('\t\t    ? \t\t    ')


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
            break
        else:
            print('That was not an option.')


def login_loop():
    make_default_admin()
    valid_or_not = False
    while valid_or_not == False:
        admin_displays.display_admin_login()
        u_name = input('Please enter your username.\n')
        pw = input('Please enter your password\n')
        valid_or_not = check_for_admin_priveleges(u_name,pw)
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
            armor = int(input('What is the monsters Armor? Minimum of 0.'))
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
            money = int(input('How much Money does the monster have? Minimum of 0.'))
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
    # Now that all that data has been collected we toss it into the Peewee model, and send it to the DB
    new_monster = Monster(name,xp_val,money,level)
    new_monster.set_str_and_armor(strength, armor, max_hp)
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
    delete_loop = True
    while delete_loop:
        present = show_all_heroes()
        if present == False:
            print('Sorry, there are no Heros as you can see.')
            break
        else:
            to_delete = input('Which Hero do you want to delete? Enter it\'s name.')
            while True:
                y_o_n = input('You are trying to delete {}, is that the record you mean to delete?'.format(to_delete))
                if y_o_n.lower() == 'y' or y_o_n.lower == 'yes':
                    try:
                        this_record = Hero_Model.get(Hero_Model.name.startswith(to_delete))
                    except DoesNotExist:
                        print('That Hero Does not exist.')
                        delete_loop = False
                        break
                    this_record.delete_instance()
                    # TODO: Make sure that if there are no records at all this either stops or doesn't begin at all.
                    delete_loop = False
                    break
                else:
                    print('The delete was aborted.')
                    break

def insert_merchant_loop():
    print('Here we insert a merchant')
    name = input('Give the merchant a name')
    while True:
        try:
            max_hp = int(input('What is the merchants maximum HP?'))
            if max_hp<1:
                print('Value has to be greater than 0')
            else:
                break
        except ValueError:
            print('It has to be an Integer value.')
    while True:
        try:
            armor = int(input('What is the merchants Armor? Minimum of 0.'))
            if armor<0:
                print(' Invalid value, it has to be 0 or greater.')
            else:
                break
        except ValueError:
            print('Armor value has to be an integer.')
    while True:
        try:
            money = int(input('How much Money does the merchant have? Minimum of 500.'))
            if money < 500:
                print(' Remember, the value has to be 500 minimum.')
            else:
                break
        except ValueError:
            print('Money value has to be an integer.')
    while True:
        try:
            #probably it needs to be expanded to add more than two items
            inventory = inventory.add_item(input('What is the merchant carrying?'))
            y_o_n = input('Do you want to add another item?')
            if y_o_n.lower() == 'y' or y_o_n.lower == 'yes':
                inventory = inventory.add_item(input('What is the merchant carrying?'))
        except ValueError:
            print('We got an error')
    new_merchant = Merchant(name,money)
    new_merchant.set_armor_max_hp(armor, max_hp)
    add_merchant(new_merchant)


def delete_merchant_loop():
    print('Here we Delete a merchant')
    delete_loop = True
    while delete_loop:
        show_all_merchants()
        to_delete = input('Which merchant do you want to delete? Enter the name of the merchant.')
        while True:
            y_o_n = input('You are trying to delete {}, is that the record you mean to delete?'.format(to_delete))
            if y_o_n.lower() == 'y' or y_o_n.lower == 'yes':
                this_record = Merchant_Model.get(Merchant_Model.name.startswith(to_delete))
                this_record.delete_instance()
                delete_loop = False
                break
            else:
                print('Couldnt perform the delete operation.')
                break



def create_admin_loop():
    print('here we make more admins')
    username = input('What will this admins username be?')
    pw = input('What will this Admins Password Be?')

    new_admin = Admin_User(username,pw)
    new_admin.save()


def delete_admin_loop():
    print('Here we delete other admins.\n'
          '-----DANGEROUS TERRITORY-----\n'
          '----DONT DELETE YOURSELF!----')
#     TODO: Figure out a way to make sure that there is always one admin before we implement this.
