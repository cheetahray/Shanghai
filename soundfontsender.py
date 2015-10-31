import numpy
import pyaudio
import analyse
import time
import fluidsynth
import socket
import serial
import threading

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
                        time.sleep(0.1)
                        sock.sendto("ml", (UDP_IP, UDP_PORT))
                        print ("ml")
                        istsl = 1
                elif tid > rndrayint:
                    if istsl != 2:
                        sock.sendto("ms", (UDP_IP, UDP_PORT))
                        print ("ms")
                        time.sleep(0.1)
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
            #if data == 'tshe':
            #    for x in range(rayshift, rayshift+howmanypitch+1):
            #        raymr(x)
            #    sock.sendto("m" + str(howmanypitch/2) + "v126", (UDP_IP, UDP_PORT))
            #    print("m" + str(howmanypitch/2) + "v126")
            #    sock.sendto("m10v126", (UDP_IP, UDP_PORT))
            #else:
            #    return False 
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
                rayampval = rayloud + 127 #rayampval = raymap(rayloud, -127, 0, 0, 127)
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
    global timercnt
    if mylist[0] == '144':
        if mylist[2] == '0':
            mylist[2] = 0 #fl.noteoff(chnl, int(mylist[1]))
        else:
            #sock.sendto("as", (UDP_IP, UDP_PORT))
            noteint = int(mylist[1])
            sock.sendto("m" + str(noteint - rayshift) + "v126", (UDP_IP, UDP_PORT))
            #fl.noteon(chnl, noteint, int(mylist[2]))
            #sock.sendto("av" + mylist[2], (UDP_IP, UDP_PORT))
            #if 5 == timercnt:
            #    timercnt = 0
            #else:
            #    timercnt = timercnt + 1
            #if 0 == timercnt:
            #    timer0 = threading.Timer(0.125, func0)
            #    timer0.start()
            #elif 1 == timercnt:
            #    timer1 = threading.Timer(0.125, func1)
            #    timer1.start()
            #elif 2 == timercnt:
            #    timer2 = threading.Timer(0.125, func2)
            #    timer2.start()
            #elif 3 == timercnt:
            #    timer3 = threading.Timer(0.125, func3)
            #    timer3.start()
            #elif 4 == timercnt:           
            #    timer4 = threading.Timer(0.125, func4)
            #    timer4.start()
            sock.sendto("aa", (UDP_IP, UDP_PORT))
    elif mylist[0] == '224':
        bendint = int(mylist[2])
        #fl.pitch_bend( chnl,raymap(bendint, 0, 127, -8192, 8192))

def func0():
    sock.sendto("aa", (UDP_IP, UDP_PORT))

def func1():
    sock.sendto("aa", (UDP_IP, UDP_PORT))

def func2():
    sock.sendto("aa", (UDP_IP, UDP_PORT))

def func3():
    sock.sendto("aa", (UDP_IP, UDP_PORT))

def func4():
    sock.sendto("aa", (UDP_IP, UDP_PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
UDP_PORT = 5005
UDP_IP = "192.168.12.178"

rayshift = 42
#fl = fluidsynth.Synth()
#fl.start('alsa')
#chnl = 0
#sfid = fl.sfload("/home/pi/Shanghai/FluidR3_GM.sf2")
#fl.program_select(chnl, sfid, 0, 27)

port = serial.Serial("/dev/ttyAMA0", baudrate=115200)

pa = pyaudio.PyAudio()
strm = pa.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True
    )

#rayudp()

timercnt = 0

#while True:
#    rcv = readlineCR(port)
#    mylist = rcv.split(" ")
#    print(mylist)
#    raylist(mylist)

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
while strm.is_active():
    rcv = readlineCR(port)
    mylist = rcv.split(" ")
    print(mylist)
    raylist(mylist)
    #time.sleep(0.1)
strm.stop_stream()
strm.close()    
    
#fl.delete()
