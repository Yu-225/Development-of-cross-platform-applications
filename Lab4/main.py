import tkinter as tk
import tkinter.ttk as ttk

from components import *


class ModelApp:
    def __init__(self):
        self.state = {}

    def set_value(self, key, value):
        self.state[key] = value

    def get_value(self, key):
        return self.state.get(key, "")

    def get_state(self):
        return self.state.copy()


class ViewApp(tk.Frame):
    def __init__(self, master, on_change):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # # Запитання 1
        # self.frame1 = tk.Frame(self, width=400, height=100, padx=3, pady=3)
        # self.frame1.pack(padx=3, pady=3)
        # self.q1 = tk.Label(self.frame1, text="Операційна система:").pack(side="left")
        # Combo(self.frame1, "combo", ["Android", "iOS"]).pack(side="left")

        # # Запитання 2
        # self.frame2 = tk.Frame(self, width=400, height=100, padx=3, pady=3)
        # self.frame2.pack(padx=3, pady=3)
        # self.q2 = tk.Label(self.frame2, text="Операційна система:").pack(side="left")
        # Radio(self.frame2, "radio", ["Навчання", "Розваги", "Робота"]).pack(side="left")

        # # Запитання 3
        # self.frame3 = tk.Frame(self, width=400, height=100, padx=3, pady=3)
        # self.frame3.pack(padx=3, pady=3)
        # self.q3 = tk.Label(self.frame3, text="Операційна система:").pack(side="left")
        # Check(self.frame3, "check", ["Соцмережі", "Банкінг", "Ігри"]).pack(side="left")

        # # Запитання 4
        # self.frame4 = tk.Frame(self, width=400, height=100, padx=3, pady=3)
        # self.frame4.pack(padx=3, pady=3)
        # self.q4 = tk.Label(self.frame4, text="Операційна система:").pack(side="left")
        # Spin(self.frame4, "spin", [ str(h) for h in range(25) ]).pack(side="left")

        # # Запитання 5
        # self.frame5 = tk.Frame(self, width=400, height=100, padx=3, pady=3)
        # self.frame5.pack(padx=3, pady=3)
        # self.q5 = tk.Label(self.frame5, text="Операційна система:").pack(side="left")
        # Scale(self.frame5, "scale", 1, 10, 1).pack(side="left")

        self.widgets = {}

        self.wgts = {
            "combo": {
                "text": "Операційна система",
                "class": Combo,
                "args": ["combo", ["Android", "iOS"]],
            },
            "radio": {
                "text": "Основна мета",
                "class": Radio,
                "args": ["radio", ["Навчання", "Розваги", "Робота"]],
            },
            "check": {
                "text": "Типи застосунків",
                "class": Check,
                "args": ["check", ["Соцмережі", "Банкінг", "Ігри"]],
            },
            "spin": {
                "text": "Годин на день",
                "class": Spin,
                "args": ["spin", [str(h) for h in range(25)]],
            },
            "scale": {
                "text": "Рівень цифрового мінімалізму",
                "class": Scale,
                "args": ["scale", 1, 10, 1],
            },
        }

        for key, data in self.wgts.items():

            frame = tk.Frame(self, bg="#eeeeee", padx=10, pady=8, relief="groove", bd=1)
            frame.pack(fill="x", padx=10, pady=4)

            tk.Label(frame, text=data["text"]).pack(side="left")

            widget = data["class"](frame, *data["args"])
            widget.pack(side="left", padx=5)

            widget.bind_command(on_change)

            self.widgets[key] = widget

        self.reset_btn = tk.Button(self, text="Очистити")
        self.reset_btn.pack(pady=5)

        self.label = tk.Label(self, bg="white", justify="left")
        self.label.pack(fill="x", padx=10, pady=10)

    def config_label(self, text):
        self.label.config(text=text)

    def config_root(self):
        self.master.title("Використання мобільних застосунків -- Variant 8")
        # self.master.maxsize(1300, 400)
        self.master.minsize(420, 600)

        w = 420
        h = 600
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        dw = (sw - w) // 2
        dh = (sh - h) // 2

        self.master.geometry(f"{w}x{h}+{dw}+{dh}")


class ControllerApp:
    def __init__(self, root):
        self.model = ModelApp()
        self.view = ViewApp(root, self.on_change)
        self.view.config_root()

        self.init_values = {
            "combo": "Android",
            "radio": "Навчання",
            "check": ["Соцмережі"],
            "spin": "1",
            "scale": 5,
        }

        self.init_state()

        self.view.reset_btn.config(command=self.reset)

    def init_state(self):
        for key, value in self.init_values.items():
            self.model.set_value(key, value)
            widget = self.view.widgets[key]
            widget.set_value(value)
            self.update_view()

    def reset(self):
        self.init_state()

    def on_change(self, key, value):
        self.model.set_value(key, value)
        self.update_view()

    def update_view(self):
        state = self.model.get_state()
        table = "".join([f"{key}: {val}\n" for key, val in state.items()])
        self.view.config_label(table)


if __name__ == "__main__":
    root = tk.Tk()
    app = ControllerApp(root)
    root.mainloop()
