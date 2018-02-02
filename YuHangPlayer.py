from mido import MidiFile
import socket
from struct import *
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      
sock.settimeout(0.001)
thetuple = ("192.168.11.217", 6936)

def HotSpring(port, point ,state):
    mycmd = 0x38
    sock.sendto( pack('15sb32b', 'EMD821612345678',mycmd, port, point, state,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), thetuple )
    #
    try:
        rcv, addr = sock.recvfrom(1024)
        if( ord( rcv[33] ) == mycmd ):
            #print ("This Command")
            if( ord( rcv[32] ) == 0x63 ):
                print ("successful")
            else:
                print ("Fail")
                print ( hex ( ord ( rcv[32] )  ) )
        else:
            print ("Not this command")
    except socket.timeout, e:
        print e
    
for msg in MidiFile('sky.mid').play():
    print msg
    if msg.type == 'note_on':
        if 0 == msg.velocity:
            HotSpring(0, msg.note, 0)
        else:
            HotSpring(0, msg.note, 1) 
    elif msg.type == 'note_off':
        HotSpring(0, msg.note, 0)