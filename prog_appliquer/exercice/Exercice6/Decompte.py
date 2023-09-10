import sys
import tkinter as tk
import time
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Un comte a rebours")
        self.creerWidget()


    def creerWidget(self):
        if int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 300:
            self.temps = sys.argv[1]
            self.temps = int(self.temps)*60
            self.tempsFormat = time.strftime('%H:%M:%S', time.gmtime(self.temps))
            self.tempsCreation = tk.Label(self, text=self.tempsFormat)
            self.tempsCreation.pack(padx=100, pady=10)
            self.quitter = tk.Button(self, text="Quitter", command=self.quit)
            self.quitter.pack(side=tk.TOP)
            self.lancer = tk.Button(self, text="Lancer", command=self.lancerDecompte)
            self.lancer.pack(side=tk.BOTTOM)
        else:
            print("Le temps doit être compris entre 1 et 300 minutes")
            self.destroy()

    def lancerDecompte(self):
        self.temps -= 1
        self.tempsFormat = time.strftime('%H:%M:%S', time.gmtime(self.temps))
        self.tempsCreation.config(text=self.tempsFormat)
        self.tempsCreation.after(1000, self.lancerDecompte)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
    print("C'est terminé !")