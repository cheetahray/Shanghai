from pyo import *
import numpy
import pyaudio
import analyse

def raymap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart));

s = Server(audio="jack",duplex=0).boot()
s.start()

CHUNK = 8192
pyaud = pyaudio.PyAudio()

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
    if rayfeq > 0:
        stream.stop_stream()
        rayint = round(rayfeq,1)
        if rayint >= 43 and rayint <= 62:
            raystr = "/home/pi/Shanghai/wav/horn/" + str(rayint) + ".wav"
            print(raystr)
            rayloud = analyse.loudness(samps)
            print (rayloud, rayfeq)
            rayampval = raymap(rayloud, -20, -1, 0, 4)
            print(rayampval)
            if rayampval > 0:
                a = SfPlayer(raystr, loop=False, mul=rayampval)
                b = WGVerb(a, feedback=0.95, bal=0.5).out()
                Clean_objects(4, a, b).start()
        stream.start_stream()

pyaud.terminate()



