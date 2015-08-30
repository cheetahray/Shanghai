from pyo import *
import numpy
import pyaudio
import analyse
import math

s = Server(audio="jack").boot()
s.start()
a = SfPlayer("/home/pi/Shanghai/wav/Strat F- 52.wav", loop=False, mul=.4)
b = Freeverb(a, size=[.79,.8], damp=.9, bal=.3)

CHUNK = 8192
#wf = wave.open('thesong.wav', 'rb')
pyaud = pyaudio.PyAudio()
lastfeq = 0

stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 1,
    input = True,
    output_device_index = 1,
    output = False,
    frames_per_buffer=CHUNK
    )
    
while True:
    # Read raw microphone data
    rawsamps = stream.read(CHUNK)
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    rayfeq = analyse.musical_detect_pitch(samps)
    #print (analyse.loudness(samps), rayfeq)
    if rayfeq > 0 and math.fabs(rayfeq-lastfeq) > 2:
        stream.stop_stream()
        print (analyse.loudness(samps), round(rayfeq))
        a.setPath("/home/pi/Shanghai/wav/Strat F- " + str(int(round(rayfeq))) + ".wav")
        #b.setInput(a)
        b.out()
        time.sleep(30)
        lastfeq = rayfeq
        stream.start_stream()
    else:
        lastfeq = 0

pyaud.terminate()
