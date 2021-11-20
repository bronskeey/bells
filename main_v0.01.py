import inspect
import platform

import time as ttt
import pygame
from pygame import mixer
import schedule
import main_support
from tkinter.filedialog import askopenfilename
from datetime import datetime, timedelta, time, date
from tkinter import messagebox
# import _tkinter
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True




def perc(n,p):
    return int((n / 100) * p)

WINDOW_HSIZE = 710
WINDOW_VSIZE = 450
TREE_HSIZE = 0.85915492957
TREE_VSIZE = 0.44444444444
_TREE_HSIZE = WINDOW_HSIZE * TREE_HSIZE
_TREE_VSIZE = WINDOW_VSIZE * TREE_VSIZE

# COLUMNS_SIZE = [perc(TREE_HSIZE, 10)] + [perc(TREE_HSIZE,18)] * 5
COLUMNS_SIZE = [perc(_TREE_HSIZE, 3), perc(_TREE_HSIZE, 32)] + [perc(_TREE_HSIZE,16)] * 4
HIDED1 = perc(WINDOW_HSIZE * TREE_HSIZE, 10)
HIDED2 = perc(WINDOW_HSIZE * TREE_HSIZE, 89.58)

STATUS1 = 0
STATUS2 = 0

class MainClass:
    """
     - redo status_all
     - what does "clear playlist do

    """
    print(f'*****[LOG] in {inspect.stack()[0][3]}')
    print(f'*****[LOG] in {inspect.stack()[1][3]}')
    def __init__(self, top=None):
        """
        creating objects
        calling functions to initialize all objects
        objects:
            two buttons
            frame with three buttons
            treeview
        :param top: root
        """
        # self.mixer = None
        self.current_time = ttt.time()
        _bgcolor   = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor   = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        self.path      = ''
        self.file_name = ''
        self.file_list = []

        self.style = ttk.Style()
        self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
            ('selected', _compcolor),
            ('active', _ana2color)]
                       )
        top.geometry(f"{WINDOW_HSIZE}x{WINDOW_VSIZE}+382+78")
        top.minsize(120, 1)
        top.maxsize(1684, 1031)
        top.resizable(0, 0)
        top.title("Bells")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.bind('<Control-h>', self.hide_event)
        top.after(1000, self.checkPlaying, top)

        self.label_default   = tk.LabelFrame(top)
        self.but_select_file  = tk.Button(self.label_default)
        self.but_bind_file   = tk.Button(self.label_default)
        self.but_delete_task = tk.Button(self.label_default)
        self.but_clear_tasks = tk.Button(self.label_default)

        self.label_prazdnik = tk.LabelFrame(top)
        self.but_pl_select  = tk.Button(self.label_prazdnik)
        self.but_pl_clear   = tk.Button(self.label_prazdnik)
        self.but_pl_run     = tk.Button(self.label_prazdnik)

        self.main_tree = ScrolledTreeView(top)
        self.main_tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.COL = ("#1", "#2", "#3", "#4", "#5", "#6")

        self.status_time_text = tk.StringVar()
        self.default_status_time = '   -   |||   -   '
        self.status_time_text.set(self.default_status_time)
        self.status_time = tk.Label(top, textvariable=self.status_time_text, anchor="center")

        self.status_all_text = tk.StringVar()
        self.status_all_text.set('1234567890'*6)
        self.t0 = '-'
        self.t = ''
        self.t1 = '-'
        self.default_status_all = f'{self.t0:27}|||{self.t1:27}'
        # self.status_all_text.set(self.default_status_all)
        self.status_all  = tk.Label(top, textvariable=self.status_all_text, anchor="w")

        self.init_default()
        self.init_prazdnik()

        self.init_tree()

        self.init_status()

        self.playlist = []
        self.current_track = ( 0, '' )
        pygame.init()
        mixer.init()
        # self.pygame.init()
        # self.mixer.init()

    def init_default(self):
        self.label_default.place(relx=0.07, rely=0.022, relheight=0.456
                                 , relwidth=0.424)
        self.label_default.configure(relief='groove')
        self.label_default.configure(foreground="black")
        self.label_default.configure(text='''D E F A U L T''')
        self.label_default.configure(background="#d9d9d9")
        self.label_default.configure(highlightbackground="#d9d9d9")
        self.label_default.configure(highlightcolor="black")


        self.but_select_file.place(relx=0.066, rely=0.195, height=44, width=127
                                  , bordermode='ignore')
        self.but_select_file.configure(activebackground="#ececec")
        self.but_select_file.configure(activeforeground="#000000")
        self.but_select_file.configure(background="#d9d9d9")
        self.but_select_file.configure(disabledforeground="#a3a3a3")
        self.but_select_file.configure(foreground="#000000")
        self.but_select_file.configure(highlightbackground="#d9d9d9")
        self.but_select_file.configure(highlightcolor="black")
        self.but_select_file.configure(pady="0")
        self.but_select_file.configure(text='''Select MP3''')
        self.but_select_file.configure(command=self.select_file)


        self.but_delete_task.place(relx=0.066, rely=0.585, height=44, width=127
                                   , bordermode='ignore')
        self.but_delete_task.configure(activebackground="#ececec")
        self.but_delete_task.configure(activeforeground="#000000")
        self.but_delete_task.configure(background="#d9d9d9")
        self.but_delete_task.configure(disabledforeground="#a3a3a3")
        self.but_delete_task.configure(foreground="#000000")
        self.but_delete_task.configure(highlightbackground="#d9d9d9")
        self.but_delete_task.configure(highlightcolor="black")
        self.but_delete_task.configure(pady="0")
        self.but_delete_task.configure(text='''Delete task''')
        self.but_delete_task.configure(command=self.delete_task)


        self.but_bind_file.place(relx=0.528, rely=0.195, height=44, width=127
                                 , bordermode='ignore')
        self.but_bind_file.configure(activebackground="#ececec")
        self.but_bind_file.configure(activeforeground="#000000")
        self.but_bind_file.configure(background="#d9d9d9")
        self.but_bind_file.configure(disabledforeground="#a3a3a3")
        self.but_bind_file.configure(foreground="#000000")
        self.but_bind_file.configure(highlightbackground="#d9d9d9")
        self.but_bind_file.configure(highlightcolor="black")
        self.but_bind_file.configure(pady="0")
        self.but_bind_file.configure(text='''Bind file''')
        self.but_bind_file.configure(command=self.bind_mp3)


        self.but_clear_tasks.place(relx=0.532, rely=0.585, height=44, width=127
                                   , bordermode='ignore')
        self.but_clear_tasks.configure(activebackground="#ececec")
        self.but_clear_tasks.configure(activeforeground="#000000")
        self.but_clear_tasks.configure(background="#d9d9d9")
        self.but_clear_tasks.configure(disabledforeground="#a3a3a3")
        self.but_clear_tasks.configure(foreground="#000000")
        self.but_clear_tasks.configure(highlightbackground="#d9d9d9")
        self.but_clear_tasks.configure(highlightcolor="black")
        self.but_clear_tasks.configure(pady="0")
        self.but_clear_tasks.configure(text='''Clear tasks''')
        self.but_clear_tasks.configure(command=self.clear_tasks)

    def init_prazdnik(self):
        """
        """
        self.label_prazdnik.place(relx=0.507, rely=0.022, relheight=0.456
                                  , relwidth=0.424)
        self.label_prazdnik.configure(relief='groove')
        self.label_prazdnik.configure(foreground="black")
        self.label_prazdnik.configure(text='''P R A Z D N I K''')
        self.label_prazdnik.configure(background="#d9d9d9")
        self.label_prazdnik.configure(highlightbackground="#d9d9d9")
        self.label_prazdnik.configure(highlightcolor="black")

        self.but_pl_select.place(relx=0.066, rely=0.195, height=44, width=127
                                 , bordermode='ignore')
        self.but_pl_select.configure(activebackground="#ececec")
        self.but_pl_select.configure(activeforeground="#000000")
        self.but_pl_select.configure(background="#d9d9d9")
        self.but_pl_select.configure(disabledforeground="#a3a3a3")
        self.but_pl_select.configure(foreground="#000000")
        self.but_pl_select.configure(highlightbackground="#d9d9d9")
        self.but_pl_select.configure(highlightcolor="black")
        self.but_pl_select.configure(pady="0")
        self.but_pl_select.configure(text='''Select playlist''')
        self.but_pl_select.configure(command=self.select_folder)

        self.but_pl_clear.place(relx=0.066, rely=0.58, height=44, width=127
                                , bordermode='ignore')
        self.but_pl_clear.configure(activebackground="#ececec")
        self.but_pl_clear.configure(activeforeground="#000000")
        self.but_pl_clear.configure(background="#d9d9d9")
        self.but_pl_clear.configure(disabledforeground="#a3a3a3")
        self.but_pl_clear.configure(foreground="#000000")
        self.but_pl_clear.configure(highlightbackground="#d9d9d9")
        self.but_pl_clear.configure(highlightcolor="black")
        self.but_pl_clear.configure(pady="0")
        self.but_pl_clear.configure(text='''Clear playlist''')

        self.but_pl_run.place(relx=0.525, rely=0.195, height=44, width=127
                                  , bordermode='ignore')
        self.but_pl_run.configure(activebackground="#ececec")
        self.but_pl_run.configure(activeforeground="#000000")
        self.but_pl_run.configure(background="#d9d9d9")
        self.but_pl_run.configure(disabledforeground="#a3a3a3")
        self.but_pl_run.configure(foreground="#000000")
        self.but_pl_run.configure(highlightbackground="#d9d9d9")
        self.but_pl_run.configure(highlightcolor="black")
        self.but_pl_run.configure(pady="0")
        self.but_pl_run.configure(text='''LET THE FUN BEGIN''')
        self.but_pl_run.configure(command=self.FUN_test)

    def init_tree(self):
        self.style.configure('Treeview', font="TkDefaultFont")
        self.main_tree.place(relx=0.07,
                             rely=0.489,
                             relheight=TREE_VSIZE,
                             relwidth =TREE_HSIZE
                             )
        self.main_tree.configure(columns=self.COL)
        self.main_tree.configure(show="headings")
        self.main_tree.configure(selectmode='browse')

        self.main_tree.heading("#0", text="-")
        self.main_tree.heading("#0", anchor="center")

        self.main_tree.heading("#1", text="№")
        self.main_tree.heading("#1", anchor="center")

        self.main_tree.heading("#2", text="Schedule")
        self.main_tree.heading("#2", anchor="center")

        self.main_tree.heading("#3", text="start_prev")
        self.main_tree.heading("#3", anchor="center")

        self.main_tree.heading("#4", text="start_next")
        self.main_tree.heading("#4", anchor="center")

        self.main_tree.heading("#5", text="end_prev")
        self.main_tree.heading("#5", anchor="center")

        self.main_tree.heading("#6", text="end_next")
        self.main_tree.heading("#6", anchor="center")

        for i, column in enumerate(self.COL):
            self.main_tree.column(column, width=COLUMNS_SIZE[i])
            self.main_tree.column(column, stretch="1")
            self.main_tree.column(column, anchor="center")

    def init_status(self):

        self.status_time.place(relx=0.0, rely=0.947, relheight=0.056
                               , relwidth=0.5)
        self.status_time.configure(relief='groove')
        self.status_time.configure(borderwidth="2")
        self.status_time.configure(relief="groove")
        self.status_time.configure(background="#d9d9d9")
        self.status_time.configure(highlightbackground="#d9d9d9")
        self.status_time.configure(highlightcolor="black")

        self.status_all.place(relx=0.501, rely=0.947, relheight=0.056
                              , relwidth=0.5)
        self.status_all.configure(relief='groove')
        self.status_all.configure(borderwidth="2")
        self.status_all.configure(relief="groove")
        self.status_all.configure(background="#d9d9d9")
        self.status_all.configure(highlightbackground="#d9d9d9")
        self.status_all.configure(highlightcolor="black")

        self.status_all.configure(text=self.status_all_text)

    def create_insert_schedule(self):
        self.main_tree.delete(*self.main_tree.get_children())

        values_data = [[], [], [], [], [], [], []]

        # start_time = datetime.combine(date.today(), time(8, 30, 00))
        # t = timedelta(minutes=45)

        start_time = datetime.combine(date.today(), time(21, 45, 00))
        t = timedelta(minutes=2)

        finish_time = start_time + t

        for i, data in enumerate(values_data):
            values = (i+1, f'{start_time.strftime("%H:%M")}  -  {finish_time.strftime("%H:%M")}')
            data.extend((list(values)))
            schedule.every().day.at(str(start_time.time())[:-3]).do(self.play_mp3).tag('start')
            schedule.every().day.at(str(finish_time.time())[:-3]).do(self.play_mp3).tag('end')
            t0 = timedelta(hours=1)
            start_time += t0
            finish_time += t0

        date_format = "%d.%m  %H:%M"
        data = schedule.get_jobs()

        for i, job in enumerate(data):
            try:
                last_date = job.last_run.strftime(date_format)
            except AttributeError:
                last_date = f'--.--  --:--'
            next_date = job.next_run.strftime(date_format)
            values_data[i % 7].append(last_date)
            values_data[i % 7].append(next_date)

        for i, values in enumerate(values_data):
            self.main_tree.insert(parent='',
                                  index='end',
                                  iid=i+1,
                                  values=values
                                  )

    def select_file(self):
        """
         - select a file name for a schedule
        """
        try:
            self.file_name = askopenfilename(initialdir="",
                                         title="Select file",
                                         filetypes=[("Music files", "*.mp3 *.wav")])
            self.t0 = f'File: {self.file_name.split("/")[-1]}'
            self.status_all_text.set(f'{self.t0:25}|||{self.t1:25}')

        except PermissionError:
            error_text = \
            """У вас нет доступа к этой папке, попробуйте запустить программу от имени администратора!
            """
            messagebox.showerror("Ошибка доступа", error_text)

    def bind_mp3(self):
        """
        NOT YET IMPLEMENTED
        :return:
        """
        from tkinter import messagebox
        if self.file_name:
            self.create_insert_schedule()
        else:
            error_text = \
            """Музыкальный файл для звонка не выбран. Хотите выбрать файл?
            """
            if messagebox.askokcancel("File not selected!", error_text):
                self.select_file()
                self.status_all.configure(text=self.file_name)
                self.status_all.update()

    def play_mp3(self):
        print(f'=====[LOG] in {inspect.stack()[0][3]}')
        from pygame import mixer
        import time
        mixer.init()
        mixer.music.load(self.file_name)
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(1)



    def delete_task(self):
        """
        NOT YET IMPLEMENTED
        :return:
        """
        data = self.main_tree.focus()
        self.main_tree.delete(data)
        self.status_all_text.set(self.default_status_all)

    def clear_tasks(self):
        """
        NOT YET IMPLEMENTED
        :return:
        """
        self.main_tree.delete(*self.main_tree.get_children())
        self.status_all_text.set(' '*10 + '|||' + ' '*10)




    def select_folder(self):
        from tkinter.filedialog import askdirectory
        from pathlib import Path
        import os
        self.path = askdirectory(title='Выберите папку с музыкой', initialdir='.')
        self.playlist = [Path(f'{self.path}/{filename}').resolve() for filename in os.listdir(self.path)]
        # self.t = self.path.split("/")
        # self.t1 = f'Folder: {self.t[0]}/ ... /{self.t[-2]}/{self.t[-1]}'
        # self.status_all_text.set(f'{self.t0} || {self.t1}')

    def FUN_test(self):
        """
        - implement player in class
        - add .music.stop() before each bell ring to stop music
        :return:
        """
        track_index, track_name = self.current_track
        if track_index >= len(self.playlist):  # if out of music, re-start
            track_index = 0

        # Play the current track
        try:
            name = self.playlist[track_index]
        except:
            print(self.playlist, track_name, track_index)
        self.current_track = (track_index, name)
        mixer.music.set_volume(10)
        # mixer_.music.load(f'C:/Users/user/Desktop/python/projects/etc/{name}.mp3')
        mixer.music.load(name)
        mixer.music.play()

    def checkPlaying(self, main_window):
        print(f'=====[LOG] in {inspect.stack()[0][3]}')
        print(f'=====[LOG] in {inspect.stack()[1][3]}')
        print(f'time taken: {ttt.time() - self.current_time:.3f} s')
        self.current_time = ttt.time()
        result = False
        if self.playlist:
            if mixer.music.get_busy():
                # Still playing
                result = True
            else:
                # Playing has finished
                print("Sound finished, playing next")
                track_index, track_name = self.current_track
                self.current_track = (track_index + 1, '')
                self.FUN_test()
                result = False

            # Queue the next call to this function
            main_window.after(3*10**3, self.checkPlaying, main_window)
        else:
            result = True
            main_window.after(10*10**3, self.checkPlaying, main_window) # seconds * 10**3
        return result




    def hide_event(self, event):
        if self.main_tree["displaycolumns"][0] == "#all" or self.main_tree["displaycolumns"] == self.COL:
            self.hide_columns()
        else:
            self.show_columns()

    def hide_columns(self):
        self.main_tree["displaycolumns"]=("#1", "#2")
        self.main_tree.column("#1", width=HIDED1)
        self.main_tree.column("#2", width=HIDED2)

    def show_columns(self):
        # self.main_tree["displaycolumns"] = self.COL
        self.main_tree["displaycolumns"] = ("#all", )
        for i, column in enumerate(self.COL):
            self.main_tree.column(column, width=COLUMNS_SIZE[i] + 1)


    def on_tree_select(self, event):
        data = self.main_tree.focus()
        data_text = self.main_tree.item(data, 'values')
        try:
            status_text = f"{data_text[2]}  -  {data_text[3]}     |||     {data_text[4]}  -  {data_text[5]}"
        except IndexError:
            status_text = ''
        self.status_time_text.set(status_text)



    # unused
    def run_music(self):
        """
        - not used
        """
        from pathlib import Path
        import pygame
        import os
        NEXT = pygame.USEREVENT + 1
        playlist = [Path(f'{self.path}/{filename}').resolve() for filename in os.listdir(self.path)]
        tracks_number = len(playlist)
        current_track = 0
        pygame.init()
        pygame.mixer.init()  # frequency = 48000
        pygame.mixer.music.load(str(playlist[current_track]))
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(NEXT)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == NEXT:
                    current_track = (current_track + 1) % tracks_number
                    pygame.mixer.music.load(str(playlist[current_track]))
                    pygame.mixer.music.play()


