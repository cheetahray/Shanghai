#!/usr/bin/python
#+-+-+-+-+-+-+
#|d|a|c|.|t|w|
#+-+-+-+-+-+-+
#
# doorbell.py
# Read a button input to trigger midi play then do some GPIO outputs.
#
# Author : Digital Art Center, Taipei.
# Date   : 11/18/2014
import argparse
import time
import unittest
from mido import MidiFile
#import xlsxwriter
#import serial
import socket
from struct import *
import sys
import WConio
mid = None
debug = False        #Boolean for on/off our debug print 
isplay = False      #Boolean to judge whether the midi is playing


class Tests(unittest.TestCase):
    def test_0(self):   #Test play midi file
        play_midi();

def raymap(value, istart, istop, ostart, ostop):
    #wierd = ostart + (ostop - ostart) * (value - istart) / (istop - istart); 
    #print wierd
    return value#wierd

def checkbound(whattype, oidx):
    global ST,AT,TT,BT
    if 6 == oidx:
        oidx = 1
    if 3 == whattype:
        while 0 == BT[oidx]:
            if 5 == oidx:
                oidx = 1
            else:
                oidx += 1
    elif 2 == whattype:
        while 0 == TT[oidx]:
            if 5 == oidx:
                oidx = 1
            else:
                oidx += 1
    elif 1 == whattype:
        while 0 == AT[oidx]:
            if 5 == oidx:
                oidx = 1
            else:
                oidx += 1
    elif 0 == whattype:
        while 0 == ST[oidx]:
            if 5 == oidx:
                oidx = 1
            else:
                oidx += 1
    return oidx                
        
