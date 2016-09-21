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
    if 67 == oidx:
        oidx = 1
    if 3 == whattype:
        while 0 == BT[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
    elif 2 == whattype:
        while 0 == TT[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
    elif 1 == whattype:
        while 0 == AT[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
    elif 0 == whattype:
        while 0 == ST[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
    return oidx                
        
def play_midi():
    global isplay
    global myshift
    global port
    global boidx,toidx,aoidx,soidx
    #workbook = xlsxwriter.Workbook('demo.xlsx')
    #worksheet = workbook.add_worksheet()
    #f = []
    boundary = 0
    #port.flush()
        
    for i in range(1,67):
        port.sendto("249 3", ("192.168.12." + str(i), 5005) )
        time.sleep(0.01)
    time.sleep(4)
    for i in range(34,67):
        port.sendto("225 0", ("192.168.12." + str(i), 5005) )
        port.sendto("225 0", ("192.168.12." + str(67-i), 5005) )
        time.sleep(0.02)
        #f.append(0)
        #worksheet.write(i, 0, 0)
    for message in mid.play():  #Next note from midi in this moment
        isplay = False          #To avoid duplicate doorbell button press during midi play
        if True:
            if message.channel == 12 or (message.channel >= 4 and message.channel <= 7):
                if message.time < 0.1:
                    print(message)
        elif 'note_on' == message.type :
            if 0 == message.velocity:
                if message.channel == 3:
                    if pickidx[3].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[3][message.note]), ("192.168.12." + str(pickidx[3][message.note]), 5005) )
                        del pickidx[3][message.note]
                elif message.channel == 2:
                    if pickidx[2].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[2][message.note]), ("192.168.12." + str(pickidx[2][message.note]), 5005) )
                        del pickidx[2][message.note]
                elif message.channel == 1:
                    if pickidx[1].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[1][message.note]), ("192.168.12." + str(pickidx[1][message.note]), 5005) )
                        del pickidx[1][message.note]
                elif message.channel == 0:
                    if pickidx[0].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[0][message.note]), ("192.168.12." + str(pickidx[0][message.note]), 5005) )
                        del pickidx[0][message.note]
                elif message.channel == 11:
                    if pickidx[7].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[7][message.note]) + "\r")
                        del pickidx[7][message.note]
                    if pickidx[11].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[11][message.note]) + "\r")
                        del pickidx[11][message.note]
                elif message.channel == 10:
                    if pickidx[6].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[6][message.note]) + "\r")
                        del pickidx[6][message.note]
                    if pickidx[10].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[10][message.note]) + "\r")
                        del pickidx[10][message.note]
                elif message.channel == 9:
                    if pickidx[5].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[5][message.note]) + "\r")
                        del pickidx[5][message.note]
                    if pickidx[9].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[9][message.note]) + "\r")
                        del pickidx[9][message.note]
                elif message.channel == 8:
                    if pickidx[4].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[4][message.note]) + "\r")
                        del pickidx[4][message.note]
                    if pickidx[8].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[8][message.note]) + "\r")
                        del pickidx[8][message.note]
            else:
                if False:#message.channel == 7:
                    boidx = checkbound(3,boidx)
                    port.sendto("224 " + str(message.note) + " " + str(raymap(message.velocity, 0, 127, boundary, 127)) + " " + str(boidx) + "\r")
                    slideidx[3][message.note] = boidx
                    boidx += 1
                elif False:#message.channel == 6:
                    toidx = checkbound(2,toidx)
                    port.sendto("224 " + str(message.note) + " " + str(raymap(message.velocity, 0, 127, boundary, 127)) + " " + str(toidx) + "\r")
                    slideidx[2][message.note] = toidx
                    toidx += 1
                elif False:#message.channel == 5:
                    aoidx = checkbound(1,aoidx)
                    port.sendto("224 " + str(message.note) + " " + str(raymap(message.velocity, 0, 127, boundary, 127)) + " " + str(aoidx) + "\r")
                    slideidx[1][message.note] = aoidx
                    aoidx += 1
                elif False:#message.channel == 4:
                    soidx = checkbound(0,soidx)
                    port.sendto("224 " + str(message.note) + " " + str(raymap(message.velocity, 0, 127, boundary, 127)) + " " + str(soidx) + "\r")
                    slideidx[0][message.note] = soidx
                    soidx += 1
                elif message.channel == 3:
                    boidx = checkbound(3,boidx)
                    port.sendto("144 " + str(message.note) + " " + str(raymap(message.velocity, 0, 127, boundary, 127)) + " " + str(boidx) , ("192.168.12." + str(boidx), 5005) )
                    pickidx[3][message.note] = boidx
                    boidx += 1
                elif message.channel == 2:
                    toidx = checkbound(2,toidx)
                    port.sendto("144 " + str(message.note) + " " + str(raymap(message.velocity, 0, 127, boundary, 127)) + " " + str(toidx) , ("192.168.12." + str(toidx), 5005))
                    pickidx[2][message.note] = toidx
                    toidx += 1
                elif message.channel == 1:
                    aoidx = checkbound(1,aoidx)
                    port.sendto("144 " + str(message.note) + " " + str(raymap(message.velocity, 0, 127, boundary, 127)) + " " + str(aoidx) , ("192.168.12." + str(aoidx), 5005))
                    pickidx[1][message.note] = aoidx
                    aoidx += 1
                elif message.channel == 0:
                    soidx = checkbound(0,soidx)
                    port.sendto("144 " + str(message.note) + " " + str(raymap(message.velocity, 0, 127, boundary, 127)) + " " + str(soidx) , ("192.168.12." + str(soidx), 5005))
                    pickidx[0][message.note] = soidx
                    soidx += 1
                elif message.channel == 11:
                    rayv = raymap(message.velocity, 0, 127, boundary, 127)
                    boidx = checkbound(3,boidx)
                    port.sendto("144 " + str(message.note) + " " + str(rayv) + " " + str(boidx) , ("192.168.12." + str(boidx), 5005) )
                    pickidx[7][message.note] = boidx
                    boidx += 1
                    boidx = checkbound(3,boidx)
                    port.sendto("144 " + str(message.note) + " " + str(rayv) + " " + str(boidx) , ("192.168.12." + str(boidx), 5005) )
                    pickidx[11][message.note] = boidx
                    boidx += 1
                elif message.channel == 10:
                    rayv = raymap(message.velocity, 0, 127, boundary, 127)
                    toidx = checkbound(2,toidx)
                    port.sendto("144 " + str(message.note) + " " + str(rayv) + " " + str(toidx) , ("192.168.12." + str(toidx), 5005))
                    pickidx[6][message.note] = toidx
                    toidx += 1
                    toidx = checkbound(2,toidx)
                    port.sendto("144 " + str(message.note) + " " + str(rayv) + " " + str(toidx) , ("192.168.12." + str(toidx), 5005))
                    pickidx[10][message.note] = toidx
                    toidx += 1
                elif message.channel == 9:
                    rayv = raymap(message.velocity, 0, 127, boundary, 127)
                    aoidx = checkbound(1,aoidx)
                    port.sendto("144 " + str(message.note) + " " + str(rayv) + " " + str(aoidx) , ("192.168.12." + str(aoidx), 5005))
                    pickidx[5][message.note] = aoidx
                    aoidx += 1
                    aoidx = checkbound(1,aoidx)
                    port.sendto("144 " + str(message.note) + " " + str(rayv) + " " + str(aoidx) , ("192.168.12." + str(aoidx), 5005))
                    pickidx[9][message.note] = aoidx
                    aoidx += 1
                elif message.channel == 8:
                    rayv = raymap(message.velocity, 0, 127, boundary, 127)
                    soidx = checkbound(0,soidx)
                    port.sendto("144 " + str(message.note) + " " + str(rayv) + " " + str(soidx) , ("192.168.12." + str(soidx), 5005))
                    pickidx[4][message.note] = soidx
                    soidx += 1
                    soidx = checkbound(0,soidx)
                    port.sendto("144 " + str(message.note) + " " + str(rayv) + " " + str(soidx) , ("192.168.12." + str(soidx), 5005))
                    pickidx[8][message.note] = soidx
                    soidx += 1
        elif 'note_off' == message.type :
            if message.channel == 3:
                if pickidx[3].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[3][message.note]) , ("192.168.12." + str(pickidx[3][message.note]), 5005) )
                    del pickidx[3][message.note]
            elif message.channel == 2:
                if pickidx[2].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[2][message.note]) , ("192.168.12." + str(pickidx[2][message.note]), 5005) )
                    del pickidx[2][message.note]
            elif message.channel == 1:
                if pickidx[1].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[1][message.note]) , ("192.168.12." + str(pickidx[1][message.note]), 5005) )
                    del pickidx[1][message.note]
            elif message.channel == 0:
                if pickidx[0].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[0][message.note]) , ("192.168.12." + str(pickidx[0][message.note]), 5005) )
                    del pickidx[0][message.note]
            elif message.channel == 11:
                if pickidx[7].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[7][message.note]) , ("192.168.12." + str(pickidx[7][message.note]), 5005) )
                    del pickidx[7][message.note]
                if pickidx[11].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[11][message.note]) , ("192.168.12." + str(pickidx[11][message.note]), 5005) )
                    del pickidx[11][message.note]
            elif message.channel == 10:
                if pickidx[6].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[6][message.note]) , ("192.168.12." + str(pickidx[6][message.note]), 5005) )
                    del pickidx[6][message.note]
                if pickidx[10].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[10][message.note]) , ("192.168.12." + str(pickidx[10][message.note]), 5005) )
                    del pickidx[10][message.note]
            elif message.channel == 9:
                if pickidx[5].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[5][message.note]) , ("192.168.12." + str(pickidx[5][message.note]), 5005) )
                    del pickidx[5][message.note]
                if pickidx[9].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[9][message.note]) , ("192.168.12." + str(pickidx[9][message.note]), 5005) )
                    del pickidx[9][message.note]
            elif message.channel == 8:
                if pickidx[4].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[4][message.note]) , ("192.168.12." + str(pickidx[4][message.note]), 5005) )
                    del pickidx[4][message.note]
                if pickidx[8].has_key(message.note):
                    port.sendto("128 " + str(message.note) + " " + str(message.velocity) + " " + str(pickidx[8][message.note]) , ("192.168.12." + str(pickidx[8][message.note]), 5005) )
                    del pickidx[8][message.note]
    time.sleep(3);
    for i in range(66,33,-1):
        port.sendto("225 1", ("192.168.12." + str(i), 5005) )
        port.sendto("225 1", ("192.168.12." + str(67-i), 5005) )
        time.sleep(0.02)
    for i in range(1,67):
        if 1 == ST[i]:
            port.sendto("144 60 1", ("192.168.12." + str(i), 5005))
        if 1 == AT[i]:
            port.sendto("144 48 1", ("192.168.12." + str(i), 5005))
        if 1 == TT[i]:
            port.sendto("144 38 1", ("192.168.12." + str(i), 5005))
        if 1 == BT[i]:
            port.sendto("144 28 1", ("192.168.12." + str(i), 5005))
        time.sleep(0.02)
    time.sleep(3);
    for i in range(1,67):
        if 1 == ST[i]:
            port.sendto("144 60 0", ("192.168.12." + str(i), 5005))
        if 1 == AT[i]:
            port.sendto("144 48 0", ("192.168.12." + str(i), 5005))
        if 1 == TT[i]:
            port.sendto("144 38 0", ("192.168.12." + str(i), 5005))
        if 1 == BT[i]:
            port.sendto("144 28 0", ("192.168.12." + str(i), 5005))
        time.sleep(0.02)
    time.sleep(3);
    for i in range(1,67):
        port.sendto("249 2" , ("192.168.12." + str(i), 5005))
        time.sleep(0.01)
    
    #time.sleep(10)
    #for i in range(1,67):
        #port.sendto("Home", ("192.168.12." + str(i), 5005))        
    
     #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66
