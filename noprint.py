import socket
import subprocess
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", 11111))
while True:
    data, addr = sock.recvfrom(1024)
    mydata = ord(data)
    playwhat = ""
    if(mydata == 60):
        playwhat = "Sp1"
    elif(mydata == 61):
        playwhat =  "w1"
    elif(mydata == 62):
        playwhat =  "w2"
    elif(mydata == 63):
        playwhat =  "w3"
    elif(mydata == 64):
        playwhat =  "w4"
    elif(mydata == 65):
        playwhat = "At1"
    elif(mydata == 66):
        playwhat = "At2"
    elif(mydata == 67):
        playwhat = "At3"
    if len(playwhat) > 0:
        subprocess.call('./reart.sh ' + playwhat + '.mov&', shell=True)
        print "==>", playwhat
    
