import tkinter as tk
from tkinter import font  as tkfont
from pages import PageOne, PageTwo, StartPage, PageQuest

list_question = {}

list_question["equations" """=B(M)"""] = {
    1: "8x^2+3x-8=68/-68",
    2: "5x^2-4x+8=pas de solutions",
    3: "2x^2-7x+9=0",
}

list_question["dérivé expo" """=A(M)"""] = {
    1: "e^3",
    2: "e^2",
    3: "e^4",
}

list_question["integrales" """=C(M)"""] = {
    1: "e^x^2=1.462",
    2: "e^x^3=1.359",
    3: "e^x^4=1.496",
}

list_question["culture maths" """=D(M)"""] = {
    1: "le nombre pi n'est pas transcendant,",
    2: "stochastique= mesure et analyse harmonique",
    3: "l'équation Navier-Stoke=comprendre les courants marins",
}

list_question["Palindrome" """=E(M)"""] = {
    1: "17371 est un nombre palindrome",
    2: "96568 est un nombre palindrome",
    3: "un palindrome= nombre à 4 chiffres",
}

list_question["maths"] = {
    1: {
        "rep1": "8x^2+3x-8=68/-68",
        "rep2": "5x^2-4x+8=pas de solutions",
        "rep3": "2x^2-7x+9=0",
        "good": "rep3"
    },
    2: {
        "rep1": "non",
        "rep2": "oui",
        "rep3": "non",
        "good": "rep2"
    },
    3: {
        "rep1": "oui",
        "rep2": "non",
        "rep3": "non ",
        "good": "rep1"
    },
    4: {
        "rep1": "non",
        "rep2": "non",
        "rep3": "oui ",
        "good": "rep3"
    },
    5: {
        "rep1": "oui",
        "rep2": "non",
        "rep3": "non ",
        "good": "rep1"
    }
}

list_question["vrai/faux" """=A(PC)"""] = {
    1: "nous ne sommes pas seuls dans l'espace",
    2: "il y a une seule dimension dans l'univers",

}

list_question["liaisons hydrogènes" """=B(PC)"""] = {
    1: "un atome d'azote possède 3 liaisons",
    2: "un atome d'hydrogène possède 2 liaisons",
    3: "un atome de crabone possède 4 liaisons",
}

list_question["vitesse de la lumiere" """=C(PC)"""] = {
    1: "3.0x10^8 m/s",
    2: "3.171002504x10^-16 a.l",
    3: "300000000 m/s",
}

list_question["physique"] = {
    "A": {
        "rep1": "non",
        "rep2": "oui",
        "good": "rep2"
    },
    "B": {
        "rep1": "non",
        "rep2": "non",
        "rep3": "oui",
        "good": "rep3"
    },
    "C": {
        "rep1": "oui",
        "rep2": "oui",
        "rep3": "oui",
        "good": "rep1, rep2, rep3"
    },
}

list_question["dates" """=A(HST)"""] = {
    1: "1965= transfert des cendres de Jean Moulin",
    2: "1957=traité de Rome",
    3: "1959= 5eme republique",
}

list_question["présidents" """=B(HST)"""] = {
    1: "1920=R.Poincaré",
    2: "1945=C.de Gaulle",
    3: "1981=F.Mitterant",
}

list_question["Simone Veil" """=C(HST)"""] = {
    1: "Née un 13 juillet",
    2: "Amie avec F.Hollande",
    3: "Déportée à Dachau",
}

list_question["histoire"] = {
    "A": {
        "rep1": "non",
        "rep2": "oui",
        "rep3": "non",
        "good": "rep2"
    },
    "B": {
        "rep1": "non",
        "rep2": "non",
        "rep3": "oui",
        "good": "rep3"
    },
    "C": {
        "rep1": "oui",
        "rep2": "non",
        "rep3": "non ",
        "good": "rep3"
    }
}

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        """constructeur de la classe: fonction appelé à l'initialisation d'un objet de cette classe"""
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.question_type = "math"
        self.cpt = {"maths": 0, "physique": 0, "histoire": 0}


        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        """assigne nvl frame au container et le met en forme"""
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        """self = objet= instance d'une classe"""
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageQuest):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        print(self.question_type)
        frame.update()
        frame.tkraise()



if __name__ == "__main__":
    """mane loop pour commencer le programme"""
    app = SampleApp()
    app.mainloop()
