from pyo import *
import numpy
import pyaudio
import analyse
import math

s = Server(audio="jack").boot()
s.start()

def assign():
    mm.setAmp(vin=0, vout=0, amp=5)

CHUNK = 8192
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
    rawsamps = stream.read(CHUNK) # Read raw microphone data
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16) # Convert raw data to NumPy array
    rayfeq = analyse.musical_detect_pitch(samps)
    #print (analyse.loudness(samps), rayfeq)
    if rayfeq > 0 and math.fabs(rayfeq-lastfeq) > 2:
        stream.stop_stream()
        print (analyse.loudness(samps), rayfeq)
        raystr = "/home/pi/Shanghai/wav/" + str(int(round(rayfeq))) + ".wav"
        print(raystr)
        a = SfPlayer(raystr, loop=False, mul=.4)
        mm = Mixer()
        mm.addInput(0,a)
        b = WGVerb(mm[0], feedback=0.9, bal=1).out()
        pat = Pattern(function=assign).play()
        #a.setPath(raystr)
        #b.setInput(a)
        #b.out()
        #pat.play() 
        lastfeq = rayfeq
        time.sleep(5)
        stream.start_stream()
    else:
        lastfeq = 0

pyaud.terminate()


