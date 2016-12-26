import socket
import subprocess
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", 11111))
while True:
    playwhat, addr = sock.recvfrom(1024)
    if len(playwhat) > 0:
        subprocess.call('./reart.sh movie_' + str(ord(playwhat)) + '.mov&', shell=True)
    print "==>", playwhat
