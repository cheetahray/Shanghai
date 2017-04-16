from OSC import *
import subprocess
import time

server = OSCServer( ("0.0.0.0", 22222) )
server.timeout = 0
run = True

def handle_timeout(self):
    self.timed_out = True

server.handle_timeout = types.MethodType(handle_timeout, server)

def movie_callback(path, tags, args, source):
    if args[0] == 0:
        print "HighHighLowLow"
        lightinout(1)
    elif args[0] == 28:
        print "upup"
        upup()
    else:
        print "Animation"
        #lightinout(0)
        port.sendto(pack('B',args[0]), ("127.0.0.1",11111) )

def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

server.addMsgHandler( "/movie", movie_callback )

try:
    #Register the door bell button GPIO input call back function
    # simulate a "game engine"
    while run:
        # do the game stuff:
        #sleep(1)
        # call user script
        each_frame()

    server.close()

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 