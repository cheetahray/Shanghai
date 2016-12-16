#socket library
import socket
#library
from struct import *
#socket
port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#EMD8308 IP Port
thetuple = ("192.168.11.250", 6936)
#Listen port
#port.bind(("0.0.0.0", 6936))
mycmd = 0x51
port.sendto( pack('15sb32b', 'EMA830812345678',mycmd,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), thetuple )
#
rcv, addr = port.recvfrom(1024)
if( ord( rcv[33] ) == mycmd ):
    print ("This Command")
    if( ord( rcv[32] ) == 0x63 ):
        print ("successful")
        for ii in range(0,34):
            print hex( ord( rcv[ii] ) ),
    else:
        print ("Fail")
        print ( hex ( ord ( rcv[32] )  ) )
else:
    print ("Not this command")
    