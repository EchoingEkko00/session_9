#classeTkinter.py
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets() #on crée et rattache les widgets en même temps que l'application

    def creer_widgets(self):
        self.etiquette = tk.Label(self, text="J'aime Python !")
        self.bouton = tk.Button(self, text="Quitter", fg = "red", command=self.quit) # callback à quit()
        self.etiquette.pack()
        self.bouton.pack()


if __name__ == "__main__":
    app = Application()
    app.title("Ma Première Application Tkinter")
    app.mainloop()

