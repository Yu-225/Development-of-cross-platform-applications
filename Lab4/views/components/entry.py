import tkinter as tk


class Entry(tk.Frame):
    def __init__(self, master, name, callback):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.name = name
        self.callback = callback

        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="we")
        button = tk.Button(self, text="Зберегти", command=self.on_click)
        button.grid(row=0, column=1)
    
    def on_click(self):
        self.callback(self.name, self.get_value())
    
    def set_value(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)
    
    def get_value(self):
        return self.entry.get()