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
import wave
import pitchtools

def raymap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart));

def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

def tscnt(mystr,ttime):
    global UDP_tuple
    mycmd(mystr)
    time.sleep(ttime)
    mycmd("tss")
    time.sleep(0.75)
    
def mycmd(mystr):
    global UDP_tuple
    sock.sendto(mystr, UDP_tuple)
    print (mystr)

def raymr(tid):
    global sock
    global UDP_PORT
    global UDP_IP
    global rayshift
    global whattype
    global UDP_tuple
    rndrayint = 0.0
    basscnt = 0
    tenorcnt = 0
    altocnt = 0
    sopranocnt = 0.0
    if 3 != startmode:
        tttid, basefeq = shiftbase(tid, rayshift[whoami]) 
        while tttid != rndrayint :
            mycmd("ms")
            mycmd("aa") 
            #if 0 == whattype[whoami]:
            #    time.sleep(0.1)
            #elif 1 == whattype[whoami]:
            #    time.sleep(0.111)
            if 2 >= whattype[whoami]:
                time.sleep(10)
            elif 3 == whattype[whoami]:
                time.sleep(15)
            rndrayint = round(raypitch(),1)
            ismh = False
            feqnochange = True
            lastfeq = rndrayint
            while tttid != rndrayint :
                if basscnt > 30:
                    if True == feqnochange:
                        tscnt("tst",0.1)
                    basscnt = 0
                    break;
                elif tenorcnt > 25:
                    tenorcnt = 0
                    break;
                elif altocnt > 15:
                    altocnt = 0
                    break;
                elif sopranocnt > 5.0:
                    sopranocnt = 0.0
                    break;
                elif rndrayint > 0: 
                    checkfreq = str(tttid) + ":" + str(rndrayint)
                    print( checkfreq )
                    sock.sendto(checkfreq, ("192.168.12.255", 15005))
                    if basefeq == tttid :
                        bassbool = ( 3 == whattype[whoami] and ( rndrayint - tttid > 2.5 or tttid - rndrayint > 8.5 ) )
                        tenorbool = ( 2 >= whattype[whoami] and ( rndrayint - tttid > 2.5 or tttid - rndrayint > 6.0 ) )
                        altobool = False #( 1 == whattype[whoami] and ( rndrayint - tttid > 2.5 or tttid - rndrayint > 8.0 ) )
                        sopranobool = False #( 0 == whattype[whoami] )
                        if True == bassbool:
                            if rndrayint - lastfeq > 0.1:
                                feqnochange = False  
                                lastfeq = rndrayint
                            basscnt += 1
                        elif True == tenorbool:
                            tenorcnt += 1
                        elif True == altobool:
                            altocnt += 1 
                        elif tttid < rndrayint:
                            basscnt = 0
                            tenorcnt = 0
                            altocnt = 0
                            tscnt("tsl",0.025)
                            if True == sopranobool:
                                sopranocnt += 6
                        elif tttid > rndrayint:
                            basscnt = 0
                            tenorcnt = 0
                            altocnt = 0
                            tscnt("tst",0.025)
                            if True == sopranobool:
                                sopranocnt += 6
                    else:
                        bassbool = ( 3 == whattype[whoami] and (rndrayint - tttid > 1.5 or tttid - rndrayint > 1.5) )
                        tenorbool = ( 2 == whattype[whoami] and ( rndrayint - tttid > 0.5 or tttid - rndrayint > 1.5 ) )
                        altobool = ( 1 == whattype[whoami] and ( rndrayint - tttid > 0.5 or tttid - rndrayint > 1.5 ) )
                        sopranobool = ( 0 == whattype[whoami] )
                        if True == bassbool:
                            basscnt += 1   
                        elif True == tenorbool:
                            tenorcnt += 1
                        elif True == altobool:
                            altocnt += 1
                        elif tttid < rndrayint:
                            if True == ismh:
                                mycmd("ms")
                                ismh = False
                                mycmd("ml")
                            if True == sopranobool:
                                if (tttid - basefeq) >= 15 : 
                                    sopranocnt += 1
                                else:
                                    sopranocnt += 0.375
                        elif tttid > rndrayint:
                            if False == ismh:
                                mycmd("ms")
                                ismh = True
                                mycmd("mh")
                            if True == sopranobool:
                                if (tttid - basefeq) >= 15 :
                                    sopranocnt += 1
                                else:
                                    sopranocnt += 0.375
                rndrayint = round(raypitch(),1)
        mycmd("ms")
        checkfreq = str(tttid) + ":" + str(rndrayint)
        print( checkfreq )
        sock.sendto(checkfreq, ("192.168.12.255", 15005))
        mycmd("mr" + str(tttid-basefeq))
        data, addr = sock.recvfrom(1024)
        tp0[tttid-basefeq] = int(data)
        print(tp0[tttid-basefeq])
    else: 
        mycmd("tst")
        time.sleep(0.5)
        mycmd("tss")
        time.sleep(1)
    
