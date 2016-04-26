# Art-Net protocol for Pimoroni Unicorn Hat
# Open Pixel Control protocol for Pimoroni Unicorn Hat
# License: MIT
import RPi.GPIO as GPIO
import socket
import time
import commands
import ledmatrix as rayled
from threading import * 
import sys
import thread

def handler(clientsocket, clientaddr):
    global islightout
    global qq50
    global QQ
    while 1:
        data = clientsocket.recv(1024)
        if ( len(data) == 6  and (data[0:6] == "picker") ):
            GPIO.output(13, False) #p13.ChangeDutyCycle(0)
            if False == QQ:
                p38.ChangeDutyCycle(100) #GPIO.output(38, True)
                p40.ChangeDutyCycle(0) #GPIO.output(40, False)
            Timer(0.333, func).start()
        elif ( len(data) >= 5  and (data[0:5] == "slide") ):
            if False == islightout:
                if True == QQ and 50 == qq50:
                    qq50 = 0
                    p40.ChangeDutyCycle(qq50)
                mylist2 = data[5:].split(" ")
                #print(mylist2)
                if '0' == mylist2[2] : 
                    anim.rayanim(0,255,0,255,int(mylist2[0])+1,float(mylist2[1]))
                    if False == QQ:
                        p31.ChangeDutyCycle(0)
                        p33.ChangeDutyCycle(100)
                        p35.ChangeDutyCycle(0)
                elif '1' == mylist2[2] : 
                    anim.rayanim(255,255,255,255,int(mylist2[0])+1,float(mylist2[1]))
                    if False == QQ:
                        p31.ChangeDutyCycle(100)
                        p33.ChangeDutyCycle(100)
                        p35.ChangeDutyCycle(100)
                elif '2' == mylist2[2] : 
                    anim.rayanim(255,112,0,255,int(mylist2[0])+1,float(mylist2[1]))
                    if False == QQ:
                        p31.ChangeDutyCycle(100)
                        p33.ChangeDutyCycle(50)
                        p35.ChangeDutyCycle(0)
                elif '3' == mylist2[2] : 
                    anim.rayanim(255,0,0,255,int(mylist2[0])+1,float(mylist2[1]))
                    if False == QQ:
                        p31.ChangeDutyCycle(100)
                        p33.ChangeDutyCycle(0)
                        p35.ChangeDutyCycle(0)
        elif len(data) == 3  and (data[0:3] == "out"):
            QQ = False
            qq50 = 50
            Timer(5, musicend).start()
            islightout = True
            anim.cleargb()
        elif len(data) == 2  and (data[0:2] == "in"):
            QQ = False
            qq50 = 50
            musicstart()
            islightout = False
            anim.cleargb()
            p31.ChangeDutyCycle(0)
            p33.ChangeDutyCycle(0)
            p35.ChangeDutyCycle(0)
        elif len(data) == 2  and (data[0:2] == "qq"):
            QQ = True
            musicstart()
            islightout = False
            anim.cleargb()
        elif len(data) == 4  and (data[0:4] == "rgbw"):
            p31.ChangeDutyCycle(100)
            p33.ChangeDutyCycle(0)
            p35.ChangeDutyCycle(0)
            p37.ChangeDutyCycle(0)
            time.sleep(1)
            p31.ChangeDutyCycle(0)
            p33.ChangeDutyCycle(100)
            time.sleep(1)
            p33.ChangeDutyCycle(0)
            p35.ChangeDutyCycle(100)
            time.sleep(1)
            p35.ChangeDutyCycle(0)
            p37.ChangeDutyCycle(100)
            
def func():
    #global p13
    global qq50
    global QQ
    GPIO.output(13, True) #p13.ChangeDutyCycle(100)
    if False == QQ:
        p38.ChangeDutyCycle(0) #GPIO.output(38, False)
        p40.ChangeDutyCycle(qq50) #GPIO.output(40, True)

def musicend():
    global QQ
    if False == QQ:
        p38.ChangeDutyCycle(0) #GPIO.output(38, False)
        p40.ChangeDutyCycle(0) #GPIO.output(40, False)

def musicstart():
    global qq50
    p38.ChangeDutyCycle(0) #GPIO.output(38, False)
    p40.ChangeDutyCycle(qq50) #GPIO.output(40, True)
    
islightout = True
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", 6454))
ips = commands.getoutput("/sbin/ifconfig | grep -iA2 \"eth0\" | grep -i \"inet\" | grep -iv \"inet6\" | " +
                         "awk {'print $2'} | sed -ne 's/addr\://p'")
mylist = ips.split(".")
whoami = int(mylist[3])
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
p31 = GPIO.PWM(31, 200)
GPIO.output(13, True)
#p13 = GPIO.PWM(13, 1000)
p33 = GPIO.PWM(33, 200)
p35 = GPIO.PWM(35, 200)
p37 = GPIO.PWM(37, 200)
p38 = GPIO.PWM(38, 200)
p40 = GPIO.PWM(40, 200)
p31.start(0)
#p13.start(100)
p33.start(0)
p35.start(0)
p37.start(0)
p38.start(0)
p40.start(0)

