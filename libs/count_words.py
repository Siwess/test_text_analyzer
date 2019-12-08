from tkinter import messagebox as msg
from libs import file_name


def msg_box_count_words():
    ##
    # Count words in file
    ##
    file = open(file_name.name_file)
    data = file.read()
    rm_spaces = data.replace(".", " ")
    numbers_of_words = len(rm_spaces.split(" "))
    msg.showinfo("Words in text", numbers_of_words)