def rayudp():
    global sock
    global UDP_PORT
    global UDP_I
    global rayshift
    global pa
    global strm
    global chunk
    global whattype
    global UDP_tuple
    thischunk = chunk
    if True:#whattype[whoami] > 0:
        thischunk = 8192
    strm = pa.open(
        format = pyaudio.paInt16,
        channels = 1,
        rate = 44100,
        input_device_index = 0,
        input = True,
        frames_per_buffer = thischunk
    )
    
    data = ''
    mycmd("tph")
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data == 'tphe':
        mycmd("tvh")
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        if data == 'tvhe':
            mycmd("tsh")
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if data == 'tshe':
                if 1 == startmode:
                    if False: #whattype[whoami] == 3:
                        for x in range(rayshift[whoami], rayshift[whoami] + 5):
                            raymr(x)
                    else:
                        for x in range(rayshift[whoami], rayshift[whoami] + howmanypitch[whoami]):
                            raymr(x)
                    #headd = tp0[0]
                    taill = tp0[howmanypitch[whoami]-1]
                    for x in range(0, howmanypitch[whoami]):    
                        tp[whattype[whoami]][x] =  int( float(tp0[x]) / float(taill) * 35.0 ) 
                        tp[whattype[whoami]][x] = tp[whattype[whoami]][x] + 5
                    print(tp0)
                    print(tp)
                elif 2 == startmode:
                    #if 30 == whoami:
                    #    sock.sendto("mt2", UDP_tuple)
                    #    print ("mt2")
                    for x in range(rayshift[whoami], rayshift[whoami] + 1):
                        raymr(x)
                elif 3 == startmode:
                    sock.sendto("tsl", UDP_tuple)
                    time.sleep(2.5)
                    sock.sendto("tss", UDP_tuple)
                    time.sleep(0.5)
                    sock.sendto("tst", UDP_tuple)
                    time.sleep(2.5)
                    sock.sendto("tss", UDP_tuple)
                    sock.sendto("mh", UDP_tuple)
                    time.sleep(2.5)
                    sock.sendto("ms", UDP_tuple)
                    time.sleep(0.5)
                    sock.sendto("ml", UDP_tuple)
                    time.sleep(2.5)
                    sock.sendto("ms", UDP_tuple)
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
    global chunk
    thenote = 0.0
    try:
        if True:#0 != whattype[whoami]:
            thischunk = 8192
            sdata = strm.read(thischunk)
            swidth = pyaudio.paInt16
            window = numpy.blackman(thischunk)
            RATE = 44100
            # unpack the data and times by the hamming window
            indata = numpy.array(wave.struct.unpack("%dh"%(len(sdata)*4/swidth),sdata))*window
            # Take the fft and square each value
            fftData=abs(numpy.fft.rfft(indata))**2
            # find the maximum
            which = fftData[1:].argmax() + 1
            # use quadratic interpolation around the max
            if which != len(fftData)-1:
                y0,y1,y2 = numpy.log(fftData[which-1:which+2:])
                x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
                # find the frequency and output it
                thefreq = (which+x1)*RATE/thischunk
            else:
                thefreq = which*RATE/thischunk
            thenote = pitchtools.f2m(thefreq)
            #if thenote > 32 and thenote < 90:
                #print "The freq is %f Hz. Note is %f" % (thefreq, thenote)
                #pass
            #else:
                #thenote = 0.0
        else:
            sdata = strm.read(chunk)
            samps = numpy.fromstring(sdata, dtype=numpy.int16) # Convert raw data to NumPy array
            rayfeq = analyse.musical_detect_pitch(samps)
            #print (rayfeq)
            if rayfeq > 0:
                #strm.stop_stream()
                #rayint = round(rayfeq,1)
                if True:#rayint <= 83:
                    #rayloud = analyse.loudness(samps)
                    #rayampval = rayloud + 100 #rayampval = raymap(rayloud, -127, 0, 0, 127)
                    #print (rayfeq, rayampval)
                    thenote = rayfeq
                #strm.start_stream()
    except IOError, e:
        if e.args[1] == pyaudio.paInputOverflowed:
            pass
        else:
            raise
    return thenote 
    
