from playsound import playsound
import schedule
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from datetime import datetime, timedelta, time, date


class FirstWindow(object):
    def __init__(self, root_):
        self.root = root_
        self.var = IntVar()
        self.description_text = None

    def show_description(self):
        if self.var.get() == 1:
            self.description_text.config(
                text=f'You selected the first option. \nWith this option you can only choose a music to be played\n\
                within default school schedule(08:30 - 15:15)')
        if self.var.get() == 2:
            self.description_text.config(
                text=f'You selected the second option. \nWith this option you can separately choose a music \n\
                of the beginning and the ending, still default schedule(08:30 - 15:15)')

    def first_check(self):
        if self.var.get() == 1:
            FirstWayWindow(self.root).main()
            self.root.withdraw()

    def main(self):
        choosing_frame = Frame(bd=6)
        choosing_frame.pack(side=TOP, fill=X)
        choosing_text = Label(choosing_frame, text='Choose a way to do it babe')
        choosing_text.pack()

        first_way = Radiobutton(
            choosing_frame,
            text="Option 1",
            variable=self.var,
            value=1,
            command=self.show_description
        )
        second_way = Radiobutton(
            choosing_frame,
            text="Option 2",
            variable=self.var,
            value=2,
            command=self.show_description
        )

        first_way.pack(anchor=W)
        second_way.pack(anchor=W)

        start_button = Button(
            choosing_frame,
            text="Start",
            command=self.first_check
        )

        start_button.pack(side=BOTTOM)

        description_frame = Frame(bd=6)
        description_frame. pack(side=BOTTOM, fill=X)
        self.description_text = Label(description_frame, text='Choose one')
        self.description_text. pack()

        self.root.mainloop()


class FirstWayWindow(object):
    def __init__(self, root__):
        self.root = root__
        self.first_new_window = Toplevel(self.root)
        self.first_new_window.geometry('400x300+600+200')
        self.my_tree = None
        self.file_name = ''

    def create_schedule(self):
        start_time = datetime.combine(date.today(), time(8, 30, 00))
        t = timedelta(minutes=45)
        finish_time = start_time + t

        for i in range(1, 8):
            self.my_tree.insert(parent='', index='end', iid=i, values=(i, start_time.time(), finish_time.time()))
            t0 = timedelta(hours=1)
            start_time += t0
            finish_time += t0
            schedule.every().day.at(str(start_time.time())[:-3]).do(self.play_sound)
            schedule.every().day.at(str(finish_time.time())[:-3]).do(self.play_sound)

    def select_music(self):
        self.file_name = askopenfilename(initialdir="/", title="Select file", filetypes=[("Music files", "*.mp3 *.wav")])

    def play_sound(self):
        playsound(self.file_name)

    def main(self):
        f_n_main_frame = Frame(self.first_new_window)
        f_n_main_frame.pack()

        create = Button(f_n_main_frame, text="Create a schedule", command=self.create_schedule)
        create.pack(pady=7)

        melody_select = Button(f_n_main_frame, text="Select music", command=self.select_music)
        melody_select.pack(pady=7)

        columns = ('Номер урока', 'Время начала', 'Время окончания')
        self.my_tree = ttk.Treeview(f_n_main_frame, columns=columns, show='headings')
        self.my_tree.column("Номер урока", width=120, minwidth=25)
        self.my_tree.column("Время начала", width=120, minwidth=25)
        self.my_tree.column("Время окончания", width=120, minwidth=25)

        self.my_tree.heading("Номер урока", text="Номер урока")
        self.my_tree.heading("Время начала", text="Время начала")
        self.my_tree.heading("Время окончания", text="Время окончания")
        self.my_tree.pack(pady=20)


if __name__ == '__main__':
    root = Tk()
    root.geometry('350x300+600+200')
    root.title('Bells')
    temp_app = FirstWindow(root)
    temp_app.main()
