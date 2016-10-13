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

port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

while True:
    ts_cmd = raw_input('Send to T-Step--> ')
    print ts_cmd
    port.write("\r\n")
    port.write(ts_cmd + "\r\n")
    rcv=readlineCR(port)
    print rcv
    port.flush()