def rayslide(thetwo):
    global UDP_tuple 
    bendbool = False
    if thetwo > 0:
        bendbool = (nowm-thetwo >= 0) and (nowm+thetwo <= len(tp0)-1)
    elif thetwo < 0:
        bendbool = (nowm-thetwo <= len(tp0)-1) and (nowm+thetwo >= 0)
    if True == bendbool:
        sock.sendto("as", UDP_tuple)
        bend1 = nowm-thetwo
        sock.sendto("mt" + str(bend1) , UDP_tuple)
        sock.sendto("aa", UDP_tuple)
        bend2 = nowm+thetwo
        sock.sendto("m" + str(bend2) + "v" + math.fabs(tp0[bend1]-tp0[bend2]), UDP_tuple)
        nowm += thetwo

def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        if ch=='\r' or ch=='':
            return rv
        rv += ch

def funcdrop(printnote):
    global UDP_tuple
    global dropnote
    global canweas
    global whoami
    if 1 == canweas[whoami]:
        sock.sendto("aa", UDP_tuple)
        print("aa" + str(printnote))
        clientsock.send("picker")
        canweas[whoami] = 2
    dropnote = False

def funcdrop2(printnote):
    global UDP_tuple
    global canweas
    global whoami
    if 1 == canweas[whoami]:
        sock.sendto("aa", UDP_tuple)
        print("aa" + str(printnote))
        clientsock.send("picker")
        canweas[whoami] = 2

def funcdrop3(printnote):
    global dropnote
    dropnote = False
    
def func():
    global UDP_tuple
    mycmd("aa")
    clientsock.send("picker")
    
def AR(printnote, velocity):
    global UDP_tuple
    global canweas
    global whoami
    global biggestvolume
    global issoundfont
    if 3 == canweas[whoami]:
        if False == issoundfont:
            nowvolume = (biggestvolume-60) * velocity / 127 + 60
            commands.getoutput("amixer cset numid=6 " + str(nowvolume) + "% " + str(nowvolume) + "%")
        sock.sendto("ar", UDP_tuple)
        print("ar" + str(printnote))
        canweas[whoami] = 1
    
def AS(printnote):
    global UDP_tuple
    global canweas
    global whoami
    if 2 == canweas[whoami]:
        sock.sendto("as", UDP_tuple)
        print("as" + str(printnote))
        canweas[whoami] = 3
    
def fluidnoteon(chnl, noteint, intmylist):
    global fl
    fl.noteon(chnl, noteint, intmylist)
    
