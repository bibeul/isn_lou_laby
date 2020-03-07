import tkinter as tk
from tkinter import font  as tkfont
from pages import PageOne, PageTwo, StartPage, PageQuest, PageVictory, PageDefeat

list_question = {}

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        """constructeur de la classe: fonction appelé à l'initialisation d'un objet de cette classe"""
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.question_type = "maths"
        self.cpt = {"maths": 0, "physique": 0, "histoire": 0}

        """le container est l'endroit ou sont stockée toutes les pages, chaque page est ecrasée par une autre"""
        """ le container assigne nvl frame au container et le met en forme"""
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        """self = objet= instance d'une classe"""
        self.frames = {}
        """initialisation d'une boucle pour mettre toutes les pages au meme endroit"""
        for F in (StartPage, PageOne, PageTwo, PageQuest, PageVictory, PageDefeat):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """montrer la page pourlui donner un nom"""
        frame = self.frames[page_name]
        print(self.question_type)
        frame.update()
        frame.tkraise()


if __name__ == "__main__":
    """main loop pour commencer le programme"""
    app = SampleApp()
    app.mainloop()
