import tkinter as tk
from tkinter import *
from libs.file_download import file_download
from libs.count_letters import msg_box_count_letters
from libs.count_words import count_words
from libs.count_punctuation_marks import count_punctuation_marks
from libs.count_sentences import count_sentences
from tkinter import filedialog as fd
from msg_box import _msg_box


class Application:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry("500x500")
        self.win.title("Text Analyzer")
        self.win.iconbitmap(default="icons/text_analyzer.ico")
        self.create_widgets()
        self.text = tk.Text(self.win)
        self.scrollbar_text = tk.Scrollbar(self.win)
        self.scrollbar_text.place(in_=self.text, relx=1., rely=0, relheight=1.)
        self.scrollbar_text.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar_text.set)
        self.text.place(x=0, y=0, relwidth=1, relheight=1, width=- 18)
        self.auto_open_file()
        self.win.mainloop()

    def _quit(self):
        ##
        # Exit GUI cleanly
        ##
        self.win.quit()
        self.win.destroy()
        exit()

    def create_widgets(self):
        ##
        # Create widgets like menu, text box, etc.
        ##
        menu_bar = Menu()
        self.win.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Download hardcoded file", command=file_download)
        file_menu.add_command(label="Open file...", command=self.open_file)
        file_menu.add_command(label="Save file...", command=self.save_file)
        file_menu.add_command(label="Save statistics...", command=self.save_statistics)
        file_menu.add_command(label="Exit", command=self._quit)

        count_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Count", menu=count_menu)
        count_menu.add_command(label="Count letters", command=msg_box_count_letters)
        count_menu.add_command(label="Count punctuation marks", command=count_punctuation_marks)
        count_menu.add_command(label="Count sentences", command=count_sentences)
        count_menu.add_command(label="Count words", command=count_words)

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=_msg_box)

        # TODO: Create GUI. Add menu.

    def open_file(self):
        ##
        # Open text file
        ##
        filename = fd.askopenfilename(filetypes=[("Text file", "*.txt")])

        if filename:
            with open(filename, "r", -1, "utf-8") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())

    def auto_open_file(self):
        ##
        # Open hardcoded text file
        ##
        file = open('result.txt', encoding="utf8")
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, file.read())

    def save_file(self):
        ##
        # Save text to file
        ##
        filename = fd.asksaveasfilename(filetypes=[("Text file", "*.txt")], defaultextension="*.txt")

        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(self.text.get(1.0, tk.END))

    def save_statistics(self):
        # TODO: Implement save statistics to file...
        ##
        # Save statistics to file
        #
        filename = fd.asksaveasfilename(filetypes=[("Text file", "*.txt")], defaultextension="*.txt")

        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(self.text.get(1.0, tk.END))


app = Application()


