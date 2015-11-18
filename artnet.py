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
            p32.ChangeDutyCycle(0)
            p38.ChangeDutyCycle(0)
            p40.ChangeDutyCycle(100)
            timer = Timer(0.1, func)
            timer.start()
        elif len(data) >= 3  and (data[0:3] == "out"):
            islightout = True
        elif len(data) >= 2  and (data[0:2] == "in"):
            islightout = False    

def func():
    global p32
    global p38
    global p40
    p32.ChangeDutyCycle(100)
    p38.ChangeDutyCycle(100)
    p40.ChangeDutyCycle(0)

islightout = True
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", 6454))
sparksock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sparksock.bind(("0.0.0.0",9999))
sparksock.listen(2)
clientsocket, clientaddr = sparksock.accept()
ips = commands.getoutput("/sbin/ifconfig | grep -iA2 \"wlan0\" | grep -i \"inet\" | grep -iv \"inet6\" | " +
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
p31 = GPIO.PWM(31, 1000)
p32 = GPIO.PWM(32, 1000)
p33 = GPIO.PWM(33, 1000)
p35 = GPIO.PWM(35, 1000)
p37 = GPIO.PWM(37, 1000)
p38 = GPIO.PWM(38, 1000)
p40 = GPIO.PWM(40, 1000)
p31.start(0)
p32.start(100)
p33.start(0)
p35.start(0)
p37.start(0)
p38.start(0)
p40.start(0)

coords = [
[64,59],[65,58],[66,57],[67,56],[68,55],[69,54],[70,53],[71,52],[72,51],[73,50],[74,49],[75,48],[76,47],[77,46],[78,45],[79,44],
[80,43],[81,42],[82,41],[83,40],[84,39],[85,38],[86,37],[87,36],[88,35],[89,34],[90,33],[91,32],[92,31],[93,30],[94,29],[95,28],
[96,27],[97,26],[98,25],[99,24],[100,23],[101,22],[102,21],[103,20],[104,19],[105,18],[106,17],[107,16],[108,15],[109,14],
[110,13],[111,12],[112,11],[113,10],[114,9],[115,8],[116,7],[117,6],[118,5],[119,4],[120,3],[121,2],[122,1],[123,0],[60,61],[62,63]
]

#coords = [
#[10,9],[11,8],[12,7],[13,6],[14,5],[15,4],[16,3],[17,2],[18,1],[19,0]
#]

#causes frame timing information to be output
rayled.log.setLogLevel(rayled.log.CRITICAL)
#set number of pixels & LED type here
driver = rayled.DriverLPD8806( num = len(coords[0]) * len(coords) )
#load the LEDStrip class
led = rayled.LEDMatrix(driver, width = len(coords[0]), height = len(coords), coordMap = coords, threadedUpdate = True)
#load channel test animation
anim = rayled.ColorWipe(led, width = len(coords[0]))

timer = None  
thread.start_new_thread(handler, (clientsocket, clientaddr))

try:        
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
                    if ( x == whoami - 78 ) or ( x == whoami - 77 ):
                        if 0 == nowy:
                            p31.ChangeDutyCycle(int(r/2.55))
                            p33.ChangeDutyCycle(int(g/2.55))
                            p35.ChangeDutyCycle(int(b/2.55))
                        else:
                            anim.drawone(x, nowy-1, r, g, b)
                            #sock.sendto( "{0} {1} {2} {3} {4}".format(x, nowy-1, r, g, b), ('127.0.0.1', 5005) ) 
                            #print "{0} {1} {2} {3} {4}".format(x, nowy-1, r, g, b)
                    x += 1
                    if (x >= 66):
                        x = 0
                        #y += 1
            
except (KeyboardInterrupt):
    p31.stop()
    p32.stop()
    p33.stop()
    p35.stop()
    p37.stop()
    p38.stop()
    p40.stop()
    GPIO.cleanup()
    sock.close()
    sparksock.close()
