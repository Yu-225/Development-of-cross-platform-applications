import tkinter as tk

from views.components.entry import Entry
from views.components.entry2 import Entry2
from views.components.spin import Spin
from views.components.combo import Combo
from views.components.radio import Radio


class ViewApp(tk.Frame):
    def __init__(self, master, callback, options):
        super().__init__(master)
        self.callback = callback

        self.fields = {}

        # Час засинання
        tk.Label(self, text="Коли лягли спати? (HH:MM)").pack(fill="x")
        self.fields["bed_time"] = Entry2(self, "bed_time", callback)
        self.fields["bed_time"].pack(fill="x")

        # Час пробудження
        tk.Label(self, text="Коли прокинулись? (HH:MM)").pack(fill="x")
        self.fields["wake_time"] = Entry2(self, "wake_time", callback)
        self.fields["wake_time"].pack(fill="x")

        # Чи були пробудження
        tk.Label(self, text="Чи були пробудження вночі?").pack(fill="x")
        self.fields["had_awakenings"] = Radio(
            self,
            "had_awakenings",
            callback,
            ["Ні", "Так"]
        )
        self.fields["had_awakenings"].pack(fill="x")
        self.fields["had_awakenings"].set_value("Ні")

        # Тривалість пробуджень
        self.awake_frame = tk.Frame(self)
        tk.Label(self.awake_frame, text="Скільки хвилин сумарно?").pack(fill="x")
        self.fields["awake_minutes"] = Spin(
            self.awake_frame,
            "awake_minutes",
            callback,
            list(range(0, 301))
        )
        self.fields["awake_minutes"].pack(fill="x")

        # Спочатку приховано
        self.awake_frame.pack_forget()

        # Якість сну
        tk.Label(self, text="Оцініть якість сну (1-5)").pack(fill="x")
        self.fields["quality"] = Spin(
            self,
            "quality",
            callback,
            [1, 2, 3, 4, 5]
        )
        self.fields["quality"].pack(fill="x")
        
        
        # обчислити
        tk.Button(self, text="Обчислити", command=self.calc_result).pack(fill="x")


        # Результат
        self.label = tk.Label(self, text="", bg="white")
        self.label.pack(fill="both", expand=True)
    
    
    def calc_result(self):
        self.callback('', '')
    

    # Показує додаткове питання
    def toggle_awake_field(self, value):
        if value == "Так":
            self.awake_frame.pack(fill="x")
        else:
            self.awake_frame.pack_forget()

    # Оноалення мітки
    def update_label(self, text):
        self.label.config(text=text)
        
        
if __name__ == "__main__":
    def mock_callback(name, value):
        print(f"{name} changed to {value}")

    root = tk.Tk()
    root.geometry("400x550")
    root.title("View Test")

    options = ["Option 1", "Option 2", "Option 3"]

    app = ViewApp(root, mock_callback, options)
    app.pack(fill="both", expand=True)

    root.mainloop()