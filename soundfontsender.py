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
UDP_IP = "192.168.12.178"
        
def raymr(tid):
    global sock
    global UDP_PORT
    global UDP_IP
    global rayshift
    rndrayint = 0.0
    avcnt = 0
    istsl = 0
    while tid != rndrayint :
        if avcnt == 0:
            sock.sendto("av126", (UDP_IP, UDP_PORT))
            print ("av126")
        rayint, rayampval = raypitch()
        if rayampval > 0 :
            rndrayint = round(rayint,1)
            if 42 == tid:
                print(str(tid) + ":"+ str(rndrayint))
                if tid < rndrayint:
                    if istsl != 1:
                        sock.sendto("tsl", (UDP_IP, UDP_PORT))
                        print ("tsl")
                        istsl = 1
                elif tid > rndrayint:
                    if istsl != 2:
                        sock.sendto("tst", (UDP_IP, UDP_PORT))
                        print ("tst")
                        istsl = 2
                else:
                    sock.sendto("tss", (UDP_IP, UDP_PORT))
                    print ("tss")
                    istsl = 0
                    sock.sendto("mr" + str(tid-rayshift), (UDP_IP, UDP_PORT))
            else:
                if tid < rndrayint:
                    sock.sendto("ml", (UDP_IP, UDP_PORT))
                    sock.sendto("ms", (UDP_IP, UDP_PORT))
                elif tid > rndrayint:
                    sock.sendto("mh", (UDP_IP, UDP_PORT))
                    sock.sendto("ms", (UDP_IP, UDP_PORT))
                else:
                    sock.sendto("mr" + str(tid-rayshift), (UDP_IP, UDP_PORT))
        if avcnt == 100:
            avcnt = 0
        else:
            avcnt = avcnt + 1
    return True
    
def rayudp():
    global sock
    global UDP_PORT
    global UDP_IP
    sock.bind(("", UDP_PORT))
    data = ''
    #while len(data) == 0: 
    sock.sendto("tph", (UDP_IP, UDP_PORT) )
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data == 'tphe':
        sock.sendto("tvh", (UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        if data == 'tvhe':
            sock.sendto("tsh", (UDP_IP, UDP_PORT))
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if data == 'tshe':
                for x in range(42, 43):
                    raymr(x)
            else:
                return False 
        else:
            return False
    else:
        return False
    return True
    
rayshift = 41
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
            if rayint <= 83:

                rayloud = analyse.loudness(samps)
                rayampval = rayloud + 127 #rayampval = raymap(rayloud, -127, 0, 0, 127)
                #print (rayfeq, rayampval)
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
            sock.sendto("m" + str(noteint - rayshift) + "v248", (UDP_IP, UDP_PORT))
            sock.sendto("av" + mylist[2], (UDP_IP, UDP_PORT))
            fl.noteon(chnl, noteint, int(mylist[2]))
    elif mylist[0] == '224':
        bendint = int(mylist[2])
        fl.pitch_bend( chnl,raymap(bendint, 0, 127, -8192, 8192))
        

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

if True:
    rayudp()
    #rcv = readlineCR(port)
    #mylist = rcv.split(" ")
    #mylist = ['144','55','125']
    #print(mylist)
    #raylist(mylist)
    
fl.delete()
#pyaud.terminate()
