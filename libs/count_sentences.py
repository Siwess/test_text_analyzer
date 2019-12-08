import tkinter as tk
from tkinter import *
from libs import file_name


def count_sentences():
    ##
    # Count sentences in file
    ##
    win = tk.Toplevel()
    win.geometry("400x200")
    win.title("Number of sentences")

    file = open(file_name.name_file)
    data = file.read()
    sentences = len(data.split("."))
    text = Label(win, text="Number of sentences in text: ")
    text.pack()
    number_of_sentences = Label(win, text=sentences)
    number_of_sentences.pack()


