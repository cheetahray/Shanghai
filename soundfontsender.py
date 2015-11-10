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
                    data, addr = sock.recvfrom(1024)
                    tp.append(int(data))
                    print(int(data))
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
                    data, addr = sock.recvfrom(1024)
                    tp.append(int(data))
                    time.sleep(0.5)
        if aacnt == 100:
            aacnt = 0
        else:
            aacnt = aacnt + 1
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
                headd = tp[0]
                taill = tp[len(tp)-1]
                for x in range(0, howmanypitch+1):    
                    tp[x] = raymap (tp[x], headd, taill, 0, 20)
                print(tp)
                sock.sendto("m" + str(howmanypitch/2) + "v126", (UDP_IP, UDP_PORT))
                print("m" + str(howmanypitch/2) + "v126")
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
    global islightout
    global issoundfont
    global chnl
    global pa
    global strm

    if mylist[0] == '144':
        if mylist[2] == '0':
            if True == issoundfont:
                fl.noteoff(chnl, int(mylist[1]))
        else:
            #sock.sendto("as", (UDP_IP, UDP_PORT))
            noteint = int(mylist[1])
            if True == issoundfont:
                fl.noteon(chnl, noteint, int(mylist[2]))
            nowm = noteint - rayshift
            sock.sendto("m" + str(nowm) + "v126", (UDP_IP, UDP_PORT))
            nowm = tp[ nowm ]
            if False == islightout:    
                anim.rayanim(255,255,255,255,nowm,math.fabs(nowm-lastm)*0.1)
            #time.sleep(0.2)
            lastm = nowm
            #sock.sendto("av" + mylist[2], (UDP_IP, UDP_PORT))
            sock.sendto("aa", (UDP_IP, UDP_PORT))
    elif mylist[0] == '224':
        if True == issoundfont:
            fl.pitch_bend( chnl,raymap(int(mylist[2]), 0, 127, -8192, 8192))
    elif mylist[0] == '225':
        islightout = int(mylist[1])
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
                    stream_callback=callback
                )
                strm.start_stream()
            issoundfont = False

def handler():
    gpioartnet = None
    led.all_off()
    led.update()
    strm.stop_stream()
    strm.close()
    pa.terminate()

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
sock.bind(("0.0.0.0", UDP_PORT))
gpioartnet = ArtNet()

rayshift = 42
lastm = 0
tp=[]
islightout = True
issoundfont = False
chnl = 0
strm = None
pa = pyaudio.PyAudio()
fl = None
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout = 0.01)

#rayudp()

#sock.sendto("m0v126", (UDP_IP, UDP_PORT))
#time.sleep(5)
#sock.sendto("m18v126", (UDP_IP, UDP_PORT))
#time.sleep(5) 

if True == issoundfont:
    fl = fluidsynth.Synth()
    fl.start('alsa')
    sfid = fl.sfload("/home/pi/Shanghai/FluidR3_GM.sf2")
    fl.program_select(chnl, sfid, 0, int(mylist[2]) )
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
        stream_callback=callback
    )
    strm.start_stream()

sock.settimeout(0.01) 

while True:
    rcv = readlineCR(port)
    if rcv != '':
        mylist = rcv.split(" ")
        print(mylist)
        raylist(mylist)
    if True == islightout:
        try:
            data, addr = sock.recvfrom(1024)
            mylist = data.split(" ") 
            anim.drawone(int(mylist[0]),int(mylist[1]),int(mylist[2]),int(mylist[3]),int(mylist[4]))
        except socket.timeout:
            pass

handler()
