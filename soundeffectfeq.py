import numpy
import pyaudio
import analyse
import time
import fluidsynth
import socket
import serial
import math
import threading
import commands

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
            if rayshift[whoami] == tid:
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
                    sock.sendto("mr" + str(tid-rayshift[whoami]), (UDP_IP, UDP_PORT))
                    data, addr = sock.recvfrom(1024)
                    tp0[tid-rayshift[whoami]] = int(data)
                    print(data)
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
                    sock.sendto("mr" + str(tid-rayshift[whoami]), (UDP_IP, UDP_PORT))
                    data, addr = sock.recvfrom(1024)
                    tp0[tid-rayshift[whoami]] = int(data)
                    print(data)
                    time.sleep(0.5)
            if aacnt == 25:
                aacnt = 0
            else:
                aacnt = aacnt + 1
        elif rayshift[whoami] == tid:
            sock.sendto("tst", (UDP_IP, UDP_PORT))
            print ("tst")
            istsl = 2
            time.sleep(0.5)
            sock.sendto("tss", (UDP_IP, UDP_PORT))
            print ("tss")
            time.sleep(1)
            aacnt = 0
    return True
    
def rayudp():
    global sock
    global UDP_PORT
    global UDP_I
    global rayshift
    global pa
    global strm

    strm = pa.open(
        format = pyaudio.paInt16,
        channels = 1,
        rate = 44100,
        input_device_index = 0,
        input = True
    )

    data = ''
    howmanypitch = [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 
                    18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 
                    18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 21, 21, 18, 18, 21]
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
                if 1 == startmode:
                    for x in range(rayshift[whoami], rayshift[whoami] + howmanypitch[whoami]):
                        raymr(x)
                    #headd = tp0[0]
                    taill = tp0[len(tp0)-1]
                    for x in range(0, howmanypitch[whoami]):    
                        tp[x] =  int( float(tp0[x]) / float(taill) * 35.0 ) 
                        tp[x] = tp[x] + 5
                    print(tp0)
                    print(tp)
                    sock.sendto("mt1", (UDP_IP, UDP_PORT))
            else:
                return False 
        else:
            return False
    else:
        print (data)
        return False
    
    strm.stop_stream()
    strm.close()    
    pa.terminate()

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
            if True:#rayint <= 83:

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

def rayslide(thetwo):
    bendbool = False
    if thetwo > 0:
        bendbool = (nowm-thetwo >= 0) and (nowm+thetwo <= len(tp0)-1)
    elif thetwo < 0:
        bendbool = (nowm-thetwo <= len(tp0)-1) and (nowm+thetwo >= 0)
    if True == bendbool:
        sock.sendto("as", (UDP_IP, UDP_PORT))
        bend1 = nowm-thetwo
        sock.sendto("mt" + str(bend1) , (UDP_IP, UDP_PORT))
        sock.sendto("aa", (UDP_IP, UDP_PORT))
        bend2 = nowm+thetwo
        sock.sendto("m" + str(bend2) + "v" + math.fabs(tp0[bend1]-tp0[bend2]), (UDP_IP, UDP_PORT))
        nowm += thetwo

def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        if ch=='\r' or ch=='':
            return rv
        rv += ch

def func():
    #sock.sendto("av" + mylist[2], (UDP_IP, UDP_PORT))
    sock.sendto("aa", (UDP_IP, UDP_PORT))
    clientsock.send("picker")

