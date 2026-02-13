import tkinter as tk


class ModelApp:
    CORRECT_CODE = "8085"

    def __init__(self):
        self.code = ""

    def add_symbol(self, symbol):
        if len(self.code) < len(self.CORRECT_CODE):
            self.code += symbol

    def remove_symbol(self):
        if len(self.code) > 0:
            self.code = self.code[:-1]

    def get_code(self):
        return self.code

    def check_code(self):
        return self.code == self.CORRECT_CODE


class ViewApp(tk.Frame):
    def __init__(self, master, callback, backspace, check_pin):
        super().__init__(master)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.label_color = "black"
        self.label = tk.Label(self, bg="light gray", fg=self.label_color, text="")
        self.label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        layout = [
            (1, 0, "7"),
            (1, 1, "8"),
            (1, 2, "9"),
            (1, 3, "A"),
            (2, 0, "4"),
            (2, 1, "5"),
            (2, 2, "6"),
            (2, 3, "B"),
            (3, 0, "1"),
            (3, 1, "2"),
            (3, 2, "3"),
            (3, 3, "C"),
            (4, 0, "*"),
            (4, 1, "0"),
            (4, 2, "#"),
            (4, 3, "D"),
        ]
        for row, col, symbol in layout:
            if symbol == "*":
                button = tk.Button(self, text=symbol, command=backspace)

            elif symbol == "#":
                button = tk.Button(self, text=symbol, command=check_pin)

            else:
                button = tk.Button(
                    self, text=symbol, command=lambda s=symbol: callback(s)
                )

            button.grid(row=row, column=col, sticky="nsew")

    def update_label(self, text, flag):
        fg = "green" if flag else "black"
        self.label.config(text=text, fg=fg)

    def update_label_color(self, color):
        self.label.config(fg=color)

    def update_label_text(self, text):
        self.label.config(text=text)


class ControllerApp:
    def __init__(self, root):
        self.model = ModelApp()
        self.view = ViewApp(root, self.press, self.backspace, self.check_pin)
        self.view.pack(fill="both", expand=True)

        self.update_view()

    def press(self, symbol):
        self.model.add_symbol(symbol)
        self.view.update_label_color("black")
        self.update_view()

    def backspace(self):
        self.model.remove_symbol()
        self.view.update_label_color("black")
        self.update_view()

    def check_pin(self):
        flag = self.model.check_code()
        if flag:
            self.view.update_label_color("green")
        else:
            self.view.update_label_color("red")
        self.update_view()

    def update_view(self):
        code = self.model.get_code()
        self.view.update_label_text(code)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x250")
    root.title("PIN")
    app = ControllerApp(root)
    root.mainloop()
