import tkinter as tk
from tkinter import *
from libs import file_name


def count_punctuation_marks():
    ##
    # Count punctuation marks in file
    ##
    win = tk.Toplevel()
    win.geometry("400x200")
    win.title("Number of punctuation marks")

    file = open(file_name.name_file)
    data = file.read()
    count = 0
    for i in range(0, len(data)):
        if data[i] in ("!", ",", "'", ";", '"', ".", "-", "?"):
            count = count + 1

    punctuation_marks = count
    text = Label(win, text="Number of punctuation marks in text: ")
    text.pack()
    number_of_punctuation_marks = Label(win, text=punctuation_marks)
    number_of_punctuation_marks.pack()

