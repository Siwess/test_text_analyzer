import tkinter as tk
from tkinter import *
from libs import file_name


def msg_box_count_letters():
    ##
    # Show Window about letters in text.
    ##
    win = tk.Toplevel()
    win.geometry("400x200")
    win.title("Number of letters")

    file = open(file_name.name_file)
    data = file.read()
    rm_spaces = data.replace(" ", "")
    rm_dots = rm_spaces.replace(".", "")
    rm_q = rm_dots.replace("?", "")
    rm_em = rm_q.replace("!", "")
    rm_sc = rm_em.replace(";", "")
    rm_comm = rm_sc.replace(",", "")
    rm_c = rm_comm.replace(":", "")
    rm_a = rm_c.replace("'", "")
    rm_d = rm_a.replace("-", "")
    rm_an = len(rm_d.replace("$", ""))

    text = Label(win, text="Number of letters in text: ")
    text.pack()
    number_of_letters = Label(win, text=rm_an)
    number_of_letters.pack()
    # TODO: Change this nice code...

