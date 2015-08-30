from pyo import *
import time
from threading import Timer
import pyautogui

def print_time():
    global s
    s.gui()

def play_wav(raywav):
    a.setPath(raywav)
    b.setInput(a) 
    threading.Timer(0, print_time, ()).start()
    time.sleep(10)  # sleep while time-delay events execute
    pyautogui.hotkey('ctrl', 'q')

s = Server(audio="jack").boot()
s.start()
a = SfPlayer("/home/pi/Shanghai/wav/Strat F- 52.wav", loop=False, mul=.4)
b = Freeverb(a, size=[.79,.8], damp=.9, bal=.3).out()
play_wav("/home/pi/Shanghai/wav/Strat F- 82.wav")
