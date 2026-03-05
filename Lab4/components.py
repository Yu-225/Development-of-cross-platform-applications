import tkinter as tk
import tkinter.ttk as ttk


class BaseComponent(tk.LabelFrame):
    def __init__(self, master, key, var_type=tk.StringVar):
        super().__init__(master)
        self.key = key
        self.var = var_type()
        self._command = None

        self.var.trace_add("write", self._on_change)

    def set_value(self, value):
        self.var.set(value)

    def get_value(self):
        return self.var.get()

    def bind_command(self, command):
        self._command = command

    def _on_change(self, *args):
        if self._command:
            self._command(self.key, self.get_value())


class Spin(BaseComponent):
    def __init__(self, master, key, values):
        super().__init__(master, key)
        self.config(text="Spinbox")

        tk.Spinbox(self, textvariable=self.var, values=values, state="readonly").pack(
            fill="x"
        )


class Combo(BaseComponent):
    def __init__(self, master, key, values):
        super().__init__(master, key)
        self.config(text="Combobox")

        combo = ttk.Combobox(
            self, textvariable=self.var, values=values, state="readonly"
        )
        combo.pack(fill="x")


class Radio(BaseComponent):
    def __init__(self, master, key, values):
        super().__init__(master, key)
        self.config(text="Radiobutton")

        for val in values:
            tk.Radiobutton(self, variable=self.var, text=val, value=val).pack(
                anchor="w"
            )


class Check(BaseComponent):
    def __init__(self, master, key, values):
        super().__init__(master, key)

        self.config(text="Checkbutton")
        self.vars = {val: tk.BooleanVar() for val in values}

        for val, var in self.vars.items():
            var.trace_add("write", self._on_change)

            tk.Checkbutton(self, variable=var, text=val).pack(anchor="w")

    def get_value(self):
        return [val for val, var in self.vars.items() if var.get()]

    def set_value(self, values):
        for val, var in self.vars.items():
            var.set(val in values)


class Scale(BaseComponent):
    def __init__(self, master, key, from_, to, resolution):
        super().__init__(master, key)
        self.var = tk.IntVar()
        self.var.trace_add("write", self._on_change)

        self.config(text="Scale")

        tk.Scale(
            self,
            variable=self.var,
            from_=from_,
            to=to,
            resolution=resolution,
            orient="horizontal",
        ).pack(fill="x")


class Spin2(BaseComponent):
    def __init__(self, master, key, from_, to, increment):
        super().__init__(master, key)

        # Перевизначаємо тип змінної
        self.var = tk.IntVar()
        self.var.trace_add("write", self._on_change)

        self.config(text="Spin2")

        tk.Spinbox(
            self,
            textvariable=self.var,
            from_=from_,
            to=to,
            increment=increment,
            state="readonly",
        ).pack(fill="x")
