import tkinter as tk
from tkinter import filedialog


def save_file(self):
    ##
    # Save text to file
    ##

    filename = filedialog.asksaveasfilename(filetypes=[("Text file", "*.txt")], defaultextension="*.txt")

    if filename:
        with open(filename, "w", -1, "utf-8") as file:
            file.write(self.text.get(1.0, tk.END))


