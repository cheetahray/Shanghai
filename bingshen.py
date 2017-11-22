import socket
import subprocess
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("0.0.0.0", 11111))
while True:
    playwhat, addr = sock.recvfrom(1024)
    if len(playwhat) > 0:
        if playwhat == 'up':
            sock.sendto("resound", ("192.168.12.255",11111))
        elif playwhat != 'resound':
            subprocess.call('/home/oem/Shanghai/reart.sh movie_' + str(ord(playwhat)) + '.mov&', shell=True)
    print "==>", playwhat
