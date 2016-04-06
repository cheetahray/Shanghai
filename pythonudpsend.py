import socket
import sys
import time
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('172.1.0.3', 12345)
message = 'Yes or No?'

try:

    while True:
        # Send data
        print >>sys.stderr, 'sending "%s"' % message
        sent = sock.sendto(message, server_address)
        time.sleep(1)
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