def shiftbase(mynote, mybase):
    global whattype
    global whoami
    tttid = mynote
    basefeq = mybase
    if 0 == whattype[whoami]:
        tttid = mynote - 22
        basefeq = mybase - 22
    elif 1 == whattype[whoami]:
        tttid = mynote - 10
        basefeq = mybase - 10
    return tttid, basefeq

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
    global isslide0
    global isslide127
    global tp
    global howmanypitch
    global UDP_tuple
    global dropnote
    global biggestvolume
    global aanote
    notedelay = 1.5
    if mylist[0] == '128':
        if not ( len(mylist) == 4 and mylist[3] != str(whoami+1) ):
            noteint = int(mylist[1])
            nowm = noteint - rayshift[whoami]
            #print(nowm)
            if False == issoundfont:
                if nowm >= 0 and nowm < howmanypitch[whoami]:
                    threading.Timer(notedelay, AS, [noteint]).start()
                    isthistablenumberone = True
            else:
                threading.Timer(notedelay-0.3, fl.noteoff, [chnl, noteint]).start()
                threading.Timer(notedelay, AS, [noteint]).start()
    elif mylist[0] == '144':
        if not ( len(mylist) == 4 and mylist[3] != str(whoami+1) ):
            noteint = int(mylist[1])
            nowm = noteint - rayshift[whoami]
            #print(nowm)
            if False == issoundfont:
                if nowm >= 0 and nowm < howmanypitch[whoami]:
                    if mylist[2] != '0': 
                         if False == dropnote:
                             threading.Timer(notedelay, funcdrop, [noteint]).start()
                             threading.Timer(notedelay-0.1, AR, [noteint,int(mylist[2])]).start()
                             mycmd("mt" + str(nowm))
                             dropnote = True
                             if False == islightout:
                                 clientsock.send("slide{0} {1} {2}".format( tp[whattype[whoami]][nowm] , math.fabs( tp[whattype[whoami]][nowm]-tp[whattype[whoami]][lastm] )*0.025 , whattype[whoami] ) )
                             lastm = nowm
                    else:
                         threading.Timer(notedelay, AS, [noteint]).start()
            else:
                if nowm < 0:
                    nowm = 0
                elif nowm >= howmanypitch[whoami]:
                    nowm = howmanypitch[whoami] - 1
                if mylist[2] != '0': 
                    if False == dropnote:
                        threading.Timer(notedelay, funcdrop, [noteint]).start()
                        threading.Timer(notedelay-0.1, AR, [noteint,int(mylist[2])]).start()
                        threading.Timer(notedelay-0.3, fluidnoteon, [chnl, noteint, int(mylist[2])] ).start()
                        mycmd("mt" + str(nowm))
                        dropnote = True
                        if False == islightout:
                            clientsock.send("slide{0} {1} {2}".format( tp[whattype[whoami]][nowm] , math.fabs( tp[whattype[whoami]][nowm]-tp[whattype[whoami]][lastm] )*0.025 , whattype[whoami] ) )
                        lastm = nowm
                else:
                    threading.Timer(notedelay-0.3, fl.noteoff, [chnl, noteint]).start()
                    threading.Timer(notedelay, AS, [noteint]).start()

    elif mylist[0] == '224':
        if not ( len(mylist) == 4 and mylist[3] != str(whoami+1) ):
            noteint = int(mylist[1])
            aanote = noteint
            nowm = noteint - rayshift[whoami]
            #print(nowm)
            if False == issoundfont:
                if nowm >= 0 and nowm < howmanypitch[whoami]:
                    if mylist[2] != '0': 
                         if False == dropnote:
                             threading.Timer(notedelay, funcdrop3, [noteint]).start()
                             #threading.Timer(notedelay-0.1, AR, [noteint,int(mylist[2])]).start()
                             mycmd("mt" + str(nowm))
                             dropnote = True
                             if False == islightout:
                                 clientsock.send("slide{0} {1} {2}".format( tp[whattype[whoami]][nowm] , math.fabs( tp[whattype[whoami]][nowm]-tp[whattype[whoami]][lastm] )*0.025 , whattype[whoami] ) )
                             lastm = nowm
                    else:
                         threading.Timer(notedelay, AS, [noteint]).start()
            else:
                if nowm < 0:
                    nowm = 0
                elif nowm >= howmanypitch[whoami]:
                    nowm = howmanypitch[whoami] - 1
                if mylist[2] != '0': 
                    if False == dropnote:
                        threading.Timer(notedelay, funcdrop3, [noteint]).start()
                        #threading.Timer(notedelay-0.1, AR, [noteint,int(mylist[2])]).start()
                        #threading.Timer(notedelay-0.3, fluidnoteon, [chnl, noteint, int(mylist[2])] ).start()
                        mycmd("mt" + str(nowm))
                        dropnote = True
                        if False == islightout:
                            clientsock.send("slide{0} {1} {2}".format( tp[whattype[whoami]][nowm] , math.fabs( tp[whattype[whoami]][nowm]-tp[whattype[whoami]][lastm] )*0.025 , whattype[whoami] ) )
                        lastm = nowm
                else:
                    threading.Timer(notedelay-0.3, fl.noteoff, [chnl, noteint]).start()
                    threading.Timer(notedelay, AS, [noteint]).start()
                
    elif mylist[0] == '225':
        if '1' == mylist[1]:
            islightout = True 
            clientsock.send("out")
        elif '0' == mylist[1]:
            islightout = False 
            clientsock.send("in")
        elif '2' == mylist[1]:
            islightout = False 
            clientsock.send("qq")
    elif mylist[0] == '249':
        if '3' == mylist[1]:
            if False == issoundfont and pa is None:
                pa = pyaudio.PyAudio()
                strm = pa.open(
                    format = pyaudio.paInt16,
                    channels = 1,
                    rate = 44100,
                    input_device_index = 0,
                    input = True,
                    output_device_index = 0,
                    output = True,
                    frames_per_buffer = chunk,
                    stream_callback=callback
                )
                strm.start_stream()
            elif True == issoundfont and fl is None:
                fl = fluidsynth.Synth()
                fl.start('alsa')
                sfid = fl.sfload("/home/pi/Shanghai/FluidR3_GM.sf2")
                fl.program_select(chnl, sfid, 0, 27 )
        elif '2' == mylist[1]:
            if False == issoundfont and pa is not None:
                strm.stop_stream()
                strm.close()    
                pa.terminate()
                pa = None
            elif True == issoundfont and fl is not None:
                fl.delete()
                fl = None
        elif '1' == mylist[1]:
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
                    frames_per_buffer = chunk,
                    stream_callback=callback
                )
                strm.start_stream()
            issoundfont = False
    elif mylist[0] == '253':
        if mylist[1] == str(whoami+1):   
            biggestvolume = int(mylist[2])
            commands.getoutput("amixer cset numid=6 " + mylist[2] + "% " + mylist[2] + "%")
