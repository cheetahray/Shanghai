#/usr/bin/python
#+-+-+-+-+-+-+
#|d|a|c|.|t|w|
#+-+-+-+-+-+-+
#
# doorbell.py
# Read a button input to trigger midi play then do some GPIO outputs.
#
# Author : Digital Art Center, Taipei.
# Date   : 11/18/2014
import argparse
import time
import threading
import socket
from OSC import *
from struct import *

server = OSCServer( ("0.0.0.0", 7777) )
server.timeout = 0.01
run = True

def handle_timeout(self):
    self.timed_out = True

server.handle_timeout = types.MethodType(handle_timeout, server)

debug = False        #Boolean for on/off our debug print 
pianoDELAY = 0.01
duration = 20

def do_callback(path, tags, args, source):
    threading.Timer( pianoDELAY, port.sendto, [pack('BH', 127, duration), ("192.168.1.255", 8888)]).start()
	
def re_callback(path, tags, args, source):
    threading.Timer( pianoDELAY, port.sendto, [pack('BH', 143, duration), ("192.168.1.255", 8888)]).start()
    
def mi_callback(path, tags, args, source):
    threading.Timer( pianoDELAY, port.sendto, [pack('BH', 159, duration), ("192.168.1.255", 8888)]).start()

def fa_callback(path, tags, args, source):
    threading.Timer( pianoDELAY, port.sendto, [pack('BH', 175, duration), ("192.168.1.255", 8888)]).start()
 
def so_callback(path, tags, args, source):
    threading.Timer( pianoDELAY, port.sendto, [pack('BH', 191, duration), ("192.168.1.255", 8888)]).start()
 
def la_callback(path, tags, args, source):
    threading.Timer( pianoDELAY, port.sendto, [pack('BH', 207, duration), ("192.168.1.255", 8888)]).start()
 
def ti_callback(path, tags, args, source):
    threading.Timer( pianoDELAY, port.sendto, [pack('BH', 223, duration), ("192.168.1.255", 8888)]).start()
 
def doo_callback(path, tags, args, source):
    threading.Timer( pianoDELAY, port.sendto, [pack('BH', 239, duration), ("192.168.1.255", 8888)]).start()

def quit_callback(path, tags, args, source):
    # don't do this at home (or it'll quit blender)
    global run
    run = False

# user script that's called by the game engine every frame
def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#port.sendto("127", ("192.168.13.249", 8888))
#time.sleep(2)
#port.sendto("143", ("192.168.13.249", 8888))
#time.sleep(2)

server.addMsgHandler( "/Do", do_callback )
server.addMsgHandler( "/Re", re_callback )
server.addMsgHandler( "/Mi", mi_callback )
server.addMsgHandler( "/Fa", fa_callback )
server.addMsgHandler( "/So", so_callback )
server.addMsgHandler( "/La", la_callback )
server.addMsgHandler( "/Ti", ti_callback )
server.addMsgHandler( "/Doo", doo_callback )

try:
    while run:
        # do the game stuff:
        #sleep(1)
        # call user script
        each_frame()

    server.close()

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
