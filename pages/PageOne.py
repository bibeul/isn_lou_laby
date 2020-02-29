from tkinter import *
from datetime import timedelta
import tkinter as tk


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl = Label(self, text="Hello")
        self.lbl.grid(column=0, row=0)

        self.btn = Button(self, text="Start Game !", command=self.startGame)
        self.hst = Button(self, text="? histoire", state=DISABLED, command=lambda: self.change_to_history_question(controller))
        self.physique = Button(self, text="? physique", state=DISABLED, command=lambda: self.change_to_physic_question(controller))
        self.math = Button(self, text="? math", state=DISABLED, command=lambda: self.change_to_maths_question(controller))

        self.math.grid(column=2, row=3)
        self.hst.grid(column=2, row=2)
        self.physique.grid(column=2, row=1)
        self.btn.grid(column=2, row=0)

        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid()

    def change_to_history_question(self, controller):
        controller.question_type = "histoire"
        controller.show_frame("PageQuest")

    def change_to_maths_question(self, controller):
        controller.question_type = "maths"
        controller.show_frame("PageQuest")

    def change_to_physic_question(self, controller):
        controller.question_type = "physique"
        controller.show_frame("PageQuest")


    def update_clock(self, n=0):
        now = timedelta(seconds=100) - timedelta(seconds=n)
        if now <= timedelta(minutes=0):
            self.lbl.configure(text="Perdu")
            return

        self.lbl.configure(text=now)
        self.after(1000, lambda: self.update_clock(n + 1))

    def startGame(self):
        self.lbl.configure(text="Game start !!")
        self.physique["state"] = 'normal'
        self.math["state"] = 'normal'
        self.hst["state"] = 'normal'
        self.btn["state"] = DISABLED
        self.update_clock()


#salut nathan