chunk = 1024
biggestvolume = 0
#commands.getoutput("cd /home/pi/ShanghaiB")
#commands.getoutput("/usr/bin/unzip pitchtools-master.zip")
#time.sleep(1)
#commands.getoutput("cd pitchtools-master")
#commands.getoutput("/usr/bin/python setup.py install")
#time.sleep(90)
ips = commands.getoutput("/sbin/ifconfig | grep -iA2 \"eth0\" | grep -i \"inet\" | grep -iv \"inet6\" | " +
                         "awk {'print $2'} | sed -ne 's/addr\://p'")
iplist = ips.split(".")
whoami = int(iplist[3])
UDP_IP = iplist[0] + "." + iplist[1] + "." + iplist[2] + "." + str(whoami + 100)
whoami = whoami - 1 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
UDP_PORT = 5005
UDP_tuple = (UDP_IP, UDP_PORT)
sock.bind(("0.0.0.0", UDP_PORT))
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect(("127.0.0.1", 9999))
dropnote = False
#isslide0 = False
#isslide127 = False
isthistablenumberone = True
startmode = 4
           # 1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
rayshift = [60, 60, 60, 60, 60, 60, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 38, 38, 38,
            38, 38, 38, 28, 28, 28, 28, 28, 38, 48, 48, 48, 60, 60, 60, 48, 48, 38, 38, 28, 
            28, 28, 28, 38, 38, 38, 38, 38, 38, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 
            60, 60, 60, 60, 60, 60, 60, 48, 38, 60, 60, 48, 38, 28]
               # 1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
