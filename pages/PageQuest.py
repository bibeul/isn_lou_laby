import tkinter as tk


class PageQuest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.question_text = tk.Label(self, text="coche la bonne reponse")
        self.question_text.pack()

        self.bouton_rep1 = tk.Button(self, text="!")
        self.bouton_rep2 = tk.Button(self, text="!")
        self.bouton_rep3 = tk.Button(self, text="!")

        self.bouton_rep1.pack()
        self.bouton_rep2.pack()
        self.bouton_rep3.pack()

        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()

        self.list_question = {}
        self.list_question["maths"] = {
            0: {
                "rep1": "8x^2+3x-8=68/-68",
                "rep2": "5x^2-4x+8=pas de solutions",
                "rep3": "2x^2-7x+9=0",
                "good": "rep3"
            },
            1: {
                "rep1": "non",
                "rep2": "oui",
                "rep3": "non",
                "good": "rep2"
            },
            2: {
                "rep1": "oui",
                "rep2": "non",
                "rep3": "non ",
                "good": "rep1"
            },
            3: {
                "rep1": "non",
                "rep2": "non",
                "rep3": "oui ",
                "good": "rep3"
            },
            4: {
                "rep1": "oui",
                "rep2": "non",
                "rep3": "non ",
                "good": "rep1"
            }
        }

        self.list_question["histoire"] = {
            0: {
                "rep1": "non",
                "rep2": "oui",
                "rep3": "non",
                "good": "rep2"
            },
            1: {
                "rep1": "non",
                "rep2": "non",
                "rep3": "oui",
                "good": "rep3"
            },
            3: {
                "rep1": "oui",
                "rep2": "non",
                "rep3": "non ",
                "good": "rep3"
            }
        }

        self.list_question["physique"] = {
            0: {
                "rep1": "non",
                "rep2": "oui",
                "rep3": "non",
                "good": "rep2"
            },
            1: {
                "rep1": "non",
                "rep2": "non",
                "rep3": "oui",
                "good": "rep3"
            },
            2: {
                "rep1": "oui",
                "rep2": "oui",
                "rep3": "oui",
                "good": "rep1, rep2, rep3"
            },
        }

#    def correction(self):

    def update(self):
        type = self.controller.question_type
        self.bouton_rep1.configure(text= self.list_question[type][self.controller.cpt[type]]["rep1"])
        self.bouton_rep2.configure(text= self.list_question[type][self.controller.cpt[type]]["rep2"])
        self.bouton_rep3.configure(text= self.list_question[type][self.controller.cpt[type]]["rep3"])
        self.controller.cpt[type] = (self.controller.cpt[type] + 1) % len(self.list_question[type])
        print(self.controller.cpt)
