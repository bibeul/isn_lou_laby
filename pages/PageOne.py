from tkinter import *
from datetime import timedelta
import tkinter as tk


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl = Label(self, text="Hello")
        self.lbl.grid(column=0, row=0)
        btn = Button(self, text="Start Game !", command=self.changeLabel)
        hst = Button(self, text="? histoire")
        physique = Button(self, text="? physique")
        math = Button(self, text="? math")
        math.grid(column=2, row=3)
        hst.grid(column=2, row=2)
        physique.grid(column=2, row=1)
        btn.grid(column=2, row=0)


    def update_clock(self, n=0):
        now = timedelta(seconds=10) - timedelta(seconds=n)
        print(now)
        if now <= timedelta(minutes=0):
            self.lbl.configure(text="Perdu")
            return

        self.lbl.configure(text=now)
        self.after(1000, lambda: self.update_clock(n + 1))

    def changeLabel(self):
        self.lbl.configure(text="Game start !!")
        self.update_clock()
