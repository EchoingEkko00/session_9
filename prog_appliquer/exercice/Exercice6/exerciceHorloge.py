import tkinter as tk
import time
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Une horloge")
        temps = time.strftime('%H:%M:%S')
        self.tempsCreation = tk.Label(self, text=temps)
        self.tempsCreation.pack(padx=100,pady=10)
        self.tempsCreation.after(1000, self.maj_heure())


    def maj_heure(self) :
        temps = time.strftime('%H:%M:%S')
        self.tempsCreation.config(text=temps)
        self.tempsCreation.after(1000, self.maj_heure)

if __name__ == "__main__":
    app = Application()
    app.mainloop()