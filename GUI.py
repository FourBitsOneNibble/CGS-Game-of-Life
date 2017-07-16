import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")
        self._update()

    def _update(self):
        print('update')
        self.canvas.create_rectangle(0,0,self.canvas.winfo_width(),self.canvas.winfo_height(), fill = 'white')
        self.canvas.create_line(0,0,self.canvas.winfo_width(),self.canvas.winfo_height())
        self.after(1000, self._update)

root = tk.Tk()
gui = GUI(master = root)
gui.mainloop()
