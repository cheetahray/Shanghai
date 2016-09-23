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
import sys
import threading
import thread
import tty
import datetime
import subprocess
from select import select
import random
import commands
from struct import *
import OSC
import threading
mid = None
debug = False        #Boolean for on/off our debug print 
cc = OSC.OSCClient()
cc.connect(('192.168.12.212', 53000))   # localhost, port 57120

def click(mmsg,msg2):
    global cc
    oscmsg = OSC.OSCMessage()
    print "%s%s%c%s" % ("/cue/", mmsg, '/', msg2)
    oscmsg.setAddress("%s%s%c%s" % ("/cue/", mmsg, '/', msg2) )
    #oscmsg.append(mmsg)
    cc.send(oscmsg)

class Tests(unittest.TestCase):
    def test_0(self):   #Test play midi file
        play_midi();

def raymap(value, istart, istop, ostart, ostop):
    #wierd = ostart + (ostop - ostart) * (value - istart) / (istop - istart); 
    #print wierd
    return value#wierd

def checkbound(whattype, oidx):
    global ST,AT,TT,BT
    #if 67 == oidx:
    #    oidx = 1
    if 3 == whattype:
        tmp = BT.index(oidx)
        if tmp == len(BT) - 1:
            oidx = BT[0]
        else:
            oidx = BT[tmp + 1]
        '''
        while 0 == BT[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
        '''
    elif 2 == whattype:
        tmp = TT.index(oidx)
        if tmp == len(TT) - 1:
            oidx = TT[0]
        else:
            oidx = TT[tmp + 1]
        '''
        while 0 == TT[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
        '''
    elif 1 == whattype:
        tmp = AT.index(oidx)
        if tmp == len(AT) - 1:
            oidx = AT[0]
        else:
            oidx = AT[tmp + 1]
        '''
        while 0 == AT[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
        '''
    elif 0 == whattype:
        tmp = ST.index(oidx)
        if tmp == len(ST) - 1:
            oidx = ST[0]
        else:
            oidx = ST[tmp + 1]
        '''
        while 0 == ST[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
        '''
    return oidx                

def soundonoff(opensound):
    if opensound == True:
        for i in range(1,67):
            port2.sendto(pack('BB', 249, 3), ("%s%d" % ("192.168.12.", i), 5005) )
            #time.sleep(0.002)
    else:
        for i in range(1,67):
            port2.sendto(pack('BB', 249, 2), ("%s%d" % ("192.168.12.", i), 5005))
            #time.sleep(0.002)
    #time.sleep(4)

def changemusic(tp):
                # 1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
    soundtype = [tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, 32, 32, 32,
                 32, 32, 32, 32, 32, 32, 32, 32, 32, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, 32, 
                 32, 32, 32, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, tp, 
                 tp, tp, tp, 32, 32, 32, 32, 32, 32, tp, tp, tp, tp, 32]
    for i in range(1,67):
        port2.sendto( pack('BBB', 249, 1, soundtype[i]), ("%s%d" % ("192.168.12.", i), 5005) )
    #time.sleep(4)

def lightinout(lightin):
    global nowisin
    if nowisin == False and lightin == True:
        for i in range(1,67):
            port2.sendto( pack('BB', 225, 0), ("%s%d" % ("192.168.12.", i), 5005) )
            subprocess.call('./closeart.sh', shell=True)
            #port.sendto("225 0", ("%s%d" % ("192.168.12.", 67-i), 5005) )
    elif nowisin == True and lightin == False:
        for i in range(66,0,-1):
            port2.sendto( pack('BB', 225, 1), ("%s%d" % ("192.168.12.", i), 5005) )
            #port.sendto("225 1", ("%s%d" % ("192.168.12.", 67-i), 5005) )
    nowisin = lightin

