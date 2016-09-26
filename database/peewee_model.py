import sqlite3
from peewee import *

db = SqliteDatabase('simple_rpg.db')


class Base_Model(Model):
    class Meta:
        database = db


class Admin_User(Base_Model):
    username = CharField(max_length=20, unique=True)
    password = CharField(max_length=30, unique=True)


class Monster_Model(Base_Model):
    name = CharField(max_length=60, unique=True)
    max_hp = IntegerField(null=False, default=1)
    strength = IntegerField(null=False, default=1)
    armor = IntegerField(null=False, default=1)
    level = IntegerField(null=False, default=1)
    xp_value = IntegerField(null=False, default=5)
    money = IntegerField(null=False, default=0)


class Hero_Model(Base_Model):
    name = CharField(max_length=60, unique=True)
    # TODO: Maybe Use _ID instead to filter. That way There can be multiple saves of same name.
    current_hp = IntegerField(null=False)
    max_hp = IntegerField(null=False, default=1)
    armor = IntegerField(null=False, default=1)
    strength = IntegerField(null=False, default=1)
    xp = IntegerField(null=False, default=0)
    level = IntegerField(null=False, default=1)
    money = IntegerField(null=False, default=0)
    next_level = IntegerField(null=False, default=100)