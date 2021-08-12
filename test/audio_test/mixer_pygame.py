'''import pygame.mixer


PATH = 'C:\\Users\\Home\\Desktop\\depo\\'
BELLS_PATH = '/\\'

from tkinter.filedialog import askopenfilename


def mixer_from_pygame(NAME):
    """
    works
    """
    from pygame import mixer
    import time
    mixer.init()
    mixer.music.load(NAME)
    mixer.music.play()
    input()

    if mixer.music.get_busy:
        print('Still playing')
        print(mixer.music.get_busy())
    print('wait a second')
    input()

    current_time = mixer.music.get_pos()
    mixer.music.stop()
    print('Music stopped')
    input()

    mixer.music.play(-1, current_time/1000.0)

    while mixer.music.get_busy():
        time.sleep(1)


import os
import pygame

# NAME = askopenfilename(initialdir=".", title="Select file", filetypes=[("Music files", "*.mp3 *.wav")])
# mixer_from_pygame(NAME)'''
from tkinter.filedialog import askdirectory
from pathlib import Path
import pygame
import os

def test_event_type():
    from tkinter.filedialog import askdirectory
    from pathlib import Path
    import pygame
    import os
    NEXT = pygame.USEREVENT + 1
    PATH = askdirectory(title='Select Folder')
    playlist = [Path(f'{PATH}/{filename}').resolve() for filename in os.listdir(PATH)]
    tracks_number = len(playlist)
    current_track = 0
    pygame.init()
    pygame.mixer.init() # frequency = 48000
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(NEXT)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == NEXT:
                current_track = (current_track + 1) % tracks_number
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()
import time
def some_function():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(0)
    clock = time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        clock.tick(10)
    Rest_of_function