from pysinewave import SineWave
from time import sleep
from threading import Thread

def play(a):
    sinewave=SineWave(pitch=a, pitch_per_second=12, decibels=-20, decibels_per_second=20, samplerate=44100)
    sinewave.play()
    sinewave.set_volume(-200)
    sleep(1)
    sinewave.stop()

def key(a):
    t=Thread(None, play, args={a,})
    tt.append(t)
    t.start()

r=-20
tt=[]

for k in [10,12,[15,19],r,15,12,[15,20],r,15,17,12,r,12,10,15,r]:
    if isinstance(k,int): key(k+12)
    elif isinstance(k,list):
        for kk in k: key(kk+12)
    sleep(0.5)

for ttt in tt: ttt.join()

# maybe its my computer but it stutters weirdly when playing threaded notes
