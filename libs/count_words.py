from tkinter import messagebox as msg
from libs import file_name


def msg_box_count_words():
    ##
    # Count words in file
    ##
    file = open(file_name.name_file)
    data = file.read()
    numbers_of_words = len(data.split(" "))
    msg.showinfo("Words in text", numbers_of_words)

