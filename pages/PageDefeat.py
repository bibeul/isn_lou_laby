import tkinter as tk


class PageDefeat(tk.Frame):
    """constructeur de la classe: fonction appelé à l'initialisation d'un objet de cette classe"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="POOOOOOOOOO T'ES TROP NUL!!!!!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        """initialisation du bouton retour"""

        button_back = tk.Button(self, text="retour", command=lambda: controller.show_frame("PageOne"))
        button_back.pack()
