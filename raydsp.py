from pyo import *
import numpy
import pyaudio
import analyse
import math

s = Server(audio="jack").boot()
s.start()

a = SfPlayer("/home/pi/Shanghai/wav/52.wav", loop=False, mul=.4)
mm = Mixer()
mm.addInput(0,a)
b = Freeverb(mm[0], size=[.79,.8], damp=.9).out()

# Dynamic assignation of inputs to outputs with random amplitude
def assign():
    #global mm
    mm.setAmp(vin=0, vout=0, amp=10)

pat = Pattern(function=assign)
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
    # Read raw microphone data
    rawsamps = stream.read(CHUNK)
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    rayfeq = analyse.musical_detect_pitch(samps)
    #print (analyse.loudness(samps), rayfeq)
    if rayfeq > 0 and math.fabs(rayfeq-lastfeq) > 2:
        stream.stop_stream()
        print (analyse.loudness(samps), rayfeq)
        raystr = "/home/pi/Shanghai/wav/" + str(int(round(rayfeq))) + ".wav"
        print(raystr)
        a.setPath(raystr) #a = SfPlayer(raystr, loop=False, mul=.4)
        #b.setInput(a)
        #b.out()
        pat.play() #pat = Pattern(function=assign
        lastfeq = rayfeq
        #time.sleep(5)
        stream.start_stream()
    else:
        lastfeq = 0

pyaud.terminate()