howmanypitch = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
                20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
                20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
                20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
whattype = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 
            2, 2, 2, 3, 3, 3, 3, 3, 2, 1, 1, 1, 0, 0, 0, 1, 1, 2, 2, 3, 
            3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
            0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 2, 3]
canweas = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
lastm = 0
nowm = 0
tp0 = [0, 2120, 4879, 7575, 10566, 13007, 15121, 17015, 19858, 21518, 23323, 24730, 26738, 27945, 30184, 31591, 32820, 33827, 35629, 36685, 37689]
tp = [ [5, 7, 10, 13, 15, 18, 20, 22, 24, 26, 27, 29, 31, 32, 33, 35, 36, 37, 38, 40, 40],
       [5, 7, 10, 13, 15, 18, 20, 22, 24, 26, 28, 29, 31, 32, 33, 35, 36, 37, 39, 40, 40],
       [5, 8, 10, 13, 16, 18, 20, 22, 24, 26, 28, 29, 31, 32, 34, 35, 36, 37, 39, 40, 40],
       [5, 7, 10, 13, 15, 18, 20, 22, 24, 26, 28, 29, 31, 32, 34, 35, 36, 37, 39, 40, 40]  ]
islightout = True
issoundfont = True
chnl = 0
strm = None
pa = None
fl = None
#port = serial.Serial("/dev/ttyAMA0", baudrate=115200)#, timeout=0.01)
aanote = 0
while True:
    for ii in range(0,66):
        canweas[ii] = 2
    pa = pyaudio.PyAudio()
    
    if 3 == startmode:
        issoundfont = True
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
            frames_per_buffer = chunk,
            stream_callback=callback
        )
        strm.start_stream()
    try:
        #port.flushInput()
        #port.flushOutput()
        if 3 == startmode:
            threading.Timer(1, AS, [0]).start()
            clientsock.send("in")
            time.sleep(0.5)
            islightout = False
            clientsock.send("rgbw")
            time.sleep(3.5)
        elif 4 == startmode:
            threading.Timer(1, AS, [0]).start()
        else:
            threading.Timer(10, AS, [0]).start()
            
        commands.getoutput("amixer cset numid=6 100% 100%")    
        while True:
            #rcv = readlineCR(port)
            rcv, addr = sock.recvfrom(1024)
            if len(rcv) > 0:
                if rcv == 'Home':
                    mycmd(rcv)
                    if False == issoundfont:
                        strm.stop_stream()
                        strm.close()    
                        pa.terminate()
                    else:
                        fl.delete()
                    break
                elif addr[0].endswith("202") and rcv == '100':
                    #if aanote > 0:
                    fluidnoteon(0, aanote, 127)
                    threading.Timer(0.1, AR, [aanote, 127]).start()
                    threading.Timer(0.2, funcdrop2, [aanote]).start()
                    #    aanote = 0
                else:
                    mylist = rcv.split(" ")
                    if (mylist[0] == "249" or mylist[0] == "224"):
                       print mylist
                    raylist(mylist)
    except KeyboardInterrupt:    
        strm.stop_stream()
        strm.close()
        pa.terminate()
        sock.close()
