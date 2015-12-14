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
    while 1:
        data = clientsocket.recv(1024)
        if ( len(data) >= 6  and (data[0:6] == "picker") ):
            #print ("Boom")
            if True == islightout and len(data) != 6:
                mylist = data[6:].split(" ")
                #print(mylist)
                anim.rayanim(255,255,255,127,int(mylist[0]),float(mylist[1]))
            GPIO.output(32, False) #p32.ChangeDutyCycle(0)
            p38.ChangeDutyCycle(0)
            p40.ChangeDutyCycle(100)
            timer = Timer(0.1, func)
            timer.start()
        elif len(data) >= 3  and (data[0:3] == "out"):
            islightout = True
        elif len(data) >= 2  and (data[0:2] == "in"):
            islightout = False    

def func():
    #global p32
    global p38
    global p40
    GPIO.output(32, True) #p32.ChangeDutyCycle(100)
    p38.ChangeDutyCycle(100)
    p40.ChangeDutyCycle(0)

islightout = True
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", 6454))
ips = commands.getoutput("/sbin/ifconfig | grep -iA2 \"eth0\" | grep -i \"inet\" | grep -iv \"inet6\" | " +
                         "awk {'print $2'} | sed -ne 's/addr\://p'")
mylist = ips.split(".")
whoami = int(mylist[3])
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
p31 = GPIO.PWM(31, 200)
#p32 = GPIO.PWM(32, 1000)
p33 = GPIO.PWM(33, 200)
p35 = GPIO.PWM(35, 200)
p37 = GPIO.PWM(37, 200)
p38 = GPIO.PWM(38, 200)
p40 = GPIO.PWM(40, 200)
p31.start(0)
#p32.start(100)
p33.start(0)
p35.start(0)
p37.start(0)
p38.start(0)
p40.start(0)

coords = [
[39,40],[38,41],[37,42],[36,43],[35,44],[34,45],[33,46],[32,47],[31,48],[30,49],[29,50],[28,51],[27,52],
[26,53],[25,54],[24,55],[23,56],[22,57],[21,58],[20,59],[19,60],[18,61],[17,62],[16,63],[15,64],[14,65],
[13,66],[12,67],[11,68],[10,69],[9,70],[8,71],[7,72],[6,73],[5,74],[4,75],[3,76],[2,77],[1,78],[0,79]
]

#coords = [
#[10,9],[11,8],[12,7],[13,6],[14,5],[15,4],[16,3],[17,2],[18,1],[19,0]
#]

#causes frame timing information to be output
rayled.log.setLogLevel(rayled.log.CRITICAL)
#set number of pixels & LED type here
driver = rayled.DriverLPD8806( num = len(coords[0]) * len(coords) , SPISpeed = 4)
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
        data, addr = sock.recvfrom(1024)   
        if True == islightout and ((len(data) > 18) and (data[0:8] == "Art-Net\x00")):
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
                x = 0
                #y = 0
                while ((idx < (rgb_length+18)) ): #and ( y < 21 )):
                    r = rawbytes[idx]
                    idx += 1
                    g = rawbytes[idx]
                    idx += 1
                    b = rawbytes[idx]
                    idx += 1
                    if ( x == whoami - 179 ) or ( x == whoami - 178 ):
                        if 0 == nowy:
                            p31.ChangeDutyCycle(int(r/2.55))
                            p33.ChangeDutyCycle(int(g/2.55))
                            p35.ChangeDutyCycle(int(b/2.55))
                        else:
                            anim.drawone(x, nowy-1, r, g, b)
                            #sock.sendto( "{0} {1} {2} {3} {4}".format(x, nowy-1, r, g, b), ('127.0.0.1', 5005) ) 
                            #print "{0} {1} {2} {3} {4}".format(x, nowy-1, r, g, b)
                    x += 1
                    if (x >= 132):
                        x = 0
                        #y += 1
            
except (KeyboardInterrupt):
    sock.close()
    sparksock.shutdown(2)
    sparksock.close()
    p31.stop()
    #p32.stop()
    p33.stop()
    p35.stop()
    p37.stop()
    p38.stop()
    p40.stop()
    GPIO.cleanup()
