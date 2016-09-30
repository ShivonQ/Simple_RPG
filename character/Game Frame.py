from battle_result import NumGen
from tkinter import *
import tkinter as tk
import sqlite3
import random
import math


class GameDesign(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("GameDesign")
        self.grid()

        self._heroLabel = Label(self, text="Hero")
        self._heroLabel.grid(row=0, column=0)
        self._heroStr = StringVar()
        self._heroEntry = Entry(self,
                                textvariable=self._heroStr)
        self._heroEntry.grid(row=0, column=1)

        self._armorLabel = Label(self, text="armor")
        self._armorLabel.grid(row=2, column=0)
        self._armorStr = StringVar()
        self._armorEntry = Entry(self,
                                 textvariable=self._armorStr)
        self._armorEntry.grid(row=2, column=1)

        self._strLabel = Label(self, text="Str")
        self._strLabel.grid(row=1, column=0)
        self._strStr = StringVar()
        self._strEntry = Entry(self,
                               textvariable=self._strStr)
        self._strEntry.grid(row=1, column=1)

        self._monsterLabel = Label(self, text="Monster")
        self._monsterLabel.grid(row=0, column=2)
        self._monsterStr = StringVar()
        self._monsterEntry = Entry(self,
                                   textvariable=self._monsterStr)
        self._monsterEntry.grid(row=0, column=3)

        self._monsterHpLabel = Label(self, text="Monster Hp")
        self._monsterHpLabel.grid(row=1, column=2)
        self._monsterHpStr = StringVar()
        self._monsterHpEntry = Entry(self,
                                     textvariable=self._monsterHpStr)
        self._monsterHpEntry.grid(row=1, column=3)

        self._locationLabel = Label(self, text="Battle Location")
        self._locationLabel.grid(row=2, column=2)
        self._locationStr = StringVar()
        self._locationEntry = Entry(self,
                                    textvariable=self._locationStr)
        self._locationEntry.grid(row=2, column=3)

        self._moneyLabel = Label(self, text="Money")
        self._moneyLabel.grid(row=0, column=4)
        self._moneyStr = StringVar()
        self._moneyEntry = Entry(self,
                                 textvariable=self._moneyStr)
        self._moneyEntry.grid(row=0, column=5)

        '''the button f'''
        self._button = Button(self, text="Attk", command=self._battle)
        self._button.grid(row=4, column=0, columnspan=1)

        self._button = Button(self, text="Flee", command=self._bpResults)
        self._button.grid(row=5, column=0, columnspan=1)

        self._button = Button(self, text="Battle button", command=self._bpResults)
        self._button.grid(row=6, column=0, columnspan=1)

    def _battle(self):
        hero = int(input("Please enter a number up to 10. "))
        monster = random.randint(1, 10)
        """ x and z can both be used below without errors -- testing/learning"""

        randomNumber = random.randint(1, 50)
        print("hero attack does", randomNumber, "damg")
        if hero < monster:
            hero == ("winner")
            print("winner")
        elif hero > monster:
            hero == ("lose")
            print("lose")
        else:
            print("you lose")

        randomNumber = random.randint(1, 50)
        print("monster attack does", randomNumber, "damg")
        if monster < hero:
            monster == ("Winner")
            print("winner")
        elif monster > hero:
            monster == ("lose")
            print("lose")
        else:
            monster == ("monster defeated")
            print("monster defeated")

    def _bpResults(self):
        hero = self._heroStr.get()
        armor = self._armorStr.get()
        strenght = self._strStr.get()
        monster = self._monsterStr.get()
        monsterHp = self._monsterHpStr.get()
        location = self._locationStr.get()
        money = self._moneyStr.get()

        self._bpResultsVar.set

        print("Battle", " in the", location, "$", hero, "fought a ", monster)


def main():
    GameDesign().mainloop()


main()