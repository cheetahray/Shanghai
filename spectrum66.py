import socket
import sys
import commands
from time import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 33153)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

start_time = 0

while True:
    data, address = sock.recvfrom(4096)

    end_time = time()
    hours, rest = divmod(end_time,3600)
    mymin, seconds = divmod(rest, 60)
    mymin %= 30
    
    time_taken = end_time - start_time # time_taken is in seconds
    hours, rest = divmod(time_taken,3600)
    minutes, seconds = divmod(rest, 60)

    print "==>", data
    if data == "tss":
        pass #subprocess.call('/home/oem/Shanghai/closeJames.sh', shell=True)
    #elif mymin <= 5 or mymin >= 25:
    #    pass
    elif True: #minutes >= 5:
        commands.getoutput('/home/oem/' + data + '.sh')
        start_time = time()
