import tkinter as tk


class ModelApp:
    def __init__(self):
        self.style = {
            "text": "Код писався вночі, тому виглядає дивно... довно що він взагалі запускається..."
        }

    def update_style(self, item):
        self.style.update(item)

    def get_style(self):
        return self.style.copy()


class ViewApp(tk.Frame):
    def __init__(self, master, callback):
        super().__init__(master)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.frame_button = tk.Frame(self)
        self.frame_button.grid(row=0, column=0, columnspan=1, sticky="nsew")

        self.frame_label = tk.Frame(self)
        self.frame_label.grid(row=0, column=1, columnspan=1, sticky="nsew")

        # не робит :(
        self.scrollbar = tk.Scrollbar(self.frame_button, orient=tk.VERTICAL)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.frame_button)

        options = [
            ("fg", "dark blue"),
            ("fg", "dark green"),
            ("bg", "light blue"),
            ("bg", "light green"),
            ("activebackground", "blue"),
            ("activebackground", "green"),
            ("anchor", "n"),
            ("anchor", "s"),
            ("anchor", "w"),
            ("anchor", "e"),
            ("anchor", "center"),
            ("padx", 0),
            ("padx", 10),
            ("pady", 0),
            ("pady", 10),
            ("bd", 0),
            ("bd", 3),
            ("bd", 5),
            ("bd", 10),
            ("relief", "flat"),
            ("relief", "raised"),
            ("relief", "sunken"),
            ("relief", "ridge"),
            ("relief", "groove"),
            ("relief", "solid"),
            ("width", 20),
            ("width", 50),
            ("justify", "left"),
            ("justify", "center"),
            ("justify", "right"),
            ("wraplength", 0),
            ("wraplength", 100),
            ("wraplength", 300),
            ("highlightbackground", "black"),
            ("highlightbackground", "red"),
            ("highlightbackground", "green"),
            ("highlightbackground", "blue"),
            ("highlightcolor", "black"),
            ("highlightcolor", "red"),
            ("highlightcolor", "green"),
            ("highlightcolor", "blue"),
            ("highlightthickness", 0),
            ("highlightthickness", 5),
            ("highlightthickness", 10),
        ]

        parameters = list(dict.fromkeys(p for p, _ in options))
        frames = {}

        for p in parameters:
            frames[p] = tk.LabelFrame(self.frame_button, text=p)
            frames[p].pack(anchor="w")

        for p, t in options:
            tk.Button(
                frames[p], text=t, cursor="hand2", command=lambda s={p: t}: callback(s)
            ).pack(side="left")

        self.label = tk.Label(self.frame_label, cursor="xterm", text="", takefocus=True)
        self.label.pack(fill="both", expand=True)

        self.label.bind("<FocusIn>", lambda e: print("IN"))
        self.label.bind("<FocusOut>", lambda e: print("OUT"))

    def update_label(self, item):
        self.label.config(**item)
        pass


class ControllerApp:
    def __init__(self, root):
        self.model = ModelApp()
        self.view = ViewApp(root, self.press)
        self.view.pack(fill="both", expand=True)
        self.update_view()

    def press(self, item):
        self.model.update_style(item)
        self.update_view()

    def update_view(self):
        style = self.model.get_style()
        self.view.update_label(style)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Label styling demo")
    root.geometry("800x400")
    root.maxsize(800, 700)
    root.minsize(400, 300)

    app = ControllerApp(root)
    root.mainloop()
