from character.Hero import Hero
from character.Monster import *

from tkinter import *
import random
import math


class GameDesign(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("GameDesign")
        self.grid()

        self.HeroLabel = Label(self, text="Hero")
        self.HeroLabel.grid(row=0, column=0)
        self.HeroStr = StringVar()
        self.HeroEntry = Entry(self,
                                textvariable=self.HeroStr)
        self.HeroEntry.grid(row=0, column=1)

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

        self.MonsterLabel = Label(self, text="Monster")
        self.MonsterLabel.grid(row=0, column=2)
        self.MonsterStr = StringVar()
        self.MonsterEntry = Entry(self,
                                   textvariable=self.MonsterStr)
        self.MonsterEntry.grid(row=0, column=3)

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


    #def c



    def _bpResults(self):
        hero = self.HeroStr.get()
        armor = self._armorStr.get()
        strenght = self._strStr.get()
        monster = self.MonsterStr.get()
        monsterHp = self._monsterHpStr.get()
        location = self._locationStr.get()
        money = self._moneyStr.get()

        self._bpResultsVar.set

        print("Battle", " in the", location, "$", hero, "fought a ", monster)


def main():
    GameDesign().mainloop()


main()