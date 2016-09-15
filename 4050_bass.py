#! /usr/bin/env python

import serial
import time
def readlineCR(port):
        rv = ""
        while True:
                ch = port.read()
                if ch=='\n' or ch=='':
                        return rv
                rv += ch

port = serial.Serial("/dev/ttyAMA0", baudrate=57600, timeout=3.0)

tp0 = [0, 2742, 6230, 9007, 11267, 13785, 16308, 18534, 20399, 22252, 24186, 25889, 27596, 29150, 30484, 31816, 33297, 34383, 35487, 36524, 37689]

for i in range(0,len(tp0)):
    ts_cmd = "#ATS" + str(i) + "," + str(tp0[i])
    port.write("\r\n")
    port.write(ts_cmd + "\r\n")
    rcv=readlineCR(port)
    print rcv
    port.flush()
    time.sleep(0.5)

port.write("\r\n")
port.write("#ASD\r\n")
rcv=readlineCR(port)
print rcv
port.flush()
