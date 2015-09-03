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
        raystr = "/home/pi/Shanghai/wav/piano/" + str(int(round(rayfeq))) + ".wav"
        print(raystr)
        rayampval = raymap(rayloud, -19, -1, 0, 4)
        print(rayampval)
        a = SfPlayer(raystr, loop=False, mul=rayampval)
        #mm = Mixer()
        #mm.addInput(0,a)
        #mm.setAmp(vin=0, vout=0, amp=rayampval)
        b = WGVerb(a, feedback=0.95, bal=0.5).out()
        lastfeq = rayfeq
        time.sleep(1)
        stream.start_stream()
    else:
        lastfeq = 0

pyaud.terminate()



