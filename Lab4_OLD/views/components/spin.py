import tkinter as tk


class Spin(tk.Frame):
    def __init__(self, master, name, callback, options):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.var = tk.StringVar()
        self.name = name
        self.callback = callback

        entry2 = tk.Spinbox(self, textvariable=self.var, values=options)
        entry2.grid(row=0, column=0, sticky="we")
        button = tk.Button(self, text="Зберегти", command=self.on_click)
        button.grid(row=0, column=1)
    
    def on_click(self):
        self.callback(self.name, self.get_value())
    
    def set_value(self, value):
        self.var.set(value)
    
    def get_value(self):
        return self.var.get()