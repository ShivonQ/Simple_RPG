from tkinter import *
import sqlite3

import math

class GameDisplay(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('GameDisplay')
        self.grid()

        self._heroLabel = Label(self, text = "Hero")
        self._heroLabel.grid(row = 0, column = 0)
        self._heroStr = stringVar()
        self._heroEntry = Entry(self,
                                textvariable = self._heroStr)
        self._heroEntry.grid(row = 0, column = 1)

        self._hero_HpLabel = Label(self, text = "Hero Hp")
        self._hero_HpLabel.grid(row = 0, column = 2)
        self._hero_HpStr = StringVar()
        self._hero_HpEntry =Entry(self,
                                  textvariable = self._hero_hpStr)
        self._hero_HpEntry.grid(row = 0, column = 3)


        self._monsterLabel = Label(self, text = "Monster")
        self._monsterLabel.grid(row = 1, column = 0)
        self._monsterStr = StringVar()
        self._monsterEntry =Entry(self,
                                  textvariable = self._monsterStr)
        self._monsterEntry.grid(row = 1, column = 1)


        self._monster_HpLabel = Label(self, text = "Monster Hp")
        self._monster_HpLabel.grid(row = 1, column = 2)
        self._monster_HpStr = StringVar()
        self._monster_HpEntry =Entry(self,
                                  textvariable = self._monster_HpStr)
        self._monster_HpEntry.grid(row = 1, column = 3)



