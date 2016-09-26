
from tkinter import *
import sqlite3

import math


class GameDisplay(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('GameDisplay')
        self.grid()

        self._heroLabel = Label(self, text="Hero")
        self._heroLabel.grid(row=0, column=0)
        self._heroStr = StringVar()
        self._heroEntry = Entry(self,
                                textvariable=self._heroStr)
        self._heroEntry.grid(row=0, column=1)

        self._heroHpLabel = Label(self, text="Hero Hp")
        self._heroHpLabel.grid(row=0, column=2)
        self._heroHpStr = StringVar()
        self._heroHpEntry = Entry(self,
                                  textvariable=self._heroHpStr)
        self._heroHpEntry.grid(row=0, column=3)

        self._heroArmorLabel = Label(self, text="Hero Armor")
        self._heroArmorLabel.grid(row=0, column=4)
        self._heroArmorStr = StringVar()
        self._heroArmorEntry = Entry(self,
                                  textvariable=self._heroArmorStr)
        self._heroArmorEntry.grid(row=0, column=5)

        self._monsterLabel = Label(self, text="Monster")
        self._monsterLabel.grid(row=1, column=0)
        self._monsterStr = StringVar()
        self._monsterEntry = Entry(self,
                                   textvariable=self._monsterStr)
        self._monsterEntry.grid(row=1, column=1)

        self._monsterHpLabel = Label(self, text="Monster Hp")
        self._monsterHpLabel.grid(row=1, column=2)
        self._monsterHpStr = StringVar()
        self._monsterHpEntry = Entry(self,
                                     textvariable=self._monsterHpStr)
        self._monsterHpEntry.grid(row=1, column=3)



        self._locationLabel = Label(self, text="Battle Location")
        self._locationLabel.grid(row=3, column=0)
        self._locationStr = StringVar()
        self._locationEntry = Entry(self,
                                    textvariable=self._locationStr)
        self._locationEntry.grid(row=3, column=1)

        self._button = Button(self, text="Battle button", command=self._bpResults)
        self._button.grid(row=5, column=0, columnspan=2)

    def _bpResults(self):
        hero = self._heroHpStr.get()
        monster = self._monsterHp.get()
        location = self._locationStr.get()
        battle = hero / monster
        self._bpResultsVar.set


def main():
    GameDisplay().mainloop()


main()