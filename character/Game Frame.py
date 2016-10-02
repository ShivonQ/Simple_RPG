from tkinter import Tk, Label, Button, W, E, S, N, StringVar, PhotoImage, Entry
# from game import Combat, displays, Encounters, Location_Generator, run_game
# from database import Admin_User, admin_displays , data_validator, db, peewee_model, Admin_DB
from character.Hero import Hero
from character.Monster import Monster
from character.Item import Item
from character.Inventory import Inventory
# from character.Merchant import Merchant
from random import randint

import math


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Simple RPG")

        # labels for charaters and items
        self.Hero = Label(master, text="Warrior")
        self.Hero.grid(column=0, row=1)
        self.HeroStr = StringVar()
        self.HeroEntry = Entry(master,
                               textvariable=self.HeroStr)
        self.HeroEntry.grid(column=1, row=1)

        self.HeroHp = Label(master, text="Warrior HP")
        self.HeroHp.grid(column=0, row=2)

        self.armor = Label(master, text="Armor")
        self.armor.grid(column=0, row=3)
        self.armorStr = StringVar()
        self.armorEntry = Entry(master,
                                textvariable=self.armorStr)
        self.armorEntry.grid(column=1, row=4)

        self.strenght = Label(master, text="Str")
        self.strenght.grid(column=0, row=4)
        self.strenghtStr = StringVar()
        self.strenghtEntry = Entry(master,
                                   textvariable=self.strenghtStr)
        self.strenghtEntry.grid(column=1, row=3)

        self.Monster = Label(master, text="Monster")
        self.Monster.grid(column=4, row=1)

        self.MonsterHp = Label(master, text="Monster Hp")
        self.MonsterHp.grid(column=4, row=2)

        self.locationLabel = Label(master, text="Battle Location")
        self.locationLabel.grid(column=4, row=4)
        self.locationStr = StringVar()
        self.locationEntry = Entry(master,
                                   textvariable=self.locationStr)
        self.locationEntry.grid(column=5, row=4)

        self.results = StringVar()
        self.resultsLabel = Label(self, text="\n", textvariable=self.resultsVar)
        self.resultsLabel.pack()

        # dont need the label for flee.
        # self.run = Label(master, text="Flee")
        # self.run.grid(columnspan=2, rowspan=4)


        # Command buttons
        self.attk_button = Button(master, text="Attack", command=self.attk)
        self.attk_button.grid(column=0, row=6)

        self.Mon_button = Button(master, text="Monster Attack", command=self.Mon)
        self.Mon_button.grid(column=1, row=6)

        self.run_button = Button(master, text="Flee", command=self.run)
        self.run_button.grid(column=2, row=6)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(column=3, row=6)

        self.bpResults_button = Button(master, text="Bp Result", command=self.bpResults)
        self.bpResults_button.grid(column=4, row=6)

    def getName(self):
        return self.HeroEntry

    def getMonster(self):
        return self.Monster

    def getMonsterHp(self):
        return self.MonsterHp

    def getarmor(self):
        return self.armorEntry

    def getStrenght(self):
        return self.strenght

    def getLocation(self):
        return self.locationEntry

    def attk(self):
        print("kill them")

    def Mon(self):
        print("Uggg")

    def run(self):
        print("run away")

   # def bpResults(self):
    #    return self.bpResults()

    def results(self):
        Hero = self.HeroStr.get()
        # Hero = set_starter_stats.get()
        armor = self.armorStr.get()
        Strenght = self.strenghtStr.get()
        Monster = self.MonsterStr.get()
        #MonsterHp = self._monsterHpStr.get()
        location = self.locationStr.get()
        results = self.resultsLabel.get()

        if results is None:
            results = ""
        else:
            results = ""

        self.resultsVar.set(results)

        print("Battle", " in the", location, "$", Hero, "fought a ", Monster, armor, Strenght)


'''def main():
    GUI().mainloop()


main()'''

root = Tk()
my_game = GUI(root)
root.mainloop()