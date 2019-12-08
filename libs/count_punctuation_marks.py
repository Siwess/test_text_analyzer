from tkinter import messagebox as msg
from libs import file_name


def msg_box_count_punctuation_marks():
    ##
    # Count punctuation marks in file
    ##
    file = open(file_name.name_file)
    data = file.read()
    count = 0
    for i in range(0, len(data)):
        if data[i] in ("!", ",", "'", ";", '"', ".", "-", "?"):
            count = count + 1

    numbers_of_punctuation_marks = count
    msg.showinfo("Punctuation marks in text: ", numbers_of_punctuation_marks)
