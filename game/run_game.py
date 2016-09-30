from database.peewee_model import *
from database.Admin_User import Admin
from sqlite3 import *
import peewee
from database.db import db


def run_game():
    print('The game is running theoretically.')

db.connect()
db.create_tables([Hero_Model,Monster_Model,Admin_User], safe=True)

run_game()
