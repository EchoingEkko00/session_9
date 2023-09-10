#dessinTkinter.py
import tkinter as tk

racine = tk.Tk()
canv = tk.Canvas(racine, bg="white", height=200, width=200) #Canvas ( master, option=value, ... )
canv.pack()
canv.create_oval(10, 10, 190, 190, outline="red", width=4) #canvas.create_oval(x0, y0, x1, y1, options)
canv.create_line(0, 0, 200, 200, fill="black", width=10) #canvas.create_line(x0, y0, x1, y1, ..., xn, yn, options)
canv.create_line(0, 200, 200, 0, fill="black", width=10)
racine.mainloop()