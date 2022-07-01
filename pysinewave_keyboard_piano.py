import keyboard
from pysinewave import SineWave

class Note:
    def __init__(self,note, key):
        self.note = note
        self.on = False
        self.sinewave=SineWave(pitch=self.note, pitch_per_second=12, decibels=-20, decibels_per_second=20, samplerate=44100)
        keyboard.on_press_key(key, lambda _:self.play_on())
        keyboard.on_release_key(key, lambda _:self.play_off())
    def play_on(self):
        if self.on: return
        self.sinewave.play()
        self.on = True
    def play_off(self):
        self.sinewave.stop()
        self.on = False

Note(10,"a")
Note(12,"s")
Note(14,"d")
Note(15,"f")
Note(17,"g")
Note(19,"h")
Note(21,"j")
Note(22,"k")
Note(24,"l")
Note(26,";")

keyboard.wait()
