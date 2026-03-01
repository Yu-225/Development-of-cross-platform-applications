from dataclasses import dataclass
import tkinter as tk


@dataclass
class LightTheme:
    # Text
    text: str = "Operation Failed"
    font: tuple = ("Segoe UI", 14)
    anchor: str = "center"
    justify: str = "center"

    # Size
    width: int = 30
    height: int = 3
    padx: int = 10
    pady: int = 10

    # Colors
    fg: str = "black"
    bg: str = "white"

    # Border
    bd: int = 2
    relief: str = "ridge"

    # Highlight
    highlightthickness: int = 2
    highlightbackground: str = "gray"
    highlightcolor: str = "blue"

    def as_dict(self):
        return self.__dict__


@dataclass
class DarkTheme:
    # Text
    text: str = "Operation Failed"
    font: tuple = ("Helvetica", 14)
    anchor: str = "center"
    justify: str = "center"

    # Size
    width: int = 30
    height: int = 3
    padx: int = 10
    pady: int = 10

    # Colors
    fg: str = "white"
    bg: str = "#2b2b2b"

    # Border
    bd: int = 2
    relief: str = "ridge"

    # Highlight
    highlightthickness: int = 2
    highlightbackground: str = "#3a7afe"
    highlightcolor: str = "#3a7afe"

    def as_dict(self):
        return self.__dict__


class ViewApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        avaliable = {
            # Size
            "height": [1, 2, 3],
            "width": [10, 20, 30],
            # Text
            "text": ["hello word", "hello\nword"],
            "anchor": ["n", "e", "s", "w", "center"],
            "justify": ["left", "center", "right"],
            "wraplength": [40, 80],
            "padx": [0, 5, 10],
            "pady": [0, 5, 10],
            # Image
            # Поки нема картинок )
            # Cursor
            "cursor": ["arrow", "hand2", "cross", "watch"],
            # Color
            "fg": ["black", "navy"],
            "bg": ["white", "azure"],
            "activeforeground": ["blue"],
            "activebackground": ["light blue"],
            # Border
            "bd": [0, 2, 5],
            "relief": ["flat", "raised", "sunken", "ridge", "groove", "solid"],
            # State
            "state": ["normal", "disabled"],
            # Highlight
            "highlightbackground": ["grey"],
            "highlightcolor": ["blue"],
            "highlightthickness": [0, 2, 5],
        }

        frame_wid = tk.LabelFrame(self, text="Widget")
        frame_wid.pack(fill="x")

        frame_set = tk.LabelFrame(self, text="Settings")
        frame_set.pack(fill="x")

        # -----
        self.widget = tk.Label(frame_wid, text="Operation Failed")
        # self.widget = tk.Button(frame_wid)
        # self.widget = tk.Entry(frame_wid)
        self.widget.pack()
        # -----

        for par, args in avaliable.items():
            frame = tk.LabelFrame(frame_set, text=par)
            frame.pack(side="left", anchor="nw", fill="y")
            for arg in args:
                tk.Button(
                    frame,
                    text=str(arg),
                    command=lambda p=par, a=arg: self.press_button(p, a),
                ).pack(fill="x", anchor="nw")

        # Change Theme
        self.on_light = None
        self.on_dark = None

        theme_frame = tk.LabelFrame(self, text="Theme")
        theme_frame.pack(side="left", fill="x")

        tk.Button(theme_frame, text="Light", command=self._light).pack(side="left")
        tk.Button(theme_frame, text="Dark", command=self._dark).pack(side="left")

        # Reset
        tk.Button(self, text="Reset", command=self.set_default).pack(fill="x")
        self.get_default()

    def _light(self):
        if self.on_light:
            self.on_light()

    def _dark(self):
        if self.on_dark:
            self.on_dark()

    def apply_style(self, style: dict):
        self.widget.config(**style)

    def press_button(self, par, arg):
        if par in self.widget.keys():
            self.widget.config(**{par: arg})
        else:
            print(f"{par}={arg} is ignored")

    def get_default(self):
        pars = self.widget.keys()
        self.default = {par: self.widget.cget(par) for par in pars}

    def set_default(self):
        self.widget.config(**self.default)

    def config_root(self):
        self.master.title("Style and Geometry -- Variant 8")
        self.master.maxsize(1300, 400)
        self.master.minsize(800, 200)

        w = 1000
        h = 400
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        dw = (sw - w) // 2
        dh = (sh - h) // 2

        # print(sw, sh)
        self.master.geometry(f"{w}x{h}+{dw}+{dh}")


class ControllerApp:
    def __init__(self, root):
        # self.model = model
        self.view = ViewApp(root)
        self.view.pack(fill="both")
        self.view.config_root()

        self.LIGHT_THEME = LightTheme()
        self.DARK_THEME = DarkTheme()
        self.view.on_light = lambda: self.apply_theme(self.LIGHT_THEME)
        self.view.on_dark = lambda: self.apply_theme(self.DARK_THEME)

    def apply_theme(self, theme):
        self.view.apply_style(theme.as_dict())


if __name__ == "__main__":
    root = tk.Tk()
    # root.title("...")
    # root.geometry("1000x400")
    app = ControllerApp(root)
    root.mainloop()