def BoomBoom(rayrandom, myType):
    global nowisboom
    if True == nowisboom:
        pass
    else:
        nowisboom = True
        pixel = (rayrandom << 9)
        red_value = (pixel & 0xF800) >> 11;
        green_value = (pixel & 0x7E0) >> 5;
        blue_value = (pixel & 0x1F);
        red   = red_value << 3;
        green = green_value << 2;
        blue  = blue_value << 3;
        BOOM = pack('4sBBBBBB', "boom" ,red, green, blue, int(red/2.55), int(green/2.55), int(blue/2.55) )
        #print BOOM
        if myType == 0:
            for i in range(1,67):
                port4.sendto(BOOM, ("%s%d" % ("192.168.12.", i), 6454))
        elif myType == 1:
            for i in range(1,67):
                threading.Timer(0.01*i, port4.sendto, [BOOM, ("%s%d" % ("192.168.12.", i), 6454) ])
        elif myType == 2:
            for i in range(67,1):
                threading.Timer(0.01*i, port4.sendto, [BOOM, ("%s%d" % ("192.168.12.", i), 6454) ])
        elif myType == 3:
            for i in range(34,67):
                threading.Timer(0.02*i, port4.sendto, [BOOM, ("%s%d" % ("192.168.12.", i), 6454) ])
                threading.Timer(0.02*i, port4.sendto, [BOOM, ("%s%d" % ("192.168.12.", 67-i), 6454) ])
        elif myType == 4:
            for i in range(34,67):
                threading.Timer(0.02*i, port4.sendto, [BOOM, ("%s%d" % ("192.168.12.", i), 6454) ])
                threading.Timer(0.02*i, port4.sendto, [BOOM, ("%s%d" % ("192.168.12.", 67-i), 6454) ])
        elif myType == 5:
            for i in range(66,33,-1):
                threading.Timer(0.02*i, port4.sendto, [BOOM, ("%s%d" % ("192.168.12.", i), 6454) ])
                threading.Timer(0.02*i, port4.sendto, [BOOM, ("%s%d" % ("192.168.12.", 67-i), 6454) ])
        nowisboom = False

def readyplay(midstr):
    global mid
    #lightinout(True)
    soundonoff(True)
    #time.sleep(0.5)
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    parser.add_argument("--song",default=midstr, help="Midi file")
    args = parser.parse_args()
    mid = MidiFile(args.song)
    thread.start_new_thread(play_midi,())
    #midi_suite = unittest.TestSuite()   #Add play midi test function
    #all_suite = unittest.TestSuite()
    #midi_suite.addTest(Tests("test_0"))
    #all_suite.addTest(midi_suite)
    #unittest.TextTestRunner(verbosity=1).run(all_suite)
        