coords = [
[43,44],[42,45],[41,46],[40,47],[39,48],[38,49],[37,50],[36,51],[35,52],[34,53],[33,54],[32,55],[31,56],
[30,57],[29,58],[28,59],[27,60],[26,61],[25,62],[24,63],[23,64],[22,65],[21,66],[20,67],[19,68],[18,69],
[17,70],[16,71],[15,72],[14,73],[13,74],[12,75],[11,76],[10,77],[9,78],[8,79],[7,80],[6,81],[5,82],[4,83],
[0,1],[2,3]
]
qq50 = 50
#coords = [
#[10,9],[11,8],[12,7],[13,6],[14,5],[15,4],[16,3],[17,2],[18,1],[19,0]
#]
QQ = False
#causes frame timing information to be output
rayled.log.setLogLevel(rayled.log.CRITICAL)
#set number of pixels & LED type here
driver = rayled.DriverLPD8806( num = len(coords[0]) * len(coords) , SPISpeed = 4 )
#load the LEDStrip class
led = rayled.LEDMatrix(driver, width = len(coords[0]), height = len(coords), coordMap = coords, threadedUpdate = True)
#load channel test animation
anim = rayled.ColorWipe(led, width = len(coords[0]))

timer = None  
sparksock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:        
    sparksock.bind(("0.0.0.0",9999))
    sparksock.listen(2)
    clientsocket, clientaddr = sparksock.accept()
    thread.start_new_thread(handler, (clientsocket, clientaddr))
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            if False == islightout:
                if data[0:4] == "RGBW":
                    mylist = data[4:].split(" ")
                    p31.ChangeDutyCycle(int(mylist[0])/2.55)
                    p33.ChangeDutyCycle(int(mylist[1])/2.55)
                    p35.ChangeDutyCycle(int(mylist[2])/2.55)
                    #for ii in range (0,160,4):
                    #    y = int(mylist[ii+3])
                    #    r = int(mylist[ii])
                    #    g = int(mylist[ii+1])
                    #    b = int(mylist[ii+2])
                    #    anim.drawone(0, y, r, g, b)
                    #    anim.drawone(1, y, r, g, b)
                elif data[0:4] == "COLD":
                    mylist = data[4:].split(" ")
                    p38.ChangeDutyCycle(int(mylist[0])/2.55) #GPIO.output(38, True)
                elif data[0:4] == "WARM":
                    mylist = data[4:].split(" ")
                    p40.ChangeDutyCycle(int(mylist[0])/2.55) #GPIO.output(40, False)
                    #if int(mylist[164]) > 0:
                    #    GPIO.output(13, False) #p13.ChangeDutyCycle(0)
                    #    Timer(0.333, qq).start()
            else:    
                if (len(data) > 8) and (data[0:8] == "Art-Net\x00"):
                    rawbytes = map(ord, data)
                    opcode = rawbytes[8] + (rawbytes[9] << 8)
                    protocolVersion = (rawbytes[10] << 8) + rawbytes[11]
                    if ((opcode == 0x5000) and (protocolVersion >= 14)):
                        #sequence = rawbytes[12]
                        #physical = rawbytes[13]
                        sub_net = (rawbytes[14] & 0xF0) >> 4
                        universe = rawbytes[14] & 0x0F
                        nowy = (sub_net << 4) + universe
                        #net = rawbytes[15]
                        rgb_length = (rawbytes[16] << 8) + rawbytes[17]
                        #print "seq %d phy %d sub_net %d uni %d net %d len %d" % (sequence, physical, sub_net, universe, net, rgb_length)
                        idx = 18
                        x = 1
                        y = nowy 
                        while ((idx < (rgb_length+18)) ): 
                            r = rawbytes[idx]
                            idx += 1
                            g = rawbytes[idx]
                            idx += 1
                            b = rawbytes[idx]
                            idx += 1
                            if x == whoami:
                                if 0 == y and False == QQ:
                                    p31.ChangeDutyCycle(int(r/2.55))
                                    p33.ChangeDutyCycle(int(g/2.55))
                                    p35.ChangeDutyCycle(int(b/2.55))
                                else:
                                    anim.drawone(x-whoami, y-1, r, g, b)
                                    anim.drawone(x-whoami+1, y-1, r, g, b)
                            #print (str(x) + ":" + str(y))
                            x += 1
                            #if (x >= 66):
                            #    x = 0
                            #    y += 1
                elif data[0:6] == "artnet" and len(data) > 6:
                    mylist = data[6:].split(" ")
                    for ii in range(0, len(mylist), 4):
                        r = int(mylist[ii])
                        g = int(mylist[ii+1])
                        b = int(mylist[ii+2])
                        y = int(mylist[ii+3])
                        if 0 == y and False == QQ:
                            p31.ChangeDutyCycle(int(r/2.55))
                            p33.ChangeDutyCycle(int(g/2.55))
                            p35.ChangeDutyCycle(int(b/2.55))
                        else:
                            anim.drawone(0, y, r, g, b)
                            anim.drawone(1, y, r, g, b)
                    

        except ValueError:
            pass    
        except IndexError:
            pass
                
except (KeyboardInterrupt):
    sock.close()
    sparksock.shutdown(2)
    sparksock.close()
    p31.stop()
    #p13.stop()
    p33.stop()
    p35.stop()
    p37.stop()
    p38.stop()
    p40.stop()
    GPIO.cleanup()
