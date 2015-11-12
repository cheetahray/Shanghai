# Art-Net protocol for Pimoroni Unicorn Hat
# Open Pixel Control protocol for Pimoroni Unicorn Hat
# License: MIT
import RPi.GPIO as GPIO
import socket
import time
import commands
import ledstrip
from threading import *
import sys

def func():
    global p32
    p32.ChangeDutyCycle(100)

UDP_PORT = 6454

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))
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
p31 = GPIO.PWM(31, 5000)
p32 = GPIO.PWM(32, 5000)
p33 = GPIO.PWM(33, 5000)
p35 = GPIO.PWM(35, 5000)
p37 = GPIO.PWM(37, 5000)
p38 = GPIO.PWM(38, 5000)
p40 = GPIO.PWM(40, 5000)
p31.start(0)
p32.start(100)
p33.start(0)
p35.start(0)
p37.start(0)
p38.start(0)
p40.start(0)

#causes frame timing information to be output
ledstrip.log.setLogLevel(ledstrip.log.CRITICAL)
#set number of pixels & LED type here
driver = ledstrip.DriverLPD8806(num = 20)
#load the LEDStrip class
led = ledstrip.LEDStrip(driver, threadedUpdate = True)
#load channel test animation
anim = ledstrip.ColorWipe(led)

timer = None  

try:        
    while True:
        data, addr = sock.recvfrom(1024)   
        if ((len(data) > 18) and (data[0:8] == "Art-Net\x00")):
            rawbytes = map(ord, data)
            opcode = rawbytes[8] + (rawbytes[9] << 8)
            protocolVersion = (rawbytes[10] << 8) + rawbytes[11]
            if ((opcode == 0x5000) and (protocolVersion >= 14)):
                sequence = rawbytes[12]
                physical = rawbytes[13]
                sub_net = (rawbytes[14] & 0xF0) >> 4
                universe = rawbytes[14] & 0x0F
                nowy = (sub_net << 4) + universe
                net = rawbytes[15]
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
                    if ( x == whoami - 78 ):
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
        elif ( len(data) >= 6  and (data[0:6] == "picker") ):
            if len(data) != 6: 
                mylist = data[6:].split(" ")
                #print(mylist)
                anim.rayanim(255,255,255,255,int(mylist[0]),float(mylist[1]))
            p32.ChangeDutyCycle(0)
            timer = Timer(0.1, func)
            timer.start()
            
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
