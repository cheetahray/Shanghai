import numpy
import pyaudio
import analyse
import time
import fluidsynth
import socket

def raymap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart));

pa = pyaudio.PyAudio()
strm = pa.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True
    )

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP    
UDP_PORT = 5005
UDP_IP = "192.168.11.178"
        
def raymr(tid):
    global sock
    global UDP_PORT
    global UDP_IP
    rndrayint = 0.0
    while tid != rndrayint :
        rayint, rayampval = raypitch()
        if rayampval > 0 :
            rndrayint = round(rayint,1)
            if tid < rndrayint:
                sock.sendto("ms", (UDP_IP, UDP_PORT))
                sock.sendto("a", (UDP_IP, UDP_PORT))
            else:
                sock.sendto("mh", (UDP_IP, UDP_PORT))
                sock.sendto("a", (UDP_IP, UDP_PORT))
            time.sleep(5)
    return True
    
def rayudp():
    global sock
    global UDP_PORT
    global UDP_IP
    sock.bind(("127.0.0.1", UDP_PORT))
    sock.sendto("tsh", (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data == 'tshe':
        sock.sendto("tph", (UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        if data == 'tphe':
            for x in range(45, 62):
                raymr(x)
        else:
            return False
    else:
        return False
    

fl = fluidsynth.Synth()
fl.start('alsa')

sfid = fl.sfload("/home/pi/Shanghai/FluidR3_GM.sf2")
fl.program_select(0, sfid, 0, 60)

def raypitch():
    global strm
    try:
        rawsamps = strm.read(1024) # Read raw microphone data
        samps = numpy.fromstring(rawsamps, dtype=numpy.int16) # Convert raw data to NumPy array
        rayfeq = analyse.musical_detect_pitch(samps)
        if rayfeq > 0:
            #strm.stop_stream()
            #fl.noteoff(0, rayint)
            rayint = round(rayfeq,1)
            if rayint >= 43 and rayint <= 62:
                rayloud = analyse.loudness(samps)
                print (rayloud, rayfeq)
                rayampval = raymap(rayloud, -17, -2, 0, 127)
                print(rayampval)
                return rayint, rayampval
            #strm.start_stream()
        #else:
            #fl.noteon(0, 60, 127)
            #time.sleep(5)
    except IOError, e:
        if e.args[1] == pyaudio.paInputOverflowed:
            rawsamps  = '\x00' # * CHUNK
        else:
            raise
    return 0,0

def rayslide(begin,end,velocity, raysleep):
    global fl
    interpo = 1
    if begin > end:
        interpo = -1
    for y in range (begin, end, interpo ):
        fl.pitch_bend(0,0)
        fl.noteon(0, y, velocity) 
        fl.noteoff(0,y-1)
        if 1 == interpo:
            for z in range (0, 4096, 1):
                fl.pitch_bend(0,z) 
                #time.sleep(raysleep)
        else:
            for z in range (0, -4096, -1):
                fl.pitch_bend(0,z)
                #time.sleep(raysleep)
    fl.noteoff(0,end-1)

while True:
    rayint, rayampval = raypitch()       
    if rayampval > 0 :
        fl.noteon(0, rayint, rayampval)
    else:
        #rayslide(45,63,64,0.0001)
        #fl.noteon(0,60,127)
        #fl.cc(0, 91, 0) 
        #time.sleep(4)
    
fl.delete()
pyaud.terminate()
