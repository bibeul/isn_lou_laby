import tkinter as tk

"""classe de la page question: incluant des variables ou des fonctions qui permettent de definir un objet, ici les questions des differentes categories ."""

class PageQuest(tk.Frame):
    def __init__(self, parent, controller):
        """constructeur de la classe: fonction appelé à l'initialisation d'un objet de cette classe"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.question_text = tk.Label(self, text="coche la bonne reponse")
        self.question_text.pack()

        """création des 3 boutons pour répondre aux questions et la montrer sur la page"""
        self.bouton_rep1 = tk.Button(self, text="!")
        self.bouton_rep2 = tk.Button(self, text="!")
        self.bouton_rep3 = tk.Button(self, text="!")

        self.bouton_rep1.pack()
        self.bouton_rep2.pack()
        self.bouton_rep3.pack()

        button = tk.Button(self, text="retour",command=lambda: controller.show_frame("PageOne"))
        button.pack()

        """initialisation de toutes les questions de toutes les categories"""
        self.list_question = {}
        self.list_question["maths"] = {
            0: {
                "rep1": "8x^2+3x-8=68/-68",
                "rep2": "5x^2-4x+8=pas de solutions",
                "rep3": "2x^2-7x+9=0",
                "good": "rep3"
            },
            1: {
                "rep1": "e^3",
                "rep2": "e^2",
                "rep3": "e^4",
                "good": "rep2"
            },
            2: {
                "rep1": "e^x^2=1.462",
                "rep2": "e^x^3=1.359",
                "rep3": "e^x^4=1.496",
                "good": "rep1"
            },
            3: {
                "rep1": "le nombre pi n'est pas transcendant",
                "rep2": "stochastique= mesure et analyse harmonique",
                "rep3": "l'équation Navier-Stoke=comprendre les courants marins",
                "good": "rep3"
            },
            4: {
                "rep1": "17371 est un nombre palindrome",
                "rep2": "96568 est un nombre palindrome",
                "rep3": "un palindrome= nombre à 4 chiffres",
                "good": "rep1"
            }
        }

        self.list_question["histoire"] = {
            0: {
                "rep1": "1965= transfert des cendres de Jean Moulin",
                "rep2": "1957=traité de Rome",
                "rep3": "1959= 5eme republique",
                "good": "rep2"
            },
            1: {
                "rep1": "1920=R.Poincaré",
                "rep2": "1945=C.de Gaulle",
                "rep3": "1981=F.Mitterant",
                "good": "rep3"
            },
            3: {
                "rep1": "Née un 13 juillet",
                "rep2": "Amie avec F.Hollande",
                "rep3": "Déportée à Dachau",
                "good": "rep1"
            }
        }

        self.list_question["physique"] = {
            0: {
                "rep1": "nous ne sommes pas seuls dans l'espace",
                "rep2": "il y a une seule dimension dans l'univers",
                "rep3": "il y a des extraterestres sur mars",
                "good": "rep2"
            },
            1: {
                "rep1": "un atome d'azote possède 3 liaisons",
                "rep2": "un atome d'hydrogène possède 2 liaisons",
                "rep3": "un atome de crabone possède 4 liaisons",
                "good": "rep3"
            },
            2: {
                "rep1": "3.0x10^8 m/s",
                "rep2": "3.171002504x10^-16 a.l",
                "rep3": "300000000 m/s",
                "good": "rep1, rep2, rep3"
            },
        }

    """creation de la fonction qui controle le raffraichissement des questions d'une categorie"""
    def update(self):
        type = self.controller.question_type
        self.bouton_rep1.configure(text= self.list_question[type][self.controller.cpt[type]]["rep1"])
        self.bouton_rep2.configure(text= self.list_question[type][self.controller.cpt[type]]["rep2"])
        self.bouton_rep3.configure(text= self.list_question[type][self.controller.cpt[type]]["rep3"])
        self.controller.cpt[type] = (self.controller.cpt[type] + 1) % len(self.list_question[type])
        print(self.controller.cpt)
