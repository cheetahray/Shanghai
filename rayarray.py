from pyo import *
import numpy as np
import math
from scipy.io import wavfile

s = Server(audio="jack").boot()

fps, sound = wavfile.read("/home/pi/Shanghai/wav/piano/52.wav")

size = len(sound) #512
t = DataTable(size, init=sound.T.tolist())
freq = t.getRate()
b = TableRead(t, freq, loop = True, mul = .00001).out() 
#t.view()


#size = len(sound) #256
#arr2 = np.array([[math.sin(2 * math.pi * j / size + math.sin(i/16.0)) for j in range(size)] for i in range(size)])
#m = NewMatrix(size, size, sound.tolist())
#m.view()

s.gui(locals())
