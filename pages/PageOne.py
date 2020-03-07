from tkinter import *
from datetime import timedelta
import tkinter as tk

"""classe de la page 1: incluant des variables ou des fonctions qui permettent de definir un objet, ici tout ce qui 
compose la page 1. La classe 1 correspond au lancement du jeu et ainsi qu'au deroulement du jeu """

class PageOne(tk.Frame):
    def __init__(self, parent, controller):    
        """constructeur de la classe: fonction appelé à l'initialisation d'un objet de cette classe"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl = Label(self, text="Hello")
        self.lbl.grid(column=0, row=0)
        """intiation des boutons pour les categories de questions"""
        self.btn = Button(self, text="Start Game !", command=self.startGame)
        self.hst = Button(self, text="histoire", state=DISABLED, command=lambda: self.change_to_history_question(controller))
        self.physique = Button(self, text="physique", state=DISABLED, command=lambda: self.change_to_physic_question(controller))
        self.math = Button(self, text="maths", state=DISABLED, command=lambda: self.change_to_maths_question(controller))
        """initiation des emplacements des boutons des categories"""
        self.math.grid(column=2, row=3)
        self.hst.grid(column=2, row=2)
        self.physique.grid(column=2, row=1)
        self.btn.grid(column=2, row=0)
        """initiation dubouton retour afin de communiquer entre les fenetres"""
        button = tk.Button(self, text="retour", command=lambda: controller.show_frame("StartPage"))
        button.grid()
        """initialisation des fonctions pour changer de questions dans une categorie: histoire, maths ou physique"""

    def change_to_history_question(self, controller):
        controller.question_type = "histoire"
        controller.show_frame("PageQuest")


    def change_to_maths_question(self, controller):
        controller.question_type = "maths"
        controller.show_frame("PageQuest")


    def change_to_physic_question(self, controller):
        controller.question_type = "physique"
        controller.show_frame("PageQuest")

    """initiation des fonctions du timer et sa configuration"""
    def update_clock(self, n=0):
        now = timedelta(seconds=100) - timedelta(seconds=n)
        if now <= timedelta(minutes=0):
            self.lbl.configure(text="Perdu")
            return

        self.lbl.configure(text=now)
        self.after(1000, lambda: self.update_clock(n + 1))

    """definitions des boutons, apparent que lorsque l'on enclanche 'start game' sinon impossible d'etre utilisé"""
    def startGame(self):
        self.lbl.configure(text="Game start !!")
        self.physique["state"] = 'normal'
        self.math["state"] = 'normal'
        self.hst["state"] = 'normal'
        self.btn["state"] = DISABLED
        self.update_clock()