def play_midi():
    global isplay
    global myshift
    global port
    global boidx,toidx,aoidx,soidx
    global AmIPlay
    AmIPlay = True    
    boundary = 0
    #port.flush()
        
    for i in range(1,6):
        port.sendto(pack('BB', 249, 3), ("192.168.12." + str(i), 5005) )
        time.sleep(0.01)
    time.sleep(4)
    for i in range(1,6):
        port.sendto(pack('BB', 225, 0), ("192.168.12." + str(i), 5005) )
        time.sleep(0.02)
        #f.append(0)
        #worksheet.write(i, 0, 0)
    time.sleep(1)
    for message in mid.play():  #Next note from midi in this moment
        isplay = False          #To avoid duplicate doorbell button press during midi play
        if True:
            print(message)
        if 'note_on' == message.type :
            if 0 == message.velocity:
                rayv = pack('BBB', 144, message.note, 0)
                if message.channel == 3:
                    if pickidx[3].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[3][message.note]), 5005) )
                        del pickidx[3][message.note]
                elif message.channel == 2:
                    if pickidx[2].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[2][message.note]), 5005) )
                        del pickidx[2][message.note]
                elif message.channel == 1:
                    if pickidx[1].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[1][message.note]), 5005) )
                        del pickidx[1][message.note]
                elif message.channel == 0:
                    if pickidx[0].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[0][message.note]), 5005) )
                        del pickidx[0][message.note]
                elif message.channel == 11:
                    if pickidx[7].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[7][message.note]), 5005) )
                        del pickidx[7][message.note]
                    if pickidx[11].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[11][message.note]), 5005) )
                        del pickidx[11][message.note]
                elif message.channel == 10:
                    if pickidx[6].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[6][message.note]), 5005) )
                        del pickidx[6][message.note]
                    if pickidx[10].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[10][message.note]), 5005) )
                        del pickidx[10][message.note]
                elif message.channel == 9:
                    if pickidx[5].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[5][message.note]), 5005) )
                        del pickidx[5][message.note]
                    if pickidx[9].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[9][message.note]), 5005) )
                        del pickidx[9][message.note]
                elif message.channel == 8:
                    if pickidx[4].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[4][message.note]), 5005) )
                        del pickidx[4][message.note]
                    if pickidx[8].has_key(message.note):
                        port.sendto(rayv, ("192.168.12." + str(pickidx[8][message.note]), 5005) )
                        del pickidx[8][message.note]
            else:
                rayv = pack('BBB', 144, message.note, raymap(message.velocity, 0, 127, boundary, 127))
                if message.channel == 3:
                    boidx = checkbound(3,boidx)
                    port.sendto(rayv, ("192.168.12." + str(boidx), 5005) )
                    pickidx[3][message.note] = boidx
                    boidx += 1
                elif message.channel == 2:
                    toidx = checkbound(2,toidx)
                    port.sendto(rayv, ("192.168.12." + str(toidx), 5005))
                    pickidx[2][message.note] = toidx
                    toidx += 1
                elif message.channel == 1:
                    aoidx = checkbound(1,aoidx)
                    port.sendto(rayv, ("192.168.12." + str(aoidx), 5005))
                    pickidx[1][message.note] = aoidx
                    aoidx += 1
                elif message.channel == 0:
                    soidx = checkbound(0,soidx)
                    port.sendto(rayv, ("192.168.12." + str(soidx), 5005))
                    pickidx[0][message.note] = soidx
                    soidx += 1
                elif message.channel == 11:
                    boidx = checkbound(3,boidx)
                    port.sendto(rayv, ("192.168.12." + str(boidx), 5005) )
                    pickidx[7][message.note] = boidx
                    boidx += 1
                    boidx = checkbound(3,boidx)
                    port.sendto(rayv, ("192.168.12." + str(boidx), 5005) )
                    pickidx[11][message.note] = boidx
                    boidx += 1
                elif message.channel == 10:
                    toidx = checkbound(2,toidx)
                    port.sendto(rayv, ("192.168.12." + str(toidx), 5005))
                    pickidx[6][message.note] = toidx
                    toidx += 1
                    toidx = checkbound(2,toidx)
                    port.sendto(rayv, ("192.168.12." + str(toidx), 5005))
                    pickidx[10][message.note] = toidx
                    toidx += 1
                elif message.channel == 9:
                    aoidx = checkbound(1,aoidx)
                    port.sendto(rayv, ("192.168.12." + str(aoidx), 5005))
                    pickidx[5][message.note] = aoidx
                    aoidx += 1
                    aoidx = checkbound(1,aoidx)
                    port.sendto(rayv, ("192.168.12." + str(aoidx), 5005))
                    pickidx[9][message.note] = aoidx
                    aoidx += 1
                elif message.channel == 8:
                    soidx = checkbound(0,soidx)
                    port.sendto(rayv, ("192.168.12." + str(soidx), 5005))
                    pickidx[4][message.note] = soidx
                    soidx += 1
                    soidx = checkbound(0,soidx)
                    port.sendto(rayv, ("192.168.12." + str(soidx), 5005))
                    pickidx[8][message.note] = soidx
                    soidx += 1
        elif 'note_off' == message.type :
            rayv = pack('BBB', 128, message.note, message.velocity)
            if message.channel == 3:
                if pickidx[3].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[3][message.note]), 5005) )
                    del pickidx[3][message.note]
            elif message.channel == 2:
                if pickidx[2].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[2][message.note]), 5005) )
                    del pickidx[2][message.note]
            elif message.channel == 1:
                if pickidx[1].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[1][message.note]), 5005) )
                    del pickidx[1][message.note]
            elif message.channel == 0:
                if pickidx[0].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[0][message.note]), 5005) )
                    del pickidx[0][message.note]
            elif message.channel == 11:
                if pickidx[7].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[7][message.note]), 5005) )
                    del pickidx[7][message.note]
                if pickidx[11].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[11][message.note]), 5005) )
                    del pickidx[11][message.note]
            elif message.channel == 10:
                if pickidx[6].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[6][message.note]), 5005) )
                    del pickidx[6][message.note]
                if pickidx[10].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[10][message.note]), 5005) )
                    del pickidx[10][message.note]
            elif message.channel == 9:
                if pickidx[5].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[5][message.note]), 5005) )
                    del pickidx[5][message.note]
                if pickidx[9].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[9][message.note]), 5005) )
                    del pickidx[9][message.note]
            elif message.channel == 8:
                if pickidx[4].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[4][message.note]), 5005) )
                    del pickidx[4][message.note]
                if pickidx[8].has_key(message.note):
                    port.sendto(rayv, ("192.168.12." + str(pickidx[8][message.note]), 5005) )
                    del pickidx[8][message.note]
    time.sleep(3.5);
    for i in range(1,6):
        port.sendto(pack('BB', 225, 1), ("192.168.12." + str(i), 5005) )
        time.sleep(0.02)
    time.sleep(1)
    for i in range(1,6):
        if 1 == ST[i]:
            port.sendto(pack('BBB', 144, 60, 1), ("192.168.12." + str(i), 5005))
        if 1 == AT[i]:
            port.sendto(pack('BBB', 144, 48, 1), ("192.168.12." + str(i), 5005))
        if 1 == TT[i]:
            port.sendto(pack('BBB', 144, 38, 1), ("192.168.12." + str(i), 5005))
        if 1 == BT[i]:
            port.sendto(pack('BBB', 144, 28, 1), ("192.168.12." + str(i), 5005))
        time.sleep(0.02)
    time.sleep(3.5);
    for i in range(1,6):
        if 1 == ST[i]:
            port.sendto(pack('BBB', 144, 60, 0), ("192.168.12." + str(i), 5005))
        if 1 == AT[i]:
            port.sendto(pack('BBB', 144, 48, 0), ("192.168.12." + str(i), 5005))
        if 1 == TT[i]:
            port.sendto(pack('BBB', 144, 38, 0), ("192.168.12." + str(i), 5005))
        if 1 == BT[i]:
            port.sendto(pack('BBB', 144, 28, 0), ("192.168.12." + str(i), 5005))
        time.sleep(0.02)
    time.sleep(3.5);
    for i in range(1,6):
        port.sendto(pack('BB', 249, 2), ("192.168.12." + str(i), 5005))
        time.sleep(0.01)
    AmIPlay = False    
AmIPlay = False
     #0  1  2  3  4  5  
ST = [0, 1, 1, 1, 1, 1]
AT = [0, 0, 0, 0, 0, 0]
TT = [0, 0, 0, 0, 0, 0]
BT = [0, 0, 0, 0, 0, 0]
soidx = 1
aoidx = 1
toidx = 1
boidx = 1
pickidx = [{},{},{},{},{},{},{},{},{},{},{},{}]
slideidx = [{},{},{},{},{},{},{},{},{},{},{},{}]
port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      
#port = serial.Serial("\\\\.\\COM7", baudrate=115200)
try:
    while True:
        ans = WConio.getkey()
        print ans
        if AmIPlay == False:
            print ans
            parser = argparse.ArgumentParser()
            parser.add_argument("--song", default="TEST_1", help="Midi file")
            args = parser.parse_args()
            mid = MidiFile(args.song + '.mid')
            midi_suite = unittest.TestSuite()   #Add play midi test function
            all_suite = unittest.TestSuite()
            midi_suite.addTest(Tests("test_0"))
            all_suite.addTest(midi_suite)
            unittest.TextTestRunner(verbosity=1).run(all_suite)
        
except KeyboardInterrupt:
    print "Cleaning up the GPIO" 

