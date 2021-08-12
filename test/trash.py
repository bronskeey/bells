
def test_path():
    from pathlib import Path
    from tkinter.filedialog import askopenfilename

    name = askopenfilename(initialdir=".", title="Select file",
                                             filetypes=[("Music files", "*.mp3 *.wav")])
    # print(name)
    # print(Path(name).absolute())

def test_sizes():
    def perc(n, p):
        return (n / 100) * p

    WINDOW_HSIZE = 710
    WINDOW_VSIZE = 450
    TREE_HSIZE = 610
    TREE_VSIZE = 200
    COLUMNS_SIZE = [perc(TREE_HSIZE, 10)] + [perc(TREE_HSIZE, 18)] * 5
    print(COLUMNS_SIZE)

def test_file_list():
    from tkinter.filedialog import askopenfilename

    from pathlib import Path

    pl_name = askopenfilename(initialdir=".", title="Select file",
                           filetypes=[("WPL Playlists", "*.wpl")])

    abs_pl_name = Path(pl_name).absolute()

    with open(abs_pl_name, 'r', encoding="utf-8") as file:
        data = file.readlines()

    print(data)
    input()
    good_data = [x.strip()[:-3] for x in data if x.count('src')]
    good_data = [x.split('\\') for x in good_data]
    good_data = ['PATH'+[x for x in t if x.count('mp3')][0] for t in good_data]

    file_list = good_data
    print(file_list)

def perc(n,p):
    return int((n / 100) * p)

def math():
    WINDOW_HSIZE = 710
    WINDOW_VSIZE = 450
    TREE_HSIZE = 0.85915492957
    TREE_VSIZE = 0.44444444444
    _TREE_HSIZE = WINDOW_HSIZE * TREE_HSIZE
    _TREE_VSIZE = WINDOW_VSIZE * TREE_VSIZE

    # COLUMNS_SIZE = [perc(TREE_HSIZE, 10)] + [perc(TREE_HSIZE,18)] * 5
    COLUMNS_SIZE = [perc(_TREE_HSIZE, 3), perc(_TREE_HSIZE, 32)] + [perc(_TREE_HSIZE, 16)] * 4
    HIDED1 = perc(WINDOW_HSIZE * TREE_HSIZE, 10)
    HIDED2 = perc(WINDOW_HSIZE * TREE_HSIZE, 89.58)

    STATUS1 = 0
    STATUS2 = 0
    print(COLUMNS_SIZE)
