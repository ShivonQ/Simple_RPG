from database import admin_displays
from database import db
import sys

def Admin_DB():
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
    Admin_DB()

def insert_monster_loop():
    print('Here we insert a monster')

def delete_monster_loop():
    print('Here we Delete a monster')

def delete_hero_loop():
    print('Here we delete a hero')

def create_admin_loop():
    print('here we make more admins')