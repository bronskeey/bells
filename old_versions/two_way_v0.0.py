# coding: utf-8

# ver 0.01

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
# from tkinter.messagebox import showerror
from datetime import datetime, timedelta, time, date
# from playsound import playsound
# import threading
# import sys
# import os
# import schedule


# import time

def show_description():
    if var.get() == 1:
        description_text.config(
            text=f'You selected the first option. \nWith this option you can only choose a music to be played\n\
            within default school schedule(08:30 - 15:15)')
    if var.get() == 2:
        description_text.config(
            text=f'You selected the second option. \nWith this option you can separately choose a music of the\n\
            beginning and the ending, still default schedule(08:30 - 15:15)')


def check():
    if var.get() == 1:
        first_way_window()
        root.withdraw()


def first_way_window():
    def create_schedule():
        start_time = datetime.combine(date.today(), time(8, 30, 00))
        t = timedelta(minutes=45)
        finish_time = start_time + t
        for i in range(1, 8):
            my_tree.insert(parent='', index='end', iid=i, values=(i, start_time.time(), finish_time.time()))
            t0 = timedelta(hours=1)
            start_time += t0
            finish_time += t0

    def select_music():
        fname = askopenfilename(initialdir="/", title="Select file", filetypes=[("Music files", "*.mp3 *.wav")])
        # if fname:
        # try:
        # print("""here it comes: self.settings["template"].set(fname)""")
        # except:                     # <- naked except is a bad idea
        # showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        # return

    def bind_music_to_schedule():
        pass

    first_new_window = Toplevel(root)
    first_new_window.geometry('400x300+600+200')

    f_n_main_frame = Frame(first_new_window)
    f_n_main_frame.pack()

    create = Button(f_n_main_frame, text="Create a schedule", command=create_schedule)
    # create = Button(f_n_main_frame, text="Create a schedule", command=create_schedule)
    create.pack(pady=7)

    melody_select = Button(f_n_main_frame, text="Select music", command=select_music)
    melody_select.pack(pady=7)

    columns = ('Номер урока', 'Время начала', 'Время окончания')
    my_tree = ttk.Treeview(f_n_main_frame, columns=columns, show='headings')
    my_tree.column("Номер урока", width=120, minwidth=25)
    my_tree.column("Время начала", width=120, minwidth=25)
    my_tree.column("Время окончания", width=120, minwidth=25)

    my_tree.heading("Номер урока", text="Номер урока")
    my_tree.heading("Время начала", text="Время начала")
    my_tree.heading("Время окончания", text="Время окончания")

    my_tree.pack(pady=20)

    # create_schedule()


root = Tk()
root.geometry('350x300+600+200')
root.title('Bells')

choosing_frame = Frame(bd=6)
choosing_frame.pack(side=TOP, fill=X)
choosing_text = Label(choosing_frame, text='Choose a way to do it babe')
choosing_text.pack()

var = IntVar()
first_way = Radiobutton(choosing_frame, text="Option 1", variable=var, value=1, command=show_description)
second_way = Radiobutton(choosing_frame, text="Option 2", variable=var, value=2, command=show_description)

first_way.pack(anchor=W)
second_way.pack(anchor=W)

# R3 = Radiobutton(choosing_frame, text="Option 3", variable=var, value=3)
# R3.pack( anchor = W)


start_button = Button(choosing_frame, text="Start", command=check)
start_button.pack(side=BOTTOM)

description_frame = Frame(bd=6)
description_frame.pack(side=BOTTOM, fill=X)
description_text = Label(description_frame, text='Choose one')
description_text.pack()

root.mainloop()
