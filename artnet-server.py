# Art-Net protocol for Pimoroni Unicorn Hat
# Open Pixel Control protocol for Pimoroni Unicorn Hat
# License: MIT
#import unicornhat as unicorn
from twisted.internet import protocol, endpoints
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

# Adjust the LED brightness as needed.
#unicorn.brightness(0.5)

class ArtNet(DatagramProtocol):

    __p31 = None
    __p32 = None
    __p33 = None
    __p35 = None
    __p37 = None
    __p38 = None
    __p40 = None

    def __init__(self)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(40, GPIO.OUT)
        self.__p31 = GPIO.PWM(31, 50)
        self.__p32 = GPIO.PWM(32, 50)
        self.__p33 = GPIO.PWM(33, 50)
        self.__p35 = GPIO.PWM(35, 50)
        self.__p37 = GPIO.PWM(37, 50)
        self.__p38 = GPIO.PWM(38, 50)
        self.__p40 = GPIO.PWM(40, 50)
        self.__p31.start(0)
        self.__p32.start(100)
        self.__p33.start(0)
        self.__p35.start(0)
        self.__p37.start(0)
        self.__p38.start(0)
        self.__p40.start(0)
        
    def datagramReceived(self, data, (host, port)):
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
                while ((idx < (rgb_length+18)) and (y < 8)):
                    r = rawbytes[idx]
                    idx += 1
                    g = rawbytes[idx]
                    idx += 1
                    b = rawbytes[idx]
                    idx += 1
                    print ("{0}, {1}, {2}, {3}, {4}".format(x, y, r, g, b) )  #unicorn.set_pixel(x, y, r, g, b)
                    x += 1
                    if (x > 7):
                        x = 0
                        y += 1
                #unicorn.show()
