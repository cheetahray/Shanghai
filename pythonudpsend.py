import socket
import sys
import time
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.4.1', 8888)
message = ['23','34','2','654','45','3452','45','6','78','90','768','67','879','97','657','45','5','435','65','87']
cnt = 0
try:

    for ii in message:
        # Send data
        print >>sys.stderr, 'sending "%s"' % ii
        sent = sock.sendto( ii, server_address)
        time.sleep(1)
        
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
