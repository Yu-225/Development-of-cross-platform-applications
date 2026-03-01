import tkinter as tk


class Radio(tk.LabelFrame):
    def __init__(self, master, name, callback, options):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.config(text="Radio Button")
        self.var = tk.StringVar()
        self.name = name
        self.callback = callback
        
        for i, option in enumerate(options):
            radio = tk.Radiobutton(self, variable=self.var, text=option, value=option, command=self.on_change)
            radio.grid(row=i, column=0, sticky="nw")
        
        button = tk.Button(self, text="Зберегти", command=self.on_change)
        button.grid(row=0, column=1)
    
    def on_change(self):
        self.callback(self.name, self.var.get())
    
    def set_value(self, value):
        self.var.set(value)
    
    def get_value(self):
        return self.var.get()