from tkinter import messagebox as msg
from libs import file_name


def msg_box_count_sentences():
    ##
    # Count sentences in file
    ##
    file = open(file_name.name_file)
    data = file.read()
    numbers_of_sentences = len(data.split("."))
    msg.showinfo("Sentences in text", numbers_of_sentences)

