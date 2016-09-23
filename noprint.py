import socket
import subprocess
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", 11111))
while True:
    data, addr = sock.recvfrom(1024)
    mydata = ord(data)
    if(mydata == 61):
        subprocess.call('./reart.sh w1.mov&', shell=True)
    elif(mydata == 62):
        subprocess.call('./reart.sh w2.mov&', shell=True)
    elif(mydata == 63):
        subprocess.call('./reart.sh w3.mov&', shell=True)
    elif(mydata == 64):
        subprocess.call('./reart.sh w4.mov&', shell=True)

    

