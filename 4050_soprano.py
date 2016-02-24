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

tp0 = [0, 2721, 5749, 8595, 11363, 13749, 16024, 18312, 20435, 22386, 24121, 25918, 27536, 29164, 30471, 31981, 33227, 34493, 35620, 36806, 37689]

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
