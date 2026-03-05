import tkinter as tk

from controler import ControllerApp

    
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    app = ControllerApp(root)
    root.mainloop()