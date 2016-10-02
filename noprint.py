import socket
import subprocess
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", 11111))
while True:
    data, addr = sock.recvfrom(1024)
    mydata = ord(data)
    playwhat = ""
    if(mydata == 1):
        playwhat = "back"
    elif(mydata == 4):
        playwhat = "y"
    elif(mydata == 31):
        playwhat = "m0"
    elif(mydata == 36):
        playwhat = "sky01"
    elif(mydata == 40):
        playwhat = "white_1"
    elif(mydata == 43):
        playwhat = "m1"
    elif(mydata == 48):
        playwhat = "sky02"
    elif(mydata == 55):
        playwhat = "m1"
    elif(mydata == 57):
        playwhat = "green_2"
    elif(mydata == 58):
        playwhat = "red"
    elif(mydata == 60):
        playwhat = "Sp1"
    elif(mydata == 61):
        playwhat =  "w1"
    elif(mydata == 62):
        playwhat =  "w1"
    elif(mydata == 63):
        playwhat =  "w3"
    elif(mydata == 64):
        playwhat =  "w4"
    elif(mydata == 65):
        playwhat = "C1"
    elif(mydata == 66):
        playwhat = "C2"
    elif(mydata == 67):
        #playwhat = "C3"
        playwhat = "m3"
    elif(mydata == 68):
        playwhat = "Sm1"
    elif(mydata == 69):
        playwhat = "Sm2"
    elif(mydata == 70):
        playwhat = "Sm3"
    elif(mydata == 71):
        playwhat = "B3"
    elif(mydata == 72):
        playwhat = "W5"
    elif(mydata == 79):
        playwhat = "m4"
    elif(mydata == 110):
        playwhat = "p"
    if len(playwhat) > 0:
        subprocess.call('./reart.sh ' + playwhat + '.mov&', shell=True)
        print "==>", playwhat
    
