import simpleaudio as sa
audio = sa.WaveObject.from_wave_file("music.wav")
play = audio.play()
play.wait_done()