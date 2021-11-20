
from collections import Coun


def TEST():
    import schedule
    from datetime import datetime

    def create():
        schedule.every().day.at('08:00').do(test0).tag('start')
        schedule.every().day.at('18:00').do(test1).tag('end')

    def test0():
        print('=====TEST====')

    def test1():
        print('TEST')


    for i in range(10):
        create()

    data_start = schedule.get_jobs('start')
    # print(schedule.next_run())
    t = None
    for value in data_start:

        t = value._run
        print(value.next_run).strftime("%d.%m %H:%M:%S")
        break
    input()
    print(t)
    print(type(t))
    print(t.strftime("%d.%m %H:%M:%S"))
    # data = data_start.split('()')
    # data = [x for x in data if x.count('last')]
    # print(data)


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9'  # X11 color: 'gray85'
_ana1color = '#d9d9d9'  # X11 color: 'gray85'
_ana2color = '#ececec'  # Closest X11 color: 'gray92'

def treeview_test():
    import tkinter as tk
    import tkinter.ttk as ttk
    import sys

    def on_tree_select(event):
        data = main_tree.focus()
        status_text = main_tree.item(data, 'values')
        print(status_text)
        statusbar.configure(text=status_text[3])
        statusbar.update()


    root = tk.Tk()
    root.geometry("470x350+540+200")
    root.minsize(120, 1)
    root.maxsize(1684, 1031)
    root.resizable(1, 1)
    root.title("New Toplevel")
    root.configure(background="#d9d9d9")

    style = ttk.Style()
    if sys.platform == "win32":
        style.theme_use('winnative')
    style.configure('.', background=_bgcolor)
    style.configure('.', foreground=_fgcolor)
    style.configure('.', font="TkDefaultFont")
    style.map('.', background=[
        ('selected', _compcolor),
        ('active', _ana2color)]
                   )

    main_tree = ttk.Treeview(root, show="headings", selectmode="browse")
    main_tree.bind("<<TreeviewSelect>>", on_tree_select)

    style.configure('Treeview', font="TkDefaultFont")
    main_tree.place(relx=0.036,
                         rely=0.4,
                         relheight=0.527,
                         relwidth=0.909
                         )
    main_tree.configure(columns=("#1", "#2", "#3", "#4", "#5", "#6"))

    main_tree.heading("#1", text="№")
    main_tree.heading("#1", anchor="center")
    main_tree.column("#1", width="20")
    main_tree.column("#1", minwidth="20")
    main_tree.column("#1", stretch="1")
    main_tree.column("#1", anchor="n")

    main_tree.heading("#2", text="Расписание")
    main_tree.heading("#2", anchor="center")
    main_tree.column("#2", width="100")
    main_tree.column("#2", minwidth="20")
    main_tree.column("#2", stretch="1")
    main_tree.column("#2", anchor="n")

    main_tree.heading("#3", text="prev_start")
    main_tree.heading("#3", anchor="center")
    main_tree.column("#3", width="100")
    main_tree.column("#3", minwidth="20")
    main_tree.column("#3", stretch="1")
    main_tree.column("#3", anchor="n")

    main_tree.heading("#4", text="next_start")
    main_tree.heading("#4", anchor="center")
    main_tree.column("#4", width="100")
    main_tree.column("#4", minwidth="20")
    main_tree.column("#4", stretch="1")
    main_tree.column("#4", anchor="n")

    main_tree.heading("#5", text="prev_end")
    main_tree.heading("#5", anchor="center")
    main_tree.column("#5", width="100")
    main_tree.column("#5", minwidth="20")
    main_tree.column("#5", stretch="1")
    main_tree.column("#5", anchor="n")

    main_tree.heading("#6", text="next_end")
    main_tree.heading("#6", anchor="center")
    main_tree.column("#6", width="0")
    main_tree.column("#6", minwidth="0")
    main_tree.column("#6", stretch="1")
    main_tree.column("#6", anchor="n")

    statusbar = tk.Label(root, text="on the way…", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def hide_columns():
        main_tree["displaycolumns"]=("#1", "#2")
        main_tree.column("#2", width="400")

    def insert2():
        values = ('1111', '222')
        main_tree.insert(parent='',
                         index='end',
                         values=values)
    def insert3():
        values = ('4444', '5555', 'X', 'Z', '', 'QQQQ')
        main_tree.insert(parent='',
                         index='end',
                         values=values)
    def delete():
        main_tree.delete('1')

    def change_val():
        new_value = 'OXXOXOOXOXOXOXO'
        t = main_tree.keys()

        print(t)
        # main_tree.set(item, '#3', new_value)

    button_hide = tk.Button(root, command=hide_columns)
    button_hide.place(relx=0.054, rely=0.067, height=54, width=157)
    button_hide.configure(text='''Hide columns''')

    button2 = tk.Button(root, command=insert2)
    button2.place(relx=0.054, rely=0.222, height=54, width=157)
    button2.configure(text='''Insert 2''')

    button3 = tk.Button(root, command=insert3)
    button3.place(relx=0.39, rely=0.067, height=54, width=157)
    button3.configure(text='''Insert 3''')

    button4 = tk.Button(root, command=delete)
    button4.place(relx=0.39, rely=0.222, height=54, width=157)
    button4.configure(text='''Delete''')

    button5 = tk.Button(root, command=change_val)
    button5.place(relx=0.75, rely=0.067, height=54, width=157)
    button5.configure(text='''Change''')

    root.mainloop()
