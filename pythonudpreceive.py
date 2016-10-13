import socket
import sys
import fluidsynth
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 8888)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

fs = fluidsynth.Synth()
fs.start('alsa')
sfid = fs.sfload("FluidR3_GM.sf2")
lasttype = 0
fs.pitch_bend(0, 512)
MayI = False
def whattype(typestr):
    global fs
    global sfid
    global lasttype
    chnl = typestr
    if chnl >= 10:
        chnl = 32
    elif chnl >= 8:
        chnl = 46
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
    fs.noteon(0, note, velo)

while True:
    #print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    #print data
    #mylist = data.split(" ")
    for ii in range(0, len(data), 4):
        if( data[ii] == 'n' ):
            if ord(data[ii+3]) == 1:
                print "preload"
                MayI = False
            elif ord(data[ii+3]) == 2:
                MayI = True
                threading.Timer( 0.3, playtwelve, [ord(data[ii+1]), ord(data[ii+2]), 127]).start()
            else:
                MayI = False
                threading.Timer( 1.2, playtwelve, [ord(data[ii+1]), ord(data[ii+2]), ord(data[ii+3])]).start()
        elif( data[ii] == 'f' ):
            if ord(data[ii+3]) == 2:
                threading.Timer( 0.3, fs.noteoff, [0, ord(data[ii+2])]).start()
            else:
                threading.Timer( 1.2, fs.noteoff, [0, ord(data[ii+2])]).start()
    '''
    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
    '''
