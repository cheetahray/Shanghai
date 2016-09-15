import alsaaudio, struct
import pitchtools
import socket
import commands
import threading
import math
import time
from aubio.task import *

def aacnt():
    global aacntdone
    #sock.sendto("ms", (UDP_IP, UDP_PORT))
    #print ("ms")
    sock.sendto("aa", (UDP_IP, UDP_PORT))
    print ("aa")
    aacntdone = True

def raypitch(tid):
 
    count = 0
    counttwo = 0
    nownote = 0.0
    lastnote = 0.0
    #mydict = {}

    while True:
        #read data from audio input
        [length, data]=recorder.read()
 
        # convert to an array of floats
        floats = struct.unpack('f'*length,data)
 
        # copy floats into structure
        for i in range(len(floats)):
            fvec_write_sample(buf, floats[i], 0, i)
 
        # find pitch of audio frame
        freq = aubio_pitchdetection(detect,buf)

        # find energy of audio frame
        energy = vec_local_energy(buf)

        nownote = round(pitchtools.f2m( freq ),1)    

        #if 36 != tid and 36.0 == nownote:
        #    nownote = 101.0

        #print "{:.2f} {:.2f} {:.2f}".format(freq, energy, nownote)
        
        if freq < 5000.0 and nownote < 100.0 and energy > 0.1: #1 and energy < 7 : 

            #if freq in mydict:
            #if nownote in mydict:
                #mydict[freq] = mydict[freq] + 1
                #mydict[nownote] = mydict[nownote] + 1
            #else:
                #mydict[nownote] = 1
                #mydict[freq] = 1

            count = count + 1
            if 100 > count:  
                #for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k), reverse = True):
                    #nownote = key
                    #if nownote != lastnote:
                    #  lastnote = nownote
                    #  counttwo = 0
                    #else:
                    #  counttwo += 1
                    #  if 1 == counttwo:
                    #    counttwo = 0
                    #mydict.clear()
                    #count = 0
                print( nownote )
                    #break
            return nownote
            #else:
            #    continue

def raymr(tid):
    global sock
    global UDP_PORT
    global UDP_IP
    global rayshift
    global timer
    global aacntdone
    rndrayint = 0.0
    lastrayint = 0.0
    istsl = 0
    while float(tid) != rndrayint :
        if True == aacntdone:
            timer = threading.Timer(2, aacnt)
            aacntdone = False
            timer.start()
        rndrayint = raypitch(tid)
        if rndrayint > 0 and math.fabs(tid-rndrayint) < 1:
            #rndrayint = round(rayint,1)
            if lastrayint != rndrayint:
                print( str(tid) + ":" + str(rndrayint) )
                lastrayint = rndrayint
                time.sleep(1)
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
        elif False: #rayshift[whoami] == tid:
            sock.sendto("tst", (UDP_IP, UDP_PORT))
            print ("tst")
            istsl = 2
            time.sleep(0.5)
            sock.sendto("tss", (UDP_IP, UDP_PORT))
            print ("tss")
            time.sleep(1)
    return True

def rayudp():
    global sock
    global UDP_PORT
    global UDP_I
    global rayshift
    
    data = ''
    howmanypitch = [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 
                    18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 
                    18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 20, 20, 18, 18, 10]
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
    
    return True
    
ips = commands.getoutput("/sbin/ifconfig | grep -iA2 \"eth0\" | grep -i \"inet\" | grep -iv \"inet6\" | " +
                         "awk {'print $2'} | sed -ne 's/addr\://p'")
iplist = ips.split(".")
whoami = int(iplist[3])
UDP_IP = iplist[0] + "." + iplist[1] + "." + iplist[2] + "." + str(whoami + 100)
whoami = whoami - 1 
aacntdone = True
startmode = 1
timer = None
rayshift = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
            42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
            42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 36, 64, 42, 42, 36]
tp0 = [0, 1659, 3407, 4813, 6100, 7405, 8651, 9720, 10416, 11762, 12684, 13577, 14473, 15230, 15975, 16541, 17357, 17996, 18244, 19078, 19853]
tp = [6, 8, 11, 14, 16, 18, 20, 22, 23, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38, 40]

# constants
CHANNELS    = 1
INFORMAT    = alsaaudio.PCM_FORMAT_FLOAT_LE
RATE        = 33500
FRAMESIZE   = 1024
PITCHALG    = aubio_pitch_yin
PITCHOUT    = aubio_pitchm_freq
 
# set up audio input
#recorder=alsaaudio.PCM(type=alsaaudio.PCM_CAPTURE)
recorder=alsaaudio.PCM(type=alsaaudio.PCM_CAPTURE, card='0')
recorder.setchannels(CHANNELS)
recorder.setrate(RATE)
recorder.setformat(INFORMAT)
recorder.setperiodsize(FRAMESIZE)
 
# set up pitch detect
detect = new_aubio_pitchdetection(FRAMESIZE,FRAMESIZE/2,CHANNELS,
                                  RATE,PITCHALG,PITCHOUT)
buf = new_fvec(FRAMESIZE,CHANNELS)
 
# main loop

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
UDP_PORT = 5005
sock.bind(("0.0.0.0", UDP_PORT))

if startmode < 3:
    rayudp()

sock.close()
