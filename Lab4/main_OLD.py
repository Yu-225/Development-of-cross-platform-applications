import tkinter as tk
import tkinter.ttk as ttk


class ModelApp:
    def __init__(self):
        self.state = {}

    def set_value(self, key, value):
        self.state[key] = value

    def get_value(self, key):
        return self.state.get(key, "")

    def get_state(self):
        return self.state.copy()


class Entry(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.config(text="Entry")
        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var)
        self.entry.pack(fill="x")

    def set_value(self, value):
        # self.entry.delete(0, tk.END)
        # self.entry.insert(0, value)
        self.var.set(value)

    def get_value(self):
        # return self.entry.get()
        return self.var.get()


class Spin(tk.LabelFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.config(text="Spinbox")
        self.var = tk.StringVar()
        tk.Spinbox(self, textvariable=self.var, values=values, state="readonly").pack(
            fill="x"
        )

    def set_value(self, value):
        self.var.set(value)

    def get_value(self):
        return self.var.get()


class Combo(tk.LabelFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.config(text="Combobox")
        self.var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.var, values=values, state="readonly").pack(
            fill="x"
        )

    def set_value(self, value):
        self.var.set(value)

    def get_value(self):
        return self.var.get()


class Radio(tk.LabelFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.config(text="Radiobutton")
        self.var = tk.StringVar()
        for val in values:
            tk.Radiobutton(self, variable=self.var, text=val, value=val).pack(
                anchor="w"
            )

    def set_value(self, value):
        self.var.set(value)

    def get_value(self):
        return self.var.get()


class Check(tk.LabelFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.config(text="Checkbutton")
        self.values = values
        self.vars = {val: tk.BooleanVar() for val in self.values}
        for val, var in self.vars.items():
            tk.Checkbutton(
                self, variable=var, onvalue=True, offvalue=False, text=val
            ).pack(anchor="w")

    def set_value(self, value):
        for val, var in self.vars.items():
            var.set(val in value)

    def get_value(self):
        return [val for val, var in self.vars.items() if var.get()]


class Scale(tk.LabelFrame):
    def __init__(self, master, from_, to, resolution):
        super().__init__(master)
        self.config(text="Scale")
        self.var = tk.IntVar()
        tk.Scale(
            self,
            variable=self.var,
            from_=from_,
            to=to,
            resolution=resolution,
            orient="horizontal",
        ).pack(fill="x")

    def set_value(self, value):
        self.var.set(value)

    def get_value(self):
        return self.var.get()


class Spin2(tk.LabelFrame):
    def __init__(self, master, from_, to, increment):
        super().__init__(master)
        self.config(text="Spin2")
        self.var = tk.IntVar()
        tk.Spinbox(
            self, textvariable=self.var, from_=from_, to=to, increment=increment
        ).pack(fill="x")

    def set_value(self, value):
        self.var.set(value)

    def get_value(self):
        return self.var.get()


class ViewApp(tk.Frame):
    def __init__(self, master, on_press):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.widgets = {
            "entry": Entry(self),
            "spin": Spin(self, ["First", "Second", "Third"]),
            "combo": Combo(self, ["First", "Second", "Third"]),
            "radio": Radio(self, ["First", "Second", "Third"]),
            "check": Check(self, ["First", "Second", "Third"]),
            "scale": Scale(self, 1, 3, 1),
            "spin2": Spin2(self, 1, 3, 1),
        }
        for widget in self.widgets.values():
            widget.pack(fill="x")
        tk.Button(self, text="PRESS", command=on_press).pack(fill="x")

        self.label = tk.Label(self, bg="white", justify="left")
        self.label.pack(fill="x")

    def config_label(self, text):
        self.label.config(text=text)


class ControllerApp:
    def __init__(self, root):
        init_values = {
            "entry": "First",
            "spin": "First",
            "combo": "First",
            "radio": "First",
            "check": ["First"],
            "scale": 1,
            "spin2": 1,
        }
        self.model = ModelApp()
        self.view = ViewApp(root, self.on_press)

        for key, widget in self.view.widgets.items():
            val = init_values[key]
            self.model.set_value(key, val)
            widget.set_value(val)

    def on_press(self):
        for key, widget in self.view.widgets.items():
            self.model.set_value(key, widget.get_value())
        self.update_view()

    def update_view(self):
        state = self.model.get_state()
        table = "".join([f"{key}: {val}\n" for key, val in state.items()])
        self.view.config_label(table)


if __name__ == "__main__":
    root = tk.Tk()
    app = ControllerApp(root)
    root.mainloop()
