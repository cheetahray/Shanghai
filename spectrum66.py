import socket
import sys
import subprocess
import time
import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 33153)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    now = datetime.datetime.now()
    mymin = (now.minute % 30)
    data, address = sock.recvfrom(4096)
    print "==>", data
    if data == "tss":
        pass #subprocess.call('./closeJames.sh', shell=False)
    elif mymin < 4:
        pass
    else:
        subprocess.call('../' + data + '.sh', shell=True)
        time.sleep(240)
