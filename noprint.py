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

def user_callback(path, tags, args, source):
    # which user will be determined by path:
    # we just throw away all slashes and join together what's left
    #user = ''.join(path.split("/"))
    # tags will contain 'fff'
    # args is a OSCMessage with data
    # source is where the message came from (in case you need to reply)
    playwhat = ""
	if 0 == args[0]:
       playwhat = "" 
    elif 1 == args[0]:
       playwhat = ""
    elif 2 == args[0]:
       playwhat = ""
    elif 3 == args[0]:
       playwhat = ""
    elif 4 == args[0]:
       playwhat = ""
    elif 5 == args[0]:
       playwhat = ""
    elif 6 == args[0]:
       playwhat = ""
    elif False: #7 == args[0]:
       playwhat = ""
    elif -1 == args[0]:
       playwhat = ""
    
	subprocess.call('./reart.sh ' + playwhat + '.mov&', shell=True)
    print "==>", playwhat
    
    #print ("Now do something with", user,args[2],args[0],1-args[1]) 

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
		
try:
    while run:
        each_frame()

    server.close()

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 