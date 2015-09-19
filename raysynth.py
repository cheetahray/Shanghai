import numpy
import pyaudio
import analyse
import time
import fluidsynth
import socket
import serial

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
    global rayshift
    rndrayint = 0.0
    righthandsleep = 0.1
    lefthandsleep = 1 
    while tid != rndrayint :
        sock.sendto("av127", (UDP_IP, UDP_PORT))
        rayint, rayampval = raypitch()
        if rayampval > 0 :
            rndrayint = round(rayint,1)
            print(rndrayint)
            if 45 == tid:
                if tid < rndrayint:
                    sock.sendto("tsl", (UDP_IP, UDP_PORT))
                elif tid > rndrayint:
                    sock.sendto("tst", (UDP_IP, UDP_PORT))
                else:
                    sock.sendto("mr" + str(tid-rayshift), (UDP_IP, UDP_PORT))
                time.sleep(righthandsleep) 
                sock.sendto("tss", (UDP_IP, UDP_PORT))
            else:
                if tid < rndrayint:
                    sock.sendto("ml", (UDP_IP, UDP_PORT))
                elif tid > rndrayint:
                    sock.sendto("mh", (UDP_IP, UDP_PORT))
                else:
                    sock.sendto("mr" + str(tid-rayshift), (UDP_IP, UDP_PORT))
                time.sleep(lefthandsleep)
                sock.sendto("ms", (UDP_IP, UDP_PORT))
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
            sock.sendto("tvh", (UDP_IP, UDP_PORT))
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if data == 'tvhe':
                for x in range(45, 62):
                    raymr(x)
            else:
                return False 
        else:
            return False
    else:
        return False
    return True
    
rayshift = 44
fl = fluidsynth.Synth()
fl.start('alsa')
chnl = 0
sfid = fl.sfload("/home/pi/Shanghai/FluidR3_GM.sf2")
fl.program_select(chnl, sfid, 0, 27)

def raypitch():
    global strm
    try:
        rawsamps = strm.read(1024) # Read raw microphone data
        samps = numpy.fromstring(rawsamps, dtype=numpy.int16) # Convert raw data to NumPy array
        rayfeq = analyse.musical_detect_pitch(samps)
        if rayfeq > 0:
            #strm.stop_stream()
            rayint = round(rayfeq,1)
            if rayint >= 43 and rayint <= 62:
                rayloud = analyse.loudness(samps)
                print (rayloud, rayfeq)
                rayampval = raymap(rayloud, -17, -2, 0, 127)
                print(rayampval)
                return rayint, rayampval
            #strm.start_stream()
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
        fl.pitch_bend(chnl,0)
        fl.noteon(chnl, y, velocity) 
        fl.noteoff(chnl,y-1)
        if 1 == interpo:
            for z in range (0, 2048, 1):
                fl.pitch_bend(chnl,z) 
                #time.sleep(raysleep)
        else:
            for z in range (0, -2048, -1):
                fl.pitch_bend(chnl,z)
                #time.sleep(raysleep)
    fl.noteoff(chnl,end-1)

def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        if ch=='\r' or ch=='':
            return rv
        rv += ch

def raylist(mylist):
    global fl
    global rayshift
    if mylist[0] == '144':
        if mylist[2] == '0':
            fl.noteoff(chnl, int(mylist[1]))
        else:
            noteint = int(mylist[1])
            sock.sendto("m" + str(noteint - rayshift) + "v250", (UDP_IP, UDP_PORT))
            sock.sendto("av" + mylist[2], (UDP_IP, UDP_PORT))
            fl.noteon(chnl, noteint, int(mylist[2]))
    elif mylist[0] == '224':
        bendint = int(mylist[2])
        fl.pitch_bend( chnl,raymap(bendint, 0, 127, -8192, 8192))
        

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

while True:
    rayudp()
    rcv = readlineCR(port)
    #print(repr(rcv))
    mylist = rcv.split(" ")
    print(mylist)
    raylist(mylist)
    #rayint, rayampval = raypitch()       
    #if rayampval > 0 :
        #fl.noteon(chnl, rayint, rayampval)
    #else:
        #rayslide(45,63,64,0.0001)
    
fl.delete()
pyaud.terminate()
