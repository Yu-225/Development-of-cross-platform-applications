import tkinter as tk



# Модель - Бекенд - Логіка, взаємодія з БД
class ModelApp:
    def __init__(self):
        self.times = ["Секунда", "Хвилина", "Година", "День", "Тиждень", "Місяць", "Рік"]
        self.base_value = 2
        self.counter = self.base_value
    
    
    def counter_up(self):
        self.counter += 1
        if self.counter >= len(self.times):
            self.counter = len(self.times) - 1
    
    def counter_down(self):
        self.counter -= 1
        if self.counter <= 0:
            self.counter = 0
            
    def counter_reset(self):
        self.counter = self.base_value
            
    def get_value(self):
        return self.times[self.counter]
    
    def get_index(self):
        return self.counter




# Вигляд - Фронтенд
class ViewApp(tk.Frame):
    def __init__(self, master, on_click_up, on_click_down, on_click_reset):
        super().__init__(master)
        
        # Віджет для відображення даних.
        self.label = tk.Label(self, text="")
        self.label.pack(pady=10)

        # Кнопочки
        button_up = tk.Button(self, text="Up", command=on_click_up)
        button_up.pack(pady=10)
        
        button_down = tk.Button(self, text="Down", command=on_click_down)
        button_down.pack(pady=10)
        
        button_reset = tk.Button(self, text="Reset", command=on_click_reset)
        button_reset.pack(pady=10)
    
    def update_label(self, text):
        # Оновлення відображення.
        # View не змінює стан і не звертається до Model.
        self.label.config(text=text)



# Контролер - приймає ввід користувача, взаємодіє з моделью та виглядом
class ControllerApp:
    def __init__(self, root):
        # Controller створює Model і View
        # та керує їх взаємодією.
        self.model = ModelApp()
        self.view = ViewApp(root, self.on_click_up, self.on_click_down, self.on_click_reset)
        self.view.pack()
        
        # Початкове відображення стану.
        self.update_view()

    def on_click_up(self):
        self.model.counter_up()
        self.update_view()
        
    def on_click_down(self):
        self.model.counter_down()
        self.update_view()
        
    def on_click_reset(self):
        self.model.counter_reset()
        self.update_view()

    def update_view(self):
        # Синхронізація View зі станом Model.
        value = self.model.get_value()
        index = self.model.get_index()
        
        text = f'Елемент: {value}\nІндекс: {index}'
        self.view.update_label(text)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('250x250')
    root.title('Counter')
    app = ControllerApp(root)
    root.mainloop()