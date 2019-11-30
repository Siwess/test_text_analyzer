import tkinter as tk
from tkinter import *
from file_download import file_download


class Application:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry("500x500")
        self.win.title("Text Analyzer")
        self.win.iconbitmap(default="icons/text_analyzer.ico")
        self.create_widgets()
        self.win.mainloop()

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def create_widgets(self):
        menu_bar = Menu()
        self.win.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Download File", command=file_download)
        file_menu.add_command(label="Exit", command=self._quit)

        # TODO: Create GUI. Add menu.


app = Application()