ST = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
AT = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
TT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0 ,0 ,0 ,0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1 ,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
soidx = 1
aoidx = 1
toidx = 1
boidx = 1
pickidx = [{},{},{},{},{},{},{},{},{},{},{},{}]
slideidx = [{},{},{},{},{},{},{},{},{},{},{},{}]
port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      
#port = serial.Serial("\\\\.\\COM7", baudrate=115200)
try:
    #port.flushInput()
    #port.flushOutput()

    whoami = "11"
    #Register the door bl button GPIO input call back function
    port.sendto(pack('BBB', 253, int(whoami),100), ("192.168.12." + whoami, 5005) )
    time.sleep(0.01)
    port.sendto(pack('BB', 225, 0), ("192.168.12." + whoami, 5005) )
    time.sleep(0.01)
    whattype = 'A'
    if True:
        for i in range(1,7):
            if whattype == 'S':
                port.sendto(pack('BBB', 144, 79, 127), ("192.168.12." + whoami, 5005))
            elif whattype == 'A':
                port.sendto(pack('BBB', 144, 67, 127), ("192.168.12." + whoami, 5005))
            elif whattype == 'T':
                port.sendto(pack('BBB', 144, 57, 127), ("192.168.12." + whoami, 5005))
            elif whattype == 'B':
                port.sendto(pack('BBB', 144, 47, 127), ("192.168.12." + whoami, 5005))
            time.sleep(2.5);
            if whattype == 'S':
                port.sendto(pack('BBB', 144, 79, 0), ("192.168.12." + whoami, 5005))
            elif whattype == 'A':
                port.sendto(pack('BBB', 144, 67, 0), ("192.168.12." + whoami, 5005))
            elif whattype == 'T':
                port.sendto(pack('BBB', 144, 57, 0), ("192.168.12." + whoami, 5005))
            elif whattype == 'B':
                port.sendto(pack('BBB', 144, 47, 0), ("192.168.12." + whoami, 5005))
            time.sleep(0.5);
            if whattype == 'S':
                port.sendto(pack('BBB', 144, 60, 127), ("192.168.12." + whoami, 5005))
            elif whattype == 'A':
                port.sendto(pack('BBB', 144, 48, 127), ("192.168.12." + whoami, 5005))
            elif whattype == 'T':
                port.sendto(pack('BBB', 144, 38, 127), ("192.168.12." + whoami, 5005))
            elif whattype == 'B':
                port.sendto(pack('BBB', 144, 28, 127), ("192.168.12." + whoami, 5005))
            time.sleep(2.5);
            if whattype == 'S':
                port.sendto(pack('BBB', 144, 60, 0), ("192.168.12." + whoami, 5005))
            elif whattype == 'A':
                port.sendto(pack('BBB', 144, 48, 0), ("192.168.12." + whoami, 5005))
            elif whattype == 'T':
                port.sendto(pack('BBB', 144, 38, 0), ("192.168.12." + whoami, 5005))
            elif whattype == 'B':
                port.sendto(pack('BBB', 144, 28, 0), ("192.168.12." + whoami, 5005))
            time.sleep(0.5);
    elif True:
        multi = True
        if whattype == 'B':
            if multi:
                for jj in range(1,2):
                    for ii in range(28,48):
                        port.sendto(pack('BBB', 144, ii, 127), ("192.168.12." + whoami, 5005))
                        time.sleep(2)
                        port.sendto(pack('BBB', 128, ii, 127), ("192.168.12." + whoami, 5005))
                        time.sleep(0.3)
            
            for jj in range(1):
                    
                if True:
                    port.sendto(pack('BBB', 144, 28, 127), ("192.168.12." + whoami, 5005))
                    time.sleep(2)
                    port.sendto(pack('BBB', 128, 28, 127), ("192.168.12." + whoami, 5005))
                    time.sleep(0.3)
        elif whattype == 'S':
            if multi:
                for jj in range(1,2):
                    for ii in range(60,80):
                        port.sendto(pack('BBB', 144, ii, 127), ("192.168.12." + whoami, 5005))
                        time.sleep(2)
                        port.sendto(pack('BBB', 128, ii, 127), ("192.168.12." + whoami, 5005))
                        time.sleep(0.3)
            
            for jj in range(1):
                    
                if True:
                    port.sendto(pack('BBB', 144, 60, 127), ("192.168.12." + whoami, 5005))
                    time.sleep(2)
                    port.sendto(pack('BBB', 128, 60, 127), ("192.168.12." + whoami, 5005))
                    time.sleep(0.3)
        elif whattype == 'A':
            if multi:
                for jj in range(1,2):
                    for ii in range(48,68):
                        port.sendto(pack('BBB', 144, ii, 127), ("192.168.12." + whoami, 5005))
                        time.sleep(2)
                        port.sendto(pack('BBB', 128, ii, 127), ("192.168.12." + whoami, 5005))
                        time.sleep(0.3)
            
            for jj in range(1):
                    
                if True:
                    port.sendto(pack('BBB', 144, 48, 127), ("192.168.12." + whoami, 5005))
                    time.sleep(2)
                    port.sendto(pack('BBB', 128, 48, 127), ("192.168.12." + whoami, 5005))
                    time.sleep(0.3)
        elif whattype == 'T':
            if multi:
                for jj in range(1,2):
                    for ii in range(38,58):
                        port.sendto(pack('BBB', 144, ii, 127), ("192.168.12." + whoami, 5005))
                        time.sleep(2)
                        port.sendto(pack('BBB', 128, ii, 127), ("192.168.12." + whoami, 5005))
                        time.sleep(0.3)
            
            for jj in range(1):
                    
                if True:
                    port.sendto(pack('BBB', 144, 38, 127), ("192.168.12." + whoami, 5005))
                    time.sleep(2)
                    port.sendto(pack('BBB', 128, 38, 127), ("192.168.12." + whoami, 5005))
                    time.sleep(0.3)
            
        time.sleep(1)
    elif True:    
        for i in range(1,67):
            port.sendto(pack('BB', 225, 0), ("192.168.12." + str(i), 5005) )
            time.sleep(0.001)
    elif True:
        parser = argparse.ArgumentParser()
        parser.add_argument("--song",
                             default="001", help="Midi file")
        args = parser.parse_args()
        mid = MidiFile(args.song + '.mid')
        play_midi()
    
    port.sendto(pack('BB', 225, 1), ("192.168.12." + whoami, 5005) )
    #port.flush()
    
except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
