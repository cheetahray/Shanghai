import socket
import sys
import time
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.11.60', 5000)
message = ['p1on','p1off']
try:
    mycnt = 0
    while True:
        # Send data
        #print >>sys.stderr, 'sending "%s"' % ii
        print >>sys.stderr, mycnt
        sent = sock.sendto( message[mycnt], server_address)
        time.sleep(2)
        if 0 == mycnt:
            mycnt = 1
        else:
            mycnt = 0
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
