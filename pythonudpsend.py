import socket
import sys
import time
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.4.1', 8888)
message = 'Yes or No?'
cnt = 0
try:

    while True:
        # Send data
        print >>sys.stderr, 'sending "%d"' % cnt
        sent = sock.sendto(str(cnt), server_address)
        cnt = cnt + 1
        time.sleep(1)
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
