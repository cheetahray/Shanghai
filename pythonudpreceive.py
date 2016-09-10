import socket
import sys
import fluidsynth
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 9999)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

fs = fluidsynth.Synth()
fs.start('coreaudio')
sfid = fs.sfload("FluidR3_GM.sf2")
lasttype = 0

def whattype(typestr):
    global fs
    global sfid
    global lasttype
    chnl = int(typestr)
    if chnl >= 10:
        chnl = 32
    elif chnl >= 8:
        chnl = 105
    elif chnl >= 2:
        chnl = 32
    else:
        chnl = 46 
    if lasttype != chnl:
        #print chnl
        fs.program_select(0, sfid, 0, chnl)
        lasttype = chnl

def playtwelve(chnl, note, velo):
    global fs
    whattype(chnl)
    #print note, velo
    fs.noteon(0, int(note), int(velo))

while True:
    #print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    #print data
    mylist = data.split(" ")
    print mylist
    if( mylist[0] == "n" ):
        if mylist[3] == "1":
            print "preload"
        elif mylist[3] == "2":
            #whattype(mylist[1])
            #fs.noteon(0, int(mylist[2]), 127)
            threading.Timer( 0.3, playtwelve, [mylist[1], mylist[2], 127]).start()
        else:
            #whattype(mylist[1])
            #fs.noteon(0, int(mylist[2]), int(mylist[3]))
            threading.Timer( 1.2, playtwelve, [mylist[1], mylist[2], mylist[3]]).start()
    elif( mylist[0] == "f" ):
        #fs.noteoff(0, int(mylist[2]))
        threading.Timer( 1.2, fs.noteoff, [0, int(mylist[2])]).start()
    '''
    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
    '''