"""
=======================================================================================================================
"""

class AutoScroll(object):
    # print(f'[LOG] in {inspect.stack()[0][3]}')
    # print(f'[LOG] in {inspect.stack()[1][3]}')
    """Configure the scrollbars for a widget."""

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    # print(f'[LOG] in {inspect.stack()[0][3]}')
    # print(f'[LOG] in {inspect.stack()[1][3]}')
    """Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget."""

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    # print(f'[LOG] in {inspect.stack()[0][3]}')
    # print(f'[LOG] in {inspect.stack()[1][3]}')
    """A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed."""

    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    # print(f'[LOG] in {inspect.stack()[0][3]}')
    # print(f'[LOG] in {inspect.stack()[1][3]}')
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    # print(f'[LOG] in {inspect.stack()[0][3]}')
    # print(f'[LOG] in {inspect.stack()[1][3]}')
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    # print(f'[LOG] in {inspect.stack()[0][3]}')
    # print(f'[LOG] in {inspect.stack()[1][3]}')
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    # print(f'[LOG] in {inspect.stack()[0][3]}')
    # print(f'[LOG] in {inspect.stack()[1][3]}')
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')



w, w_win, root = None, None, None
def create_MainClass(rt, *args, **kwargs):
    """Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' ."""
    global w, w_win, root
    root = rt
    w = tk.Toplevel(root)
    top = MainClass(w)
    main_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_MainClass():
    global w
    w.destroy()
    w = None


def vp_start_gui():
    print(f'=====[LOG] in {inspect.stack()[0][3]}')
    print(f'=====[LOG] in {inspect.stack()[1][3]}')
    """
    Starting point when module is the main routine.
    """
    global root # removed val, w
    root = tk.Tk()
    top = MainClass(root)
    main_support.init(root, top)
    root.mainloop()


if __name__ == '__main__':
    print(f'[IN][LOG] in {__name__}')
    vp_start_gui()
