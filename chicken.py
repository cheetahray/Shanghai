import socket
import struct
from struct import *
from OSC import *
import time
cc = OSCClient()
cc.connect(('192.168.11.128', 7777))   # localhost, port 57120

def click(msg, val):
    global cc
    mymsg = "/" + msg
    oscmsg = OSCMessage()
    #print "%s" % (mymsg)
    oscmsg.setAddress("%s" % (mymsg) )
    oscmsg.append(val)
    cc.send(oscmsg)

port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#EMD8308 IP Port
thetuple = ("192.168.11.250", 6936)
#Listen port
#port.bind(("0.0.0.0", 6936))
mycmd = 0x59
while True:
    port.sendto( pack('15sb32b', 'EMA830812345678',mycmd,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), thetuple )
    #
    rcv, addr = port.recvfrom(1024)
    if( ord( rcv[33] ) == mycmd ):
        #print ("This Command")
        if( ord( rcv[32] ) == 0x63 ):
            #print ("successful")
            #for ii in range(8,12):
            #    print hex( ord( rcv[ii] ) ),
            bb = struct.unpack('>f', struct.pack('4B', ord(rcv[11]), ord(rcv[10]), ord(rcv[9]), ord(rcv[8])))
            print bb
            click("chicken" ,bb)
        else:
            print ("Fail")
            print ( hex ( ord ( rcv[32] )  ) )
    else:
        print ("Not this command")
    time.sleep(0.1)