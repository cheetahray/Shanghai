# Art-Net protocol for Pimoroni Unicorn Hat
# Open Pixel Control protocol for Pimoroni Unicorn Hat
# License: MIT
import RPi.GPIO as GPIO
import socket
from threading import *

class ArtNet(Thread):

    __p31 = None
    __p32 = None
    __p33 = None
    __p35 = None
    __p37 = None
    __p38 = None
    __p40 = None
    __sock = None
    __UDP_PORT = 6454

    def __del__(self):
        self.__p31.stop()
        #self.__p32.stop()
        self.__p33.stop()
        self.__p35.stop()
        self.__p37.stop()
        self.__p38.stop()
        self.__p40.stop()
        GPIO.cleanup()

    def __init__(self):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.__sock.bind(("", self.__UDP_PORT))
        self.__sock.settimeout(0.04)    #fps = 25
        Thread.__init__(self)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(31, GPIO.OUT)
        #GPIO.setup(32, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(40, GPIO.OUT)
        self.__p31 = GPIO.PWM(31, 500)
        #self.__p32 = GPIO.PWM(32, 500)
        self.__p33 = GPIO.PWM(33, 500)
        self.__p35 = GPIO.PWM(35, 500)
        self.__p37 = GPIO.PWM(37, 500)
        self.__p38 = GPIO.PWM(38, 500)
        self.__p40 = GPIO.PWM(40, 500)
        self.__p31.start(0)
        #self.__p32.start(100)
        self.__p33.start(0)
        self.__p35.start(0)
        self.__p37.start(0)
        self.__p38.start(0)
        self.__p40.start(0)
        Thread.start(self)
        
    def run(self):
        while True:
            try:
                data, addr = self.__sock.recvfrom(1024)   
                if ((len(data) > 18) and (data[0:8] == "Art-Net\x00")):
                    rawbytes = map(ord, data)
                    opcode = rawbytes[8] + (rawbytes[9] << 8)
                    protocolVersion = (rawbytes[10] << 8) + rawbytes[11]
                    if ((opcode == 0x5000) and (protocolVersion >= 14)):
                        sequence = rawbytes[12]
                        physical = rawbytes[13]
                        sub_net = (rawbytes[14] & 0xF0) >> 4
                        universe = rawbytes[14] & 0x0F
                        net = rawbytes[15]
                        rgb_length = (rawbytes[16] << 8) + rawbytes[17]
                        #print "seq %d phy %d sub_net %d uni %d net %d len %d" % \
                        #(sequence, physical, sub_net, universe, net, rgb_length)
                        idx = 18
                        x = 0
                        y = 0
                        while ((idx < (rgb_length+18)) and (y < 21)):
                            r = rawbytes[idx]
                            idx += 1
                            g = rawbytes[idx]
                            idx += 1
                            b = rawbytes[idx]
                            idx += 1
                            if 0 == x and 0 == y:
                                self.__p31.ChangeDutyCycle(int(r/2.55))
                                self.__p33.ChangeDutyCycle(int(g/2.55))
                                self.__p35.ChangeDutyCycle(int(b/2.55))
                            else:
                                self.__sock.sendto( "{0} {1} {2} {3} {4}".format(x, y-1, r, g, b), ('127.0.0.1', 5005) ) #print >> self.__ww , "{0} {1} {2} {3} {4}".format(x, y-1, r, g, b)
                            x += 1
                            if (x >= 1):
                                x = 0
                                y += 1
            except socket.timeout:
                pass
