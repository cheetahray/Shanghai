import numpy
import pyaudio
import analyse
import time
import fluidsynth
import socket
import serial
import ledstrip
import math
from artnet import ArtNet 
from twisted.internet import reactor
import os, sys

def raymap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart));

def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

def raymr(tid):
    global sock
    global UDP_PORT
    global UDP_IP
    global rayshift
    rndrayint = 0.0
    lastrayint = 0.0
    aacnt = 0
    istsl = 0
    while tid != rndrayint :
        if aacnt == 0:
            sock.sendto("aa", (UDP_IP, UDP_PORT))
            print ("aa")
        rayint, rayampval = raypitch()
        if rayampval > 0 :
            rndrayint = round(rayint,1)
            if lastrayint != rndrayint:
                print(str(tid) + ":"+ str(rndrayint))
                lastrayint = rndrayint
            if rayshift == tid:
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
                    time.sleep(0.5)
                    sock.sendto("mr" + str(tid-rayshift), (UDP_IP, UDP_PORT))
                    time.sleep(0.5)
            else:
                if tid < rndrayint:
                    if istsl != 1:
                        sock.sendto("ms", (UDP_IP, UDP_PORT))
                        print ("ms")
                        time.sleep(0.2)
                        sock.sendto("ml", (UDP_IP, UDP_PORT))
                        print ("ml")
                        istsl = 1
                elif tid > rndrayint:
                    if istsl != 2:
                        sock.sendto("ms", (UDP_IP, UDP_PORT))
                        print ("ms")
                        time.sleep(0.2)
                        sock.sendto("mh", (UDP_IP, UDP_PORT))
                        print ("mh")
                        istsl = 2
                else:
                    sock.sendto("ms", (UDP_IP, UDP_PORT))
                    print ("ms")
                    istsl = 0
                    time.sleep(0.5)
                    sock.sendto("mr" + str(tid-rayshift), (UDP_IP, UDP_PORT))
                    time.sleep(0.5)
        if aacnt == 100:
            aacnt = 0
        else:
            aacnt = aacnt + 1
    return True
    
def rayudp():
    global sock
    global UDP_PORT
    global UDP_IP
    global rayshift
    sock.bind(("", UDP_PORT))
    data = ''
    howmanypitch = 18
    sock.sendto("tph", (UDP_IP, UDP_PORT) )
    print ("tph")
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data == 'tphe':
        sock.sendto("tvh", (UDP_IP, UDP_PORT))
        print ("tvh")
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        if data == 'tvhe':
            sock.sendto("tsh", (UDP_IP, UDP_PORT))
            print ("tsh")
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if data == 'tshe':
                for x in range(rayshift, rayshift+howmanypitch+1):
                    raymr(x)
                sock.sendto("m" + str(howmanypitch/2) + "v126", (UDP_IP, UDP_PORT))
                print("m" + str(howmanypitch/2) + "v126")
            else:
                return False 
        else:
            return False
    else:
        print (data)
        return False
    return True
    
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
                rayampval = rayloud + 100 #rayampval = raymap(rayloud, -127, 0, 0, 127)
                #print (rayfeq, rayampval)
                return rayint, rayampval

            #strm.start_stream()
    except IOError, e:
        if e.args[1] == pyaudio.paInputOverflowed:
            rawsamps  = '\x00'
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
    global lastm
    if mylist[0] == '144':
        if mylist[2] == '0':
            mylist[2] = 0
            fl.noteoff(chnl, int(mylist[1]))
        else:
            #sock.sendto("as", (UDP_IP, UDP_PORT))
            noteint = int(mylist[1])
            #fl.noteon(chnl, noteint, int(mylist[2]))
            nowm = noteint - rayshift
            sock.sendto("m" + str(nowm) + "v126", (UDP_IP, UDP_PORT))
            anim.rayanim(255,255,255,255,nowm,math.fabs(nowm-lastm)*0.1)
            #anim.run(threaded = True, joinThread = False)
            #time.sleep(0.2)
            lastm = nowm
            #sock.sendto("av" + mylist[2], (UDP_IP, UDP_PORT))
            sock.sendto("aa", (UDP_IP, UDP_PORT))
            #anim.stopThread()
    elif mylist[0] == '224':
        bendint = int(mylist[2])
        #fl.pitch_bend( chnl,raymap(bendint, 0, 127, -8192, 8192))

#causes frame timing information to be output
ledstrip.log.setLogLevel(ledstrip.log.CRITICAL)
#set number of pixels & LED type here
driver = ledstrip.DriverLPD8806(num = 20)
#load the LEDStrip class
led = ledstrip.LEDStrip(driver, threadedUpdate = True)
#load channel test animation
anim = ledstrip.ColorWipe(led)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
UDP_PORT = 5005
UDP_IP = "192.168.12.178"
gpioartnet = None

rayshift = 42
lastm = 0
#fl = fluidsynth.Synth()
#fl.start('alsa')
chnl = 0
#sfid = fl.sfload("/home/pi/Shanghai/FluidR3_GM.sf2")
#fl.program_select(chnl, sfid, 0, 27)

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout = 0.05)

pa = pyaudio.PyAudio()
strm = pa.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True
    )

try:
    #rayudp()

    #sock.sendto("m0v126", (UDP_IP, UDP_PORT))
    #time.sleep(5)
    #sock.sendto("m18v126", (UDP_IP, UDP_PORT))
    #time.sleep(5) 

    pa.terminate()

    pa = pyaudio.PyAudio()
    strm = pa.open(
        format = pyaudio.paInt16,
        channels = 1,
        rate = 44100,
        input_device_index = 0,
        input = True,
        output_device_index = 0,
        output = True,
        stream_callback=callback
        )

    strm.start_stream()

    rr,ww=os.pipe()
    rr,ww=os.fdopen(rr,'r',0), os.fdopen(ww,'w',0)
    gpioartnet = ArtNet(rr,ww)
    pid = os.fork()

    while True:
        if pid != 0:          # Parent
            ww.close()
            data=rr.readline()
            if not data:
                rcv = readlineCR(port)
                mylist = rcv.split(" ")
                print(mylist)
                raylist(mylist)
            else:
                print data.strip()
        else:           # Child
            reactor.listenUDP(6454, gpioartnet)
            reactor.run()

except KeyboardInterrupt:
    #reactor.stop()
    gpioartnet = None
    led.all_off()
    led.update()
    strm.stop_stream()
    strm.close()    
    #fl.delete()
    pa.terminate()