def play_midi():
    global myshift
    global port
    global boidx,toidx,aoidx,soidx
    #workbook = xlsxwriter.Workbook('demo.xlsx')
    #worksheet = workbook.add_worksheet()
    #f = []
    boundary = 0
    #port.flush()
    global AmIPlay
    AmIPlay = True    
    global waitforkey
    psidx = 0
    paidx = 0
    ptidx = 0
    pbidx = 0
    howmanyPreload = 0
    howmanyAA = 0
    mayIpreload = False
    totaltime = 0.0
    global mqueue
    noteoffaa = []
    for message in mid.play():  #Next note from midi in this moment
        msg = ""
        if 'note_on' == message.type :
            if message.channel == 14:
                if 3 == message.velocity:
                    psidx = soidx
                    paidx = aoidx
                    ptidx = toidx
                    pbidx = boidx
                    mayIpreload = True
                    howmanyPreload = 0
                    print("pulse")                    
                    #print datetime.datetime.now()
                    #lightinout(False)
                elif 5 == message.velocity:
                    soidx = psidx
                    aoidx = paidx
                    toidx = ptidx
                    boidx = pbidx
                    mayIpreload = False
                    howmanyAA = 0
                    print("resound")
                    waitforkey = True;
                    #print datetime.datetime.now()
                    while True == waitforkey:
                        time.sleep(0.002)
            elif 0 == message.velocity:
                msg = "f"
                if message.channel == 3:
                    if pickidx[3].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[3][message.note]), ("%s%d" % ("192.168.12.", pickidx[3][message.note]), 5005) )
                        del pickidx[3][message.note]
                elif message.channel == 2:
                    if pickidx[2].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[2][message.note]), ("%s%d" % ("192.168.12.", pickidx[2][message.note]), 5005) )
                        del pickidx[2][message.note]
                elif message.channel == 1:
                    if pickidx[1].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[1][message.note]), ("%s%d" % ("192.168.12.", pickidx[1][message.note]), 5005) )
                        del pickidx[1][message.note]
                elif message.channel == 0:
                    if pickidx[0].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[0][message.note]), ("%s%d" % ("192.168.12.", pickidx[0][message.note]), 5005) )
                        del pickidx[0][message.note]
                elif message.channel == 11:
                    if pickidx[7].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[7][message.note]), ("%s%d" % ("192.168.12.", pickidx[7][message.note]), 5005) )
                        del pickidx[7][message.note]
                    if pickidx[11].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[11][message.note]), ("%s%d" % ("192.168.12.", pickidx[11][message.note]), 5005) )
                        del pickidx[11][message.note]
                elif message.channel == 10:
                    if pickidx[6].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[6][message.note]), ("%s%d" % ("192.168.12.", pickidx[6][message.note]), 5005) )
                        del pickidx[6][message.note]
                    if pickidx[10].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[10][message.note]), ("%s%d" % ("192.168.12.", pickidx[10][message.note]), 5005) )
                        del pickidx[10][message.note]
                elif message.channel == 9:
                    if pickidx[5].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[5][message.note]), ("%s%d" % ("192.168.12.", pickidx[5][message.note]), 5005) )
                        del pickidx[5][message.note]
                    if pickidx[9].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[9][message.note]), ("%s%d" % ("192.168.12.", pickidx[9][message.note]), 5005) )
                        del pickidx[9][message.note]
                elif message.channel == 8:
                    if pickidx[4].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[4][message.note]), ("%s%d" % ("192.168.12.", pickidx[4][message.note]), 5005) )
                        del pickidx[4][message.note]
                    if pickidx[8].has_key(message.note):
                        #port.sendto("%s%d%s%d", ("144 " , message.note , " 0 " , pickidx[8][message.note]), ("%s%d" % ("192.168.12.", pickidx[8][message.note]), 5005) )
                        del pickidx[8][message.note]
            else:
                #if message.channel == 4:
                #    BoomBoom(message.velocity)
                if message.channel == 5:
                    oscdelay = 0
                    if message.velocity == 2:
                        oscdelay = 0.3
                    else:
                        oscdelay = 1.2
                    if message.note == 45:
                        threading.Timer(oscdelay, click, ["A1","start"]).start()
                    elif message.note == 57:
                        threading.Timer(oscdelay, click, ["A2","start"]).start()
                    elif message.note == 69:
                        threading.Timer(oscdelay, click, ["A3","start"]).start()
                    elif message.note == 47:
                        threading.Timer(oscdelay, click, ["B1","start"]).start()
                    elif message.note == 59:
                        threading.Timer(oscdelay, click, ["B2","start"]).start()
                    elif message.note == 36:
                        threading.Timer(oscdelay, click, ["C1","start"]).start()
                    elif message.note == 48:
                        threading.Timer(oscdelay, click, ["C2","start"]).start()
                    elif message.note == 72:
                        threading.Timer(oscdelay, click, ["C4","start"]).start()
                    elif message.note == 84:
                        threading.Timer(oscdelay, click, ["C5","start"]).start()
                    elif message.note == 38:
                        threading.Timer(oscdelay, click, ["D1","start"]).start()
                    elif message.note == 50:
                        threading.Timer(oscdelay, click, ["D2","start"]).start()
                elif message.channel == 6:
                    if message.note == 59:
                        lightinout(True)
                    else:
                        lightinout(False)
                        port.sendto(pack('B',message.note), ("127.0.0.1",11111) )
                else:
                    msg = "n"
                    rayv = None
                    if message.velocity > 2:
                        rayv = pack('BBB', 144, message.note, raymap(message.velocity, 0, 127, boundary, 127))
                    elif message.velocity == 1: #and True == mayIpreload:
                        howmanyPreload += 1
                        print("%s %d" % ("preload ", howmanyPreload))
                        #print datetime.datetime.now()
                        rayv = pack('BBB', 224, message.note, raymap(message.velocity, 0, 127, boundary, 127))
                    elif message.velocity == 2:
                        howmanyAA += 1
                        print("%s %d" % ("after ", howmanyAA))
                        #print datetime.datetime.now()
                        rayv = pack('BBB', 244, message.note, 127)
                        noteoffaa.append(message.note)
                    if message.channel == 3:
                        boidx = checkbound(3,boidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", boidx), 5005) )
                        pickidx[3][message.note] = boidx
                        #boidx += 1
                    elif message.channel == 2:
                        toidx = checkbound(2,toidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", toidx), 5005))
                        pickidx[2][message.note] = toidx
                        #toidx += 1
                    elif message.channel == 1:
                        aoidx = checkbound(1,aoidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", aoidx), 5005))
                        pickidx[1][message.note] = aoidx
                        #aoidx += 1
                    elif message.channel == 0:
                        soidx = checkbound(0,soidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", soidx), 5005))
                        pickidx[0][message.note] = soidx
                        #soidx += 1
                    elif message.channel == 11:
                        boidx = checkbound(3,boidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", boidx), 5005) )
                        pickidx[7][message.note] = boidx
                        #boidx += 1
                        boidx = checkbound(3,boidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", boidx), 5005) )
                        pickidx[11][message.note] = boidx
                        #boidx += 1
                    elif message.channel == 10:
                        toidx = checkbound(2,toidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", toidx), 5005))
                        pickidx[6][message.note] = toidx
                        #toidx += 1
                        toidx = checkbound(2,toidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", toidx), 5005))
                        pickidx[10][message.note] = toidx
                        #toidx += 1
                    elif message.channel == 9:
                        aoidx = checkbound(1,aoidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", aoidx), 5005))
                        pickidx[5][message.note] = aoidx
                        #aoidx += 1
                        aoidx = checkbound(1,aoidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", aoidx), 5005))
                        pickidx[9][message.note] = aoidx
                        #aoidx += 1
                    elif message.channel == 8:
                        soidx = checkbound(0,soidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", soidx), 5005))
                        pickidx[4][message.note] = soidx
                        #soidx += 1
                        soidx = checkbound(0,soidx)
                        port.sendto(rayv, ("%s%d" % ("192.168.12.", soidx), 5005))
                        pickidx[8][message.note] = soidx
                        #soidx += 1
        elif 'note_off' == message.type :
            msg = "f"
            if message.channel == 3:
                if pickidx[3].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[3][message.note]) , ("%s%d" % ("192.168.12.", pickidx[3][message.note]), 5005) )
                    del pickidx[3][message.note]
            elif message.channel == 2:
                if pickidx[2].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[2][message.note]) , ("%s%d" % ("192.168.12.", pickidx[2][message.note]), 5005) )
                    del pickidx[2][message.note]
            elif message.channel == 1:
                if pickidx[1].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[1][message.note]) , ("%s%d" % ("192.168.12.", pickidx[1][message.note]), 5005) )
                    del pickidx[1][message.note]
            elif message.channel == 0:
                if pickidx[0].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[0][message.note]) , ("%s%d" % ("192.168.12.", pickidx[0][message.note]), 5005) )
                    del pickidx[0][message.note]
            elif message.channel == 11:
                if pickidx[7].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[7][message.note]) , ("%s%d" % ("192.168.12.", pickidx[7][message.note]), 5005) )
                    del pickidx[7][message.note]
                if pickidx[11].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[11][message.note]) , ("%s%d" % ("192.168.12.", pickidx[11][message.note]), 5005) )
                    del pickidx[11][message.note]
            elif message.channel == 10:
                if pickidx[6].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[6][message.note]) , ("%s%d" % ("192.168.12.", pickidx[6][message.note]), 5005) )
                    del pickidx[6][message.note]
                if pickidx[10].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[10][message.note]) , ("%s%d" % ("192.168.12.", pickidx[10][message.note]), 5005) )
                    del pickidx[10][message.note]
            elif message.channel == 9:
                if pickidx[5].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[5][message.note]) , ("%s%d" % ("192.168.12.", pickidx[5][message.note]), 5005) )
                    del pickidx[5][message.note]
                if pickidx[9].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[9][message.note]) , ("%s%d" % ("192.168.12.", pickidx[9][message.note]), 5005) )
                    del pickidx[9][message.note]
            elif message.channel == 8:
                if pickidx[4].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[4][message.note]) , ("%s%d" % ("192.168.12.", pickidx[4][message.note]), 5005) )
                    del pickidx[4][message.note]
                if pickidx[8].has_key(message.note):
                    #port.sendto("%s%d %d %d" % ( "128 " , message.note, message.velocity, pickidx[8][message.note]) , ("%s%d" % ("192.168.12.", pickidx[8][message.note]), 5005) )
                    del pickidx[8][message.note]
        if msg.startswith("f") and message.note in noteoffaa:
            msg = pack('sBBB', msg, message.channel, message.note, 2)
            noteoffaa.remove(message.note)
        else:
            msg = pack('sBBB', msg, message.channel, message.note, message.velocity)
        #subprocess.call(['./rayclient', msg, str(message.channel), str(message.note), str(message.velocity)])
        #print msg
        #if msg.startswith("n"):
        #mqueue.insert(0,msg)
        port3.sendto(msg, ("192.168.12.203", 8888) )
        #totaltime = totaltime + message.time
    time.sleep(1.6)
    subprocess.call('./closeart.sh', shell=True)
    for i in ST:
        port.sendto(pack('BBB', 144, 60, 1), ("%s%d" % ("192.168.12.", i), 5005))
    for i in AT:
        port.sendto(pack('BBB', 144, 48, 1), ("%s%d" % ("192.168.12.", i), 5005))
    for i in TT:
        port.sendto(pack('BBB', 144, 38, 1), ("%s%d" % ("192.168.12.", i), 5005))
    for i in BT:
        port.sendto(pack('BBB', 144, 28, 1), ("%s%d" % ("192.168.12.", i), 5005))
    time.sleep(1.6);
    for i in ST:
        port.sendto(pack('BBB', 144, 60, 0), ("%s%d" % ("192.168.12.", i), 5005))
    for i in AT:
        port.sendto(pack('BBB', 144, 48, 0), ("%s%d" % ("192.168.12.", i), 5005))
    for i in TT:
        port.sendto(pack('BBB', 144, 38, 0), ("%s%d" % ("192.168.12.", i), 5005))
    for i in BT:
        port.sendto(pack('BBB', 144, 28, 0), ("%s%d" % ("192.168.12.", i), 5005))
    time.sleep(1.6)
    soundonoff(False)
    AmIPlay = False    
      #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66
