import tkinter as tk

"""classe de la startpage : incluant des variables ou des fonctions qui permettent de definir un objet, ici tout ce 
qui compose la start page c'est a dire le menu principale ou l'on decide de jouer ou consulter les regles du jeu 
cette page est reliée a la page 1 et 2. """

class StartPage(tk.Frame):
    """constructeur de la classe: fonction appelé à l'initialisation d'un objet de cette classe"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Menu que desirez vous faire", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        """initialisation des boutons pour lancer le jeu et les regles du jeu puis affichage des boutons"""
        button1 = tk.Button(self, text="Lancer le jeu", command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Règles du jeu", command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

"""    
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=(controller.title_font, 30),bg='#FF775A',foreground='white')
        label.pack(side="top", fill="x", pady=10, expand=YES)
        cadre = Frame(self)
        cadre.pack(expand=NO)
        button1 = tk.Button(cadre, text="Lancer le jeu",font=('Arrial',20),bg='#FF775A', command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Règles du jeu",font=('Arrial',10),bg='#FF775A', command=lambda: controller.show_frame("PageTwo"))
        button1.config( height = 3, width = 10,relief=FLAT)
        button2.config( height = 1, width = 10,relief=FLAT)
        button1.pack(pady=10)
        button2.pack(pady=60)
"""