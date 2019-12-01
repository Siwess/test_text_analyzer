import tkinter as tk
from tkinter import *
from libs.file_download import file_download
from libs.count_letters import count_letters
from libs.count_words import count_words
from libs.count_punctuation_marks import count_punctuation_marks
from libs.count_sentences import count_sentences
from msg_box import _msg_box


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
        file_menu.add_command(label="Download file", command=file_download)
        file_menu.add_command(label="Exit", command=self._quit)

        count_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Count", menu=count_menu)
        count_menu.add_command(label="Count letters", command=count_letters)
        count_menu.add_command(label="Count punctuation marks", command=count_punctuation_marks)
        count_menu.add_command(label="Count sentences", command=count_sentences)
        count_menu.add_command(label="Count words", command=count_words)

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=_msg_box)

        # TODO: Create GUI. Add menu.


app = Application()