#ST = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
ST = [1, 2, 3, 4, 5, 6, 33, 34, 35, 61, 62, 63, 64, 65, 66]
#AT = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
AT = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 30, 31, 32, 36, 37, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
#TT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0 ,0 ,0 ,0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
TT = [18, 19, 20, 21, 22, 23, 29, 38, 39, 44, 45, 46, 47, 48, 49, ]
#BT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1 ,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BT = [24, 25, 26, 27, 28, 40, 41, 42, 43]
soidx = 1
aoidx = 7
toidx = 18
boidx = 24
pickidx = [{},{},{},{},{},{},{},{},{},{},{},{}]
slideidx = [{},{},{},{},{},{},{},{},{},{},{},{}]
port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      
port2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#port.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1)
#port = serial.Serial("\\\\.\\COM7", baudrate=115200)
AmIPlay = False
#pygame.display.init()
#pygame.display.set_mode((100,100))
waitforkey = False
tty.setcbreak(sys.stdin)
mqueue = []
nowisin = False
nowisboom = False
while True:
    #port.flushInput()
    #port.flushOutput()
    #rlist, _, _ = select([sys.stdin], [], [], 0.001)
    eventkey = sys.stdin.read(1)
    if True: #rlist:
        #eventkey = sys.stdin.read(1)
        if AmIPlay == False:
            if eventkey == '1':
                readyplay("Spring.mid")
            elif eventkey == '2':
                readyplay("summer_correct.mid")
            elif eventkey == '3':
                readyplay("Autumn.mid")
            elif eventkey == '4':
                readyplay("WinterRay.mid")
            elif eventkey == '5':
                readyplay("mountain_spectrum_prv1.mid")
            elif eventkey == '6':
                readyplay("womensong.mid")
            elif eventkey == '7':
                readyplay("lovesong.mid")
            elif eventkey == '8':
                readyplay("TEST_1.mid")
            elif eventkey == '9':
                readyplay("TEST_2.mid")
        else:
            if ord(eventkey) == 10:
                waitforkey = False
                #sys.exit()
            elif eventkey == '.':
                BoomBoom(random.randint(0,128),0)
            elif eventkey == '/':
                BoomBoom(random.randint(0,128),1)
            elif eventkey == '*':
                BoomBoom(random.randint(0,128),2)
            elif eventkey == '-':
                BoomBoom(random.randint(0,128),3)
            elif eventkey == '+':
                BoomBoom(random.randint(0,128),4)

    elif AmIPlay == True and len(mqueue) > 0:
        #mqueue.insert(0,'./rayclient')
        #print mqueue
        #subprocess.call(mqueue)
        #del mqueue[:]
        myword = ""
        while len(mqueue) > 0:
            myword += mqueue.pop()
        #print myword
        port.sendto(myword[:-1], ("127.0.0.1", 8888) )    
