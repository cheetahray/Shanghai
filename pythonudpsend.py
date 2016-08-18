import socket
import sys
import time
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.11.4', 9930)
message = ['23','34','2','654','45','3452','45','6','78','90','768','67','879','97','657','45','5','435','65','87']
cnt = 0
try:
    mycnt = 1
    while True:
        # Send data
        #print >>sys.stderr, 'sending "%s"' % ii
        print >>sys.stderr, mycnt
        sent = sock.sendto( str(mycnt), server_address)
        time.sleep(1)
        mycnt = mycnt + 1
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
