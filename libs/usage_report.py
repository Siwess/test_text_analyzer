import tkinter as tk
from tkinter import *
from collections import Counter
from libs import file_name
from tkinter import messagebox as msg


def plot_usage_statistics():
    try:

        file = open(file_name.name_file, encoding="utf8")
        data = file.read()

        win = tk.Toplevel()
        text = tk.Text(win)
        scrollbar_text = tk.Scrollbar(win)
        scrollbar_text.place(in_=text, relx=1., rely=0, relheight=1.)
        scrollbar_text.config(command=text.yview)
        text.config(yscrollcommand=scrollbar_text.set)
        text.place(x=0, y=0, relwidth=1, relheight=1, width=-18)
        win.geometry("400x460")
        win.title("Number of letters")

        counter = Counter(data)
        a = counter['a']
        b = counter['b']
        c = counter['c']
        d = counter['d']
        e = counter['e']
        f = counter['f']
        g = counter['g']
        h = counter['h']
        i = counter['i']
        j = counter['j']
        k = counter['k']
        l = counter['l']
        m = counter['m']
        n = counter['n']
        o = counter['o']
        p = counter['p']
        q = counter['q']
        r = counter['r']
        s = counter['s']
        t = counter['t']
        u = counter['u']
        v = counter['v']
        w = counter['w']
        x = counter['x']
        y = counter['y']
        z = counter['z']
        text.insert(INSERT, "A: ")
        text.insert(END, a)
        text.insert(END, "\nB: ")
        text.insert(END, b)
        text.insert(END, "\nC: ")
        text.insert(END, c)
        text.insert(END, "\nD: ")
        text.insert(END, d)
        text.insert(END, "\nE: ")
        text.insert(END, e)
        text.insert(END, "\nF: ")
        text.insert(END, f)
        text.insert(END, "\nG: ")
        text.insert(END, g)
        text.insert(END, "\nH: ")
        text.insert(END, h)
        text.insert(END, "\nI: ")
        text.insert(END, i)
        text.insert(END, "\nJ: ")
        text.insert(END, j)
        text.insert(END, "\nK: ")
        text.insert(END, k)
        text.insert(END, "\nL: ")
        text.insert(END, l)
        text.insert(END, "\nM: ")
        text.insert(END, m)
        text.insert(END, "\nN: ")
        text.insert(END, n)
        text.insert(END, "\nO: ")
        text.insert(END, o)
        text.insert(END, "\nP: ")
        text.insert(END, p)
        text.insert(END, "\nQ: ")
        text.insert(END, q)
        text.insert(END, "\nR: ")
        text.insert(END, r)
        text.insert(END, "\nS: ")
        text.insert(END, s)
        text.insert(END, "\nT: ")
        text.insert(END, t)
        text.insert(END, "\nU: ")
        text.insert(END, u)
        text.insert(END, "\nV: ")
        text.insert(END, v)
        text.insert(END, "\nW: ")
        text.insert(END, w)
        text.insert(END, "\nX: ")
        text.insert(END, x)
        text.insert(END, "\nY: ")
        text.insert(END, y)
        text.insert(END, "\nZ: ")
        text.insert(END, z)
        text.pack()

    except IOError:
        msg.showinfo("There is no file!", "Download file...")

