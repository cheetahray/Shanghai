import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 9999)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
red = 0
blue = 0
while True:
    #print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    
    #print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    mylist = address[0].split(".")
    if data == "@":
        if int(mylist[3]) % 2 == 0:
            red += 1
        else:
            blue += 1
        print >>sys.stderr, str(red) + ":" + str(blue)
    '''
    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
    '''
