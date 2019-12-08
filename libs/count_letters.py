from tkinter import messagebox as msg
from libs import file_name


def msg_box_count_letters():
    ##
    # Show MSG Box about letters in text.
    ##
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
    rm_d = len(rm_a.replace("-", ""))

    msg.showinfo("Letters in text", rm_d)
    # TODO: Change this nice code...

