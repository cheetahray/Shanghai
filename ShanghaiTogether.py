#/usr/bin/python
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
import threading
from mido import MidiFile
#import xlsxwriter
#import serial
import socket
import pysimpledmx

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

def raysendto(_1st,_2nd,_3rd,_4th, raystr, raytuple):
    port.sendto( raystr, raytuple )
    play_dmx(_1st,_2nd,_3rd,_4th)
    
def play_dmx(_1st,_2nd,_3rd,_4th):
    global mydmx
    '''
    mydmx.setChannel(2, _1st) 
    print chan[ii]
    mydmx.setChannel(3, _2nd)
    print chan[ii+1]
    mydmx.setChannel(4, _3rd)
    print chan[ii+2]
    mydmx.setChannel(5, _4th)    
    print chan[ii+3]
    mydmx.render()
    '''
                
def play_midi():
    global isplay
    global myshift
    global port
    global boidx,toidx,aoidx,soidx
    #workbook = xlsxwriter.Workbook('demo.xlsx')
    #worksheet = workbook.add_worksheet()
    lastpiano = 0
    boundary = 0
    pianoDELAY = 0.925
    DELAY = 1.025
    for i in range(1,67):
        port.sendto("249 3", ("192.168.12." + str(i), 5005) )
        time.sleep(0.01)
    for dd in range(0,len(drum)):
        port.sendto("249 3", ("192.168.13." + str(drum[dd]), 8888) )
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
        if debug:
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
                elif message.channel == 12 or (message.channel <= 7 and message.channel >= 4):
                    if lastpiano == message.note and message.time < 0.1:
                        pass
                    else:
                        lastpiano = message.note
                        if message.note == 84:
                            threading.Timer( pianoDELAY, port.sendto, ["127", ("192.168.13.255", 8888)]).start()
                        elif message.note == 86:
                            threading.Timer( pianoDELAY, port.sendto, ["143", ("192.168.13.255", 8888)]).start()
                        elif message.note == 88:
                            threading.Timer( pianoDELAY, port.sendto, ["159", ("192.168.13.255", 8888)]).start()
                        elif message.note == 89:
                            threading.Timer( pianoDELAY, port.sendto, ["175", ("192.168.13.255", 8888)]).start()
                        elif message.note == 91:
                            threading.Timer( pianoDELAY, port.sendto, ["191", ("192.168.13.255", 8888)]).start()
                        elif message.note == 93:
                            threading.Timer( pianoDELAY, port.sendto, ["207", ("192.168.13.255", 8888)]).start()
                        elif message.note == 95:
                            threading.Timer( pianoDELAY, port.sendto, ["223", ("192.168.13.255", 8888)]).start()
                        elif message.note == 96:
                            threading.Timer( pianoDELAY, port.sendto, ["239", ("192.168.13.255", 8888)]).start()
                elif message.channel == 13:
                    if message.note == 36:
                        threading.Timer( DELAY, raysendto, [1,1,0,0,"239", ("192.168.13.241", 6666)]).start()
                    elif message.note == 38:
                        threading.Timer( DELAY, raysendto, [1,1,0,0,"223", ("192.168.13.241", 6666)]).start()
                    elif message.note == 39:
                        threading.Timer( DELAY, raysendto, [1,1,0,0,"207", ("192.168.13.241", 6666)]).start()
                    elif message.note == 40:
                        threading.Timer( DELAY, raysendto, [1,1,0,0,"191", ("192.168.13.242", 6666)]).start()
                    elif message.note == 41:
                        threading.Timer( DELAY, raysendto, [1,1,0,0,"239", ("192.168.13.242", 6666)]).start()
                    elif message.note == 42:
                        threading.Timer( DELAY, raysendto, [1,1,0,0,"223", ("192.168.13.242", 6666)]).start()
                    elif message.note == 43:
                        threading.Timer( DELAY, raysendto, [0,1,1,0,"143", ("192.168.13.247", 6666)]).start()
                    elif message.note == 44:
                        threading.Timer( DELAY, raysendto, [0,1,1,0,"127", ("192.168.13.247", 6666)]).start()
                    elif message.note == 45:
                        threading.Timer( DELAY, raysendto, [0,1,1,0,"159", ("192.168.13.247", 6666)]).start()
                    elif message.note == 46:
                        threading.Timer( DELAY, raysendto, [0,1,1,0,"143", ("192.168.13.243", 6666)]).start()
                    elif message.note == 47:
                        threading.Timer( DELAY, raysendto, [0,1,1,0,"127", ("192.168.13.243", 6666)]).start()
                    elif message.note == 48:
                        threading.Timer( DELAY, raysendto, [0,1,1,0,"175", ("192.168.13.241", 6666)]).start()
                    elif message.note == 49:
                        threading.Timer( DELAY, raysendto, [0,1,1,0,"159", ("192.168.13.241", 6666)]).start()
                    elif message.note == 50:
                        threading.Timer( DELAY, raysendto, [1,0,1,0,"239", ("192.168.13.243", 6666)]).start()
                    elif message.note == 51:
                        threading.Timer( DELAY, raysendto, [1,0,1,0,"223", ("192.168.13.243", 6666)]).start()
                    elif message.note == 52:
                        threading.Timer( DELAY, raysendto, [1,0,1,0,"207", ("192.168.13.243", 6666)]).start()
                    elif message.note == 53:
                        threading.Timer( DELAY, raysendto, [1,0,1,0,"191", ("192.168.13.243", 6666)]).start()
                    elif message.note == 54:
                        threading.Timer( DELAY, raysendto, [1,0,1,0,"175", ("192.168.13.243", 6666)]).start()
                    elif message.note == 55:
                        threading.Timer( DELAY, raysendto, [1,0,0,1,"239", ("192.168.13.244", 6666)]).start()
                    elif message.note == 56:
                        threading.Timer( DELAY, raysendto, [1,0,0,1,"223", ("192.168.13.244", 6666)]).start()
                    elif message.note == 57:
                        threading.Timer( DELAY, raysendto, [1,0,0,1,"207", ("192.168.13.244", 6666)]).start()
                    elif message.note == 58:
                        threading.Timer( DELAY, raysendto, [1,0,0,1,"191", ("192.168.13.244", 6666)]).start()
                    elif message.note == 59:
                        threading.Timer( DELAY, raysendto, [1,0,0,1,"175", ("192.168.13.244", 6666)]).start()
                    elif message.note == 60:
                        threading.Timer( DELAY, raysendto, [1,1,1,0,"239", ("192.168.13.245", 6666)]).start()
                    elif message.note == 61:
                        threading.Timer( DELAY, raysendto, [1,1,1,0,"223", ("192.168.13.245", 6666)]).start()
                    elif message.note == 62:
                        threading.Timer( DELAY, raysendto, [1,1,1,0,"207", ("192.168.13.245", 6666)]).start()
                    elif message.note == 63:
                        threading.Timer( DELAY, raysendto, [1,1,1,0,"191", ("192.168.13.245", 6666)]).start()
                    elif message.note == 64:
                        threading.Timer( DELAY, raysendto, [1,1,1,0,"175", ("192.168.13.245", 6666)]).start()
                    elif message.note == 72:
                        threading.Timer( DELAY, raysendto, [1,0,1,1,"143", ("192.168.13.249", 6666)]).start()
                    elif message.note == 73:
                        threading.Timer( DELAY, raysendto, [1,0,1,1,"127", ("192.168.13.249", 6666)]).start()                                            
                elif message.channel == 11:
                    if pickidx[7].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[7][message.note]) + "\r", ("192.168.12." + str(pickidx[7][message.note]), 5005))
                        del pickidx[7][message.note]
                    if pickidx[11].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[11][message.note]) + "\r", ("192.168.12." + str(pickidx[11][message.note]), 5005))
                        del pickidx[11][message.note]
                elif message.channel == 10:
                    if pickidx[6].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[6][message.note]) + "\r", ("192.168.12." + str(pickidx[6][message.note]), 5005))
                        del pickidx[6][message.note]
                    if pickidx[10].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[10][message.note]) + "\r", ("192.168.12." + str(pickidx[10][message.note]), 5005))
                        del pickidx[10][message.note]
                elif message.channel == 9:
                    if pickidx[5].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[5][message.note]) + "\r", ("192.168.12." + str(pickidx[5][message.note]), 5005))
                        del pickidx[5][message.note]
                    if pickidx[9].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[9][message.note]) + "\r", ("192.168.12." + str(pickidx[9][message.note]), 5005))
                        del pickidx[9][message.note]
                elif message.channel == 8:
                    if pickidx[4].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[4][message.note]) + "\r", ("192.168.12." + str(pickidx[4][message.note]), 5005))
                        del pickidx[4][message.note]
                    if pickidx[8].has_key(message.note):
                        port.sendto("144 " + str(message.note) + " 0 " + str(pickidx[8][message.note]) + "\r", ("192.168.12." + str(pickidx[8][message.note]), 5005))
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
    time.sleep(3.5);
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
    time.sleep(3.5);
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
    time.sleep(3.5);
    for i in range(1,67):
        port.sendto("249 2" , ("192.168.12." + str(i), 5005))
        time.sleep(0.01)
    for dd in range(0, len(drum)):
        port.sendto("249 2" , ("192.168.13." + str(drum[dd]), 8888))
        time.sleep(0.01)
    play_dmx(1,1,1,1)
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
#port.sendto("127", ("192.168.13.249", 8888))
#time.sleep(2)
#port.sendto("143", ("192.168.13.249", 8888))
#time.sleep(2)
port.bind(("0.0.0.0", 8888))
port.settimeout(0.2)
drum = [202,203]
drumlen = 0
mydmx = None #pysimpledmx.DMXConnection("/dev/ttyUSB0")
try:
    if False:
        for dd in range(1,121):
            port.sendto("WHO", ("192.168.13." + str(dd), 8888))
            try:    
                data, addr = port.recvfrom(1024)
                if (data == "bell"):
                    drum.append(dd);
                    print drum  
            except socket.timeout:
                continue 
        drumlen = len(drum) / 5
        if drumlen == 0:
            drumlen = 1
            for dd in range(len(drum),5):
                drum.append(135+dd)        
                print drum
    else:
        port.setsockopt(socket.SOL_SOCKET , socket.SO_BROADCAST , 1)      
    port.settimeout(0)
    if '__main__' == __name__ :
        parser = argparse.ArgumentParser()
        parser.add_argument("--song",
                             default="001", help="Midi file")
        args = parser.parse_args()
        mid = MidiFile('/home/oem/midi/' + args.song + '.mid')
        midi_suite = unittest.TestSuite()   #Add play midi test function
        all_suite = unittest.TestSuite()
        midi_suite.addTest(Tests("test_0"))
        all_suite.addTest(midi_suite)
        unittest.TextTestRunner(verbosity=1).run(all_suite)
    elif False:
        port.sendto("Home", ("192.168.12." + whoami, 5005))

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
