import sqlite3
from peewee import *

db = SqliteDatabase('simple_rpg.db')


class Base_Model(Model):
    class Meta:
        database = db

class Monster_Model(Base_Model):
    name = CharField(max_length=60, unique=False)
    max_hp = IntegerField(null=False, default=1)
    strength = IntegerField(null=False, default=1)
    armor = IntegerField(null=False, default=1)
    level = IntegerField(null=False, default=1)
    xp_value = IntegerField(null=False, default=10)

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

    def add_monster(self,monster_object):
        print('Adding a Monster')
        new_monster = Monster_Model.create(name=)


    def Create_Hero_Save(self, hero_object):
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

    def modify_Hero_Save(self,hero_object):
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
