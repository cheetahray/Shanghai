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
from OSC import *
import types
import thread

server = OSCServer( ("0.0.0.0", 6666) )
server.timeout = 0
run = True
cc = OSCClient()
cc.connect(('192.168.12.248', 1225))   # localhost, port 57120

mid1 = MidiFile('/home/oem/midi/CM_66midi_1.mid')
mid2 = MidiFile('/home/oem/midi/CM_66midi_2.mid')
mid3 = MidiFile('/home/oem/midi/CM_66midi_3.mid')
mid4 = MidiFile('/home/oem/midi/CM_66midi_4.mid')
mid5 = MidiFile('/home/oem/midi/CM_66midi_5.mid')
mid6 = MidiFile('/home/oem/midi/CM_66midi_6.mid')
mid7 = MidiFile('/home/oem/midi/CM_66midi_7.mid')
debug = False        #Boolean for on/off our debug print 
isplay = 0      #Boolean to judge whether the midi is playing
# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False
def handle_timeout(self):
    self.timed_out = True

server.handle_timeout = types.MethodType(handle_timeout, server)

def user_callback(path, tags, args, source):
    # which user will be determined by path:
    # we just throw away all slashes and join together what's left
    #user = ''.join(path.split("/"))
    # tags will contain 'fff'
    # args is a OSCMessage with data
    # source is where the message came from (in case you need to reply)
    global mid1,mid2,mid3,mid4,mid5,mid6,mid7
    global isplay
    print args[0]
    isplay = args[0]
    if 0 == args[0]:
       play_head() 
    elif 1 == args[0]:
       thread.start_new_thread(play_midi,(mid1,))
       time.sleep(1)
    elif 2 == args[0]:
       thread.start_new_thread(play_midi,(mid2,))
       time.sleep(1)
    elif 3 == args[0]:
       thread.start_new_thread(play_midi,(mid3,))
       time.sleep(1)
    elif 4 == args[0]:
       thread.start_new_thread(play_midi,(mid4,))
       time.sleep(1)
    elif 5 == args[0]:
       thread.start_new_thread(play_midi,(mid5,))
       time.sleep(1)
    elif 6 == args[0]:
       thread.start_new_thread(play_midi,(mid6,))
       time.sleep(1)
    elif False: #7 == args[0]:
       thread.start_new_thread(play_midi,(mid7,))
       time.sleep(1)
    elif -1 == args[0]:
       play_foot()
        
    #print ("Now do something with", user,args[2],args[0],1-args[1]) 

def quit_callback(path, tags, args, source):
    # don't do this at home (or it'll quit blender)
    global run
    run = False

# user script that's called by the game engine every frame
def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

def click(msg, val):
    global cc
    mymsg = "/" + msg
    oscmsg = OSCMessage()
    print "%s" % (mymsg)
    oscmsg.setAddress("%s" % (mymsg) )
    oscmsg.append(val)
    cc.send(oscmsg)

class Tests(unittest.TestCase):
    def test_0(self):   #Test play midi file
        play_midi(mid1);

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

def play_head():
    for i in range(1,67):
        port.sendto(pack('BB', 249, 3), ("192.168.12." + str(i), 5005) )
        time.sleep(0.01)
    time.sleep(4)
    for i in range(34,67):
        port.sendto(pack('BB', 225, 0), ("192.168.12." + str(i), 5005) )
        port.sendto(pack('BB', 225, 0), ("192.168.12." + str(67-i), 5005) )
        time.sleep(0.02)
        #f.append(0)
        #worksheet.write(i, 0, 0)
    time.sleep(1)

def play_midi(midd):
    global port
    global boidx,toidx,aoidx,soidx
    boundary = 0
    global isplay
    lastplay = isplay
    for message in midd.play():  #Next note from midi in this moment
        if lastplay != isplay:
            print "break"
            break
        elif 'note_on' == message.type :
            #print(message)
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
    print str(lastplay) + "_Done"

def play_foot():
    global run
    time.sleep(3.5);
    for i in range(66,33,-1):
        port.sendto(pack('BB', 225, 1), ("192.168.12." + str(i), 5005) )
        port.sendto(pack('BB', 225, 1), ("192.168.12." + str(67-i), 5005) )
        time.sleep(0.02)
    time.sleep(1)
    for i in range(1,67):
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
    for i in range(1,67):
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
    for i in range(1,67):
        port.sendto(pack('BB', 249, 2), ("192.168.12." + str(i), 5005))
        time.sleep(0.01)
    run = False   

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
server.addMsgHandler( "/cue", user_callback )
try:
    #port.flushInput()
    #port.flushOutput()
    click("stop",0)
    time.sleep(0.1)
    click("start",1)
    whoami = "65"
    #Register the door bell button GPIO input call back function
    # simulate a "game engine"
    while run:
        # do the game stuff:
        #sleep(1)
        # call user script
        each_frame()

        #if '__main__' == __name__ :
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument("--song",
                             default="chu", help="Midi file")
        args = parser.parse_args()
        mid = MidiFile('/home/oem/midi/' + args.song + '.mid')     
        midi_suite = unittest.TestSuite()   #Add play midi test function
        all_suite = unittest.TestSuite()
        midi_suite.addTest(Tests("test_0"))
        all_suite.addTest(midi_suite)
        unittest.TextTestRunner(verbosity=1).run(all_suite)
        '''
    #elif False:
        #port.sendto("Home", ("192.168.12." + whoami, 5005))

    server.close()

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
