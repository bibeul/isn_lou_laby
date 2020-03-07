import tkinter as tk


"""classe de la page 2: incluant des variables ou des fonctions qui permettent de definir un objet, ici tout ce qui 
compose la page 2. La page 2 correspond aux regles du jeu """

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        """constructeur de la classe: fonction appelé à l'initialisation d'un objet de cette classe"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Regles du jeu", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="retour", command=lambda: controller.show_frame("StartPage"))
        button.pack()

        """fonction pour definir les regles du jeu"""
        txtrdj = tk.Label(self, text=("un joueur se lance dans une course intellectuelle contre la montre. S’il lance une partie il devra choisir à chacune des cases qu'il traverse une catégorie de question, Mathématique, Physique et Histoire, 3 réponses possibles s'afficherons avec 1 question, à chaque fois 2 sont fausse et seule une réponse est bonne. Le joueur a un timer pour y répondre et s’il ne répond pas à temps, il a automatiquement faux. Plus le joueur répond juste aux questions, plus les questions seront dur et/ou le timer seras plus contraignant. A la fin du timer le jeux s'arrete et le joueur peut voire ses resultats (ou la distance qu'il a parcouru sur la rue.)"), wraplength=1000)
        txtrdj.pack(side="top", fill="x", pady=10)

