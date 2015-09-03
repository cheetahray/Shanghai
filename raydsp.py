from pyo import *
import numpy
import pyaudio
import analyse
import math

def raymap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart));

s = Server(audio="jack",duplex=0).boot()
s.start()

CHUNK = 8192
pyaud = pyaudio.PyAudio()
lastfeq = 0

stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True,
    output_device_index = 1,
    output = False,
    frames_per_buffer=CHUNK
    )
    
while True:
    #data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print ("received message:", data)
    rawsamps = stream.read(CHUNK) # Read raw microphone data
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16) # Convert raw data to NumPy array
    rayfeq = analyse.musical_detect_pitch(samps)
    if rayfeq > 0 and math.fabs(rayfeq-lastfeq) > 2:
        stream.stop_stream()
        rayloud = analyse.loudness(samps)
        print (rayloud, rayfeq)
        raystr = "/home/pi/Shanghai/wav/guitar/" + str(int(round(rayfeq))) + ".wav"
        #print(raystr)
        a = SfPlayer(raystr, loop=False, mul=.4)
        mm = Mixer()
        mm.addInput(0,a)
        rayampval = raymap(rayloud, -24, -1, 0, 20)
        #print(rayampval)
        mm.setAmp(vin=0, vout=0, amp=rayampval)
        b = WGVerb(mm[0], feedback=0.9, bal=1).out()
        #pat = Pattern(function=assign,time=0).play()
        #a.setPath(raystr)
        #b.setInput(a)
        #b.out()
        lastfeq = rayfeq
        #time.sleep(6)
        stream.start_stream()
    else:
        lastfeq = 0

pyaud.terminate()