def raylist(mylist):
    global fl
    global rayshift
    global lastm
    global nowm
    global islightout
    global issoundfont
    global chnl
    global pa
    global strm
    global timer
    global isslide0
    global isslide127
    global tp
    if mylist[0] == '144':
        if mylist[2] == '0':
            if True == issoundfont:
                fl.noteoff(chnl, int(mylist[1]))
        else:
            #sock.sendto("as", (UDP_IP, UDP_PORT))
            noteint = int(mylist[1])
            if True == issoundfont:
                fl.noteon(chnl, noteint, int(mylist[2]))
            nowm = noteint - rayshift[whoami]
            sock.sendto("mt" + str(nowm) , (UDP_IP, UDP_PORT))
            timer = threading.Timer(0.3, func )
            if False == islightout and nowm >= 0 and nowm < 21:
                clientsock.send("slide{0} {1}".format(tp[nowm],math.fabs(tp[nowm]-tp[lastm])*0.03))
            lastm = nowm
            timer.start()
    elif mylist[0] == '224':
        if True == issoundfont:
            fl.pitch_bend( chnl,raymap(int(mylist[2]), 0, 127, -8192, 8192))
        if True == isslide0 and '1' == mylist[2]:
            rayslide(2)
        if True == isslide127 and '126' == mylist[2]:
            rayslide(-2)
        if '0' == mylist[2]:
            isslide0 = True
        else: 
            isslide0 = False
            isslide127 = False
        if '127' == mylist[2]:
            isslide127 = True
        else:
            isslide127 = False
            isslide0 = False
    elif mylist[0] == '225':
        islightout = int(mylist[1])
        if '1' == islightout: 
            clientsock.send("out")
        elif '0' == islightout:
            clientsock.send("in")
    elif mylist[0] == '249':
        if '1' == mylist[1]:
            if False == issoundfont:
                strm.stop_stream()
                strm.close()    
                pa.terminate()
        
                fl = fluidsynth.Synth()
                fl.start('alsa')
                sfid = fl.sfload("/home/pi/Shanghai/FluidR3_GM.sf2")
            fl.program_select(chnl, sfid, 0, int(mylist[2]) )
            issoundfont = True
        elif '0' == mylist[1]:
            if True == issoundfont:    
                fl.delete()
                pa = pyaudio.PyAudio()
                strm = pa.open(
                    format = pyaudio.paInt16,
                    channels = 1,
                    rate = 44100,
                    input_device_index = 0,
                    input = True,
                    output_device_index = 0,
                    output = True,
                    frames_per_buffer=1024,
                    stream_callback=callback
                )
                strm.start_stream()
            issoundfont = False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
UDP_PORT = 5005
ips = commands.getoutput("/sbin/ifconfig | grep -iA2 \"eth0\" | grep -i \"inet\" | grep -iv \"inet6\" | " +
                         "awk {'print $2'} | sed -ne 's/addr\://p'")
iplist = ips.split(".")
whoami = int(iplist[3])
UDP_IP = iplist[0] + "." + iplist[1] + "." + iplist[2] + "." + str(whoami + 100)
whoami = whoami - 1 
sock.bind(("0.0.0.0", UDP_PORT))
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect(("127.0.0.1", 9999))

isslide0 = False
isslide127 = False
startmode = 2
timer = None
rayshift = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
            42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
            42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 36, 64, 42, 42, 64]
lastm = 0
nowm = 0
tp0 = [0, 1659, 3407, 4813, 6100, 7405, 8651, 9720, 10416, 11762, 12684, 13577, 14473, 15230, 15975, 16541, 17357, 17996, 18244, 19078, 19853]
tp = [6, 8, 11, 14, 16, 18, 20, 22, 23, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38, 40]
islightout = False
issoundfont = False
chnl = 0
strm = None
pa = pyaudio.PyAudio()
fl = None
port = serial.Serial("/dev/ttyAMA0", baudrate=115200)#, timeout=0.01)

if startmode < 3:
    rayudp()

if True == issoundfont:
    fl = fluidsynth.Synth()
    fl.start('alsa')
    sfid = fl.sfload("/home/pi/Shanghai/FluidR3_GM.sf2")
    fl.program_select(chnl, sfid, 0, 27)
else:    
    pa = pyaudio.PyAudio()
    strm = pa.open(
        format = pyaudio.paInt16,
        channels = 1,
        rate = 44100,
        input_device_index = 0,
        input = True,
        output_device_index = 0,
        output = True,
        frames_per_buffer=1024,
        stream_callback=callback
    )
    strm.start_stream()
try:
    port.flushInput()
    port.flushOutput()
    while True:
        rcv = readlineCR(port)
        if rcv != '':
            mylist = rcv.split(" ")
            #print(mylist)
            raylist(mylist)
except KeyboardInterrupt:    
    strm.stop_stream()
    strm.close()
    pa.terminate()
    sock.close()
