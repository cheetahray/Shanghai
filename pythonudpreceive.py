import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 9999)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    #print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    mylist = data.split(" ")
    #print mylist
    if( mylist[0] == "n" ):
        if mylist[3] == "1":
            print "preload"
        elif mylist[3] == "2":
            print "aa"
        else:
            print "on"
    elif( mylist[0] == "f" ):
        print "off"
    '''
    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
    '''
