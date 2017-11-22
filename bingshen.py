import socket
import subprocess
import time
from OSC import *

server = OSCServer( ("0.0.0.0", 6666) )
server.timeout = 0
run = True

def handle_timeout(self):
    self.timed_out = True

server.handle_timeout = types.MethodType(handle_timeout, server)

def movie_callback(path, tags, args, source):
    if True:
        print "Animation"
        #lightinout(0)
        port.sendto(pack('B',args[0]), ("127.0.0.1",11111) )

def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("0.0.0.0", 11111))

server.addMsgHandler( "/movie", movie_callback )

while run:
    each_frame()
		
server.close()