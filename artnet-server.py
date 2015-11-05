# Art-Net protocol for Pimoroni Unicorn Hat
# Open Pixel Control protocol for Pimoroni Unicorn Hat
# License: MIT
#import unicornhat as unicorn
import sys;sys.path.append(r'eclipse/plugins/org.python.pydev_4.4.0.201510052309/pysrc')
import pydevd;pydevd.settrace()

from twisted.internet import protocol, endpoints
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

# Adjust the LED brightness as needed.
#unicorn.brightness(0.5)

class ArtNet(DatagramProtocol):

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

reactor.listenUDP(6454, ArtNet())
reactor.run()
