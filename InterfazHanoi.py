import tkinter as tk

class InterfazHanoi(tk.Frame):
    def __init__(self, parent):
        super(InterfazHanoi, self).__init__(parent)
        canvas = tk.Canvas(width=400, height=400, bg="blue")
        canvas.create_rectangle(150,150,250 ,250)
        canvas.pack()


root = tk.Tk()
ventana = InterfazHanoi(root)
ventana.pack(expand=True)

root.mainloop()