from tkinter import messagebox as msg


def msg_box_count_letters():
    ##
    # Show MSG Box about letters in text.
    ##
    file = open('result.txt')
    data = file.read()
    numbers_of_characters = len(data)
    msg.showinfo("Letters in text", numbers_of_characters)
    # TODO: Change...

