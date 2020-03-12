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
        self.bouton_rep1 = tk.Button(self, text="!", command=lambda: self.correcteur("rep1"))
        self.bouton_rep2 = tk.Button(self, text="!", command=lambda: self.correcteur("rep2"))
        self.bouton_rep3 = tk.Button(self, text="!", command=lambda: self.correcteur("rep3"))

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
                "rep1": "l'exponentielle est: e^3",
                "rep2": "l'exponentielle est: e^2",
                "rep3": "l'exponentielle est: e^4",
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
                "rep2": "stochastique est la mesure et analyse harmonique",
                "rep3": "l'équation Navier-Stoke est de comprendre les courants marins",
                "good": "rep3"
            },
            4: {
                "rep1": "17371 est un nombre palindrome",
                "rep2": "96568 est un nombre palindrome",
                "rep3": "un palindrome= nombre à 4 chiffres",
                "good": "rep1"
            },
            5: {
                "rep1": "3869-7985=-4116",
                "rep2": "3346-5456=-2111",
                "rep3": "72+364=446",
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
            2: {
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
            },
            4: {
               "rep1": "M. Block est un historien",
               "rep2": "Il est né en 1912",
               "rep3": "Il fait avancer les recherches sur l'Histoire médiévale",
               "good": "rep2"
            },
            5: {
               "rep1": "Napoléon a perdu contre les polonais en 1806",
               "rep2": "Napoléon a perdu contre les bulgares en 1806",
               "rep3": "Napoléon a perdu contre les prussiens en 1806",
               "good": "rep3"
            },
            6: {
               "rep1": "Le roi soleil était louis XIV",
               "rep2": "Le roi soleil était louis XV",
               "rep3": "Le roi soleil était louis XVI",
               "good": "rep1"
            },
            7: {
               "rep1": "Le liquide de mercure permet de grandir au Moyen Age",
               "rep2": "Le liquide de mercure rend immortel au Moyen Age",
               "rep3": "Le liquide de mercure est une arme au Moyen Age",
               "good": "rep2"
            },
            8: {
              "rep1": "La capitale du Mexique est l'Uruguay",
               "rep2": "La capitale du Mexique est Mexico DF",
               "rep3": "La capitale du Mexique est Mexico",
               "good": "rep2"
            },
            9: {
              "rep1": "La capitale du Kenya est Nairobie",
               "rep2": "La capitale du Kenya est Brazaville",
               "rep3": "La capitale du Kenya est Kinshasa",
               "good": "rep1"
            },
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
                "rep1": "la vitesse de la lumiere est: 4.0x10^8 m/s",
                "rep2": "la vitesse de la lumiere est: la vitesse de la lumiere est: 3.171002504x10^-16 a.l",
                "rep3": "la vitesse de la lumiere est: 300000001 m/s",
                "good": "rep2"
            },
            3: {
                "rep1": "la Terre trourne autour du soleil",
                "rep2": "le soleil est une planète",
                "rep3": "il y a 6 planetes dans notre systeme solaire",
                "good": "rep1"
            },
            4: {
                "rep1": "la liason C=O se trouve à 1900 - 2100 cm^-1",
                "rep2": "le groupe hydroxyde possède une double liaison ",
                "rep3": "l'IRM est une application de la RMN",
                "good": "rep3"
            },
            5: {
                "rep1": "l'energie la plus polluante est le gaz d'une vache",
                "rep2": "l'energie la plus polluante est l'uranium'",
                "rep3": "l'energie la plus polluante est la combustion de charbon",
                "good": "rep2"
            },
        }
    """creation de la fonction qui controle la correction d'une reponse"""

    def correcteur(self, number_button):
        typo = self.controller.question_type
        selected_question = self.list_question[typo][self.controller.cpt[typo]]
        goodrep = selected_question["good"]
        print("goodrep:", number_button == goodrep)
        self.controller.cpt[typo] = (self.controller.cpt[typo] + 1) % len(self.list_question[typo])
        if number_button == goodrep:
            self.controller.show_frame("PageVictory")
        else:
            self.controller.show_frame("PageDefeat")

    """creation de la fonction qui controle le raffraichissement des questions d'une categorie"""
    def update(self):
        type = self.controller.question_type
        print(type)
        self.bouton_rep1.configure(text= self.list_question[type][self.controller.cpt[type]]["rep1"])
        self.bouton_rep2.configure(text= self.list_question[type][self.controller.cpt[type]]["rep2"])
        self.bouton_rep3.configure(text= self.list_question[type][self.controller.cpt[type]]["rep3"])
        print(self.controller.cpt)
