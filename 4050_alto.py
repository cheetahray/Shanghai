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

tp0 = [0, 2967, 5934, 8764, 11360, 13893, 16267, 18450, 20538, 22541, 24395, 26101, 27732, 29301, 30265, 32119, 33380, 34493, 35753, 36729, 37689]

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
