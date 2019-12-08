import tkinter as tk
from tkinter import *
from libs import file_name


def count_words():
    ##
    # Count words in file
    ##
    win = tk.Toplevel()
    win.geometry("400x200")
    win.title("Number of words")

    file = open(file_name.name_file)
    data = file.read()
    rm_spaces = data.replace(".", " ")
    words = len(rm_spaces.split(" "))
    text = Label(win, text="Number of words in text: ")
    text.pack()
    number_of_words = Label(win, text=words)
    number_of_words.pack()

