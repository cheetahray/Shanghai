#!/usr/bin/env python3
from OSC import OSCServer
import sys
# funny python's way to add a method to an instance of a class
import types
import thread
import time
import socket

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

def Threadfun1(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb1,sb2,sb3,sb4,sb5,sb6
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb1)
        end2 = len(sb2)
        end3 = len(sb3)
        end4 = len(sb4)
        end5 = len(sb5)
        end6 = len(sb6)
        if end1 > 6:
            s1.sendto(sb1, s1tuple)
            sb1 = "artx"
        if end2 > 6:
            s2.sendto(sb2, s2tuple)
            sb2 = "artx"
        if end3 > 6:
            s3.sendto(sb3, s3tuple)
            sb3 = "artx"
        if end4 > 6:
            s4.sendto(sb4, s4tuple)
            sb4 = "artx"
        if end5 > 6:
            s5.sendto(sb5, s5tuple)
            sb5 = "artx"
        if end6 > 6:
            s6.sendto(sb6, s6tuple)
            sb6 = "artx"
        time.sleep(sleeptime)

def Threadfun2(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb7,sb8,sb9,sb10,sb11,sb12
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb7)
        end2 = len(sb8)
        end3 = len(sb9)
        end4 = len(sb10)
        end5 = len(sb11)
        end6 = len(sb12)
        if end1 > 6:
            s1.sendto(sb7, s1tuple)
            sb7 = "artx"
        if end2 > 6:
            s2.sendto(sb8, s2tuple)
            sb8 = "artx"
        if end3 > 6:
            s3.sendto(sb9, s3tuple)
            sb9 = "artx"
        if end4 > 6:
            s4.sendto(sb10, s4tuple)
            sb10 = "artx"
        if end5 > 6:
            s5.sendto(sb11, s5tuple)
            sb11 = "artx"
        if end6 > 6:
            s6.sendto(sb12, s6tuple)
            sb12 = "artx"
        time.sleep(sleeptime)

def Threadfun3(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb13,sb14,sb15,sb16,sb17,sb18
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb13)
        end2 = len(sb14)
        end3 = len(sb15)
        end4 = len(sb16)
        end5 = len(sb17)
        end6 = len(sb18)
        if end1 > 6:
            s1.sendto(sb13, s1tuple)
            sb13 = "artx"
        if end2 > 6:
            s2.sendto(sb14, s2tuple)
            sb14 = "artx"
        if end3 > 6:
            s3.sendto(sb15, s3tuple)
            sb15 = "artx"
        if end4 > 6:
            s4.sendto(sb16, s4tuple)
            sb16 = "artx"
        if end5 > 6:
            s5.sendto(sb17, s5tuple)
            sb17 = "artx"
        if end6 > 6:
            s6.sendto(sb18, s6tuple)
            sb18 = "artx"
        time.sleep(sleeptime)

def Threadfun4(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb19,sb20,sb21,sb22,sb23,sb24
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb19)
        end2 = len(sb20)
        end3 = len(sb21)
        end4 = len(sb22)
        end5 = len(sb23)
        end6 = len(sb24)
        if end1 > 6:
            s1.sendto(sb19, s1tuple)
            sb19 = "artx"
        if end2 > 6:
            s2.sendto(sb20, s2tuple)
            sb20 = "artx"
        if end3 > 6:
            s3.sendto(sb21, s3tuple)
            sb21 = "artx"
        if end4 > 6:
            s4.sendto(sb22, s4tuple)
            sb22 = "artx"
        if end5 > 6:
            s5.sendto(sb23, s5tuple)
            sb23 = "artx"
        if end6 > 6:
            s6.sendto(sb24, s6tuple)
            sb24 = "artx"
        time.sleep(sleeptime)

def Threadfun5(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb25,sb26,sb27,sb28,sb29,sb30
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb25)
        end2 = len(sb26)
        end3 = len(sb27)
        end4 = len(sb28)
        end5 = len(sb29)
        end6 = len(sb30)
        if end1 > 6:
            s1.sendto(sb25, s1tuple)
            sb25 = "artx"
        if end2 > 6:
            s2.sendto(sb26, s2tuple)
            sb26 = "artx"
        if end3 > 6:
            s3.sendto(sb27, s3tuple)
            sb27 = "artx"
        if end4 > 6:
            s4.sendto(sb28, s4tuple)
            sb28 = "artx"
        if end5 > 6:
            s5.sendto(sb29, s5tuple)
            sb29 = "artx"
        if end6 > 6:
            s6.sendto(sb30, s6tuple)
            sb30 = "artx"
        time.sleep(sleeptime)

def Threadfun6(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb31,sb32,sb33,sb34,sb35,sb36
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb31)
        end2 = len(sb32)
        end3 = len(sb33)
        end4 = len(sb34)
        end5 = len(sb35)
        end6 = len(sb36)
        if end1 > 6:
            s1.sendto(sb31, s1tuple)
            sb31 = "artx"
        if end2 > 6:
            s2.sendto(sb32, s2tuple)
            sb32 = "artx"
        if end3 > 6:
            s3.sendto(sb33, s3tuple)
            sb33 = "artx"
        if end4 > 6:
            s4.sendto(sb34, s4tuple)
            sb34 = "artx"
        if end5 > 6:
            s5.sendto(sb35, s5tuple)
            sb35 = "artx"
        if end6 > 6:
            s6.sendto(sb36, s6tuple)
            sb36 = "artx"
        time.sleep(sleeptime)

def Threadfun7(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb37,sb38,sb39,sb40,sb41,sb42
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb37)
        end2 = len(sb38)
        end3 = len(sb39)
        end4 = len(sb40)
        end5 = len(sb41)
        end6 = len(sb42)
        if end1 > 6:
            s1.sendto(sb37, s1tuple)
            sb37 = "artx"
        if end2 > 6:
            s2.sendto(sb38, s2tuple)
            sb38 = "artx"
        if end3 > 6:
            s3.sendto(sb39, s3tuple)
            sb39 = "artx"
        if end4 > 6:
            s4.sendto(sb40, s4tuple)
            sb40 = "artx"
        if end5 > 6:
            s5.sendto(sb41, s5tuple)
            sb41 = "artx"
        if end6 > 6:
            s6.sendto(sb42, s6tuple)
            sb42 = "artx"
        time.sleep(sleeptime)

def Threadfun8(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb43,sb44,sb45,sb46,sb47,sb48
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb43)
        end2 = len(sb44)
        end3 = len(sb45)
        end4 = len(sb46)
        end5 = len(sb47)
        end6 = len(sb48)
        if end1 > 6:
            s1.sendto(sb43, s1tuple)
            sb43 = "artx"
        if end2 > 6:
            s2.sendto(sb44, s2tuple)
            sb44 = "artx"
        if end3 > 6:
            s3.sendto(sb45, s3tuple)
            sb45 = "artx"
        if end4 > 6:
            s4.sendto(sb46, s4tuple)
            sb46 = "artx"
        if end5 > 6:
            s5.sendto(sb47, s5tuple)
            sb47 = "artx"
        if end6 > 6:
            s6.sendto(sb48, s6tuple)
            sb48 = "artx"
        time.sleep(sleeptime)

def Threadfun9(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb49,sb50,sb51,sb52,sb53,sb54
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb49)
        end2 = len(sb50)
        end3 = len(sb51)
        end4 = len(sb52)
        end5 = len(sb53)
        end6 = len(sb54)
        if end1 > 6:
            s1.sendto(sb49, s1tuple)
            sb49 = "artx"
        if end2 > 6:
            s2.sendto(sb50, s2tuple)
            sb50 = "artx"
        if end3 > 6:
            s3.sendto(sb51, s3tuple)
            sb51 = "artx"
        if end4 > 6:
            s4.sendto(sb52, s4tuple)
            sb52 = "artx"
        if end5 > 6:
            s5.sendto(sb53, s5tuple)
            sb53 = "artx"
        if end6 > 6:
            s6.sendto(sb54, s6tuple)
            sb54 = "artx"
        time.sleep(sleeptime)

def Threadfun10(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb55,sb56,sb57,sb58,sb59,sb60
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb55)
        end2 = len(sb56)
        end3 = len(sb57)
        end4 = len(sb58)
        end5 = len(sb59)
        end6 = len(sb60)
        if end1 > 6:
            s1.sendto(sb55, s1tuple)
            sb55 = "artx"
        if end2 > 6:
            s2.sendto(sb56, s2tuple)
            sb56 = "artx"
        if end3 > 6:
            s3.sendto(sb57, s3tuple)
            sb57 = "artx"
        if end4 > 6:
            s4.sendto(sb58, s4tuple)
            sb58 = "artx"
        if end5 > 6:
            s5.sendto(sb59, s5tuple)
            sb59 = "artx"
        if end6 > 6:
            s6.sendto(sb60, s6tuple)
            sb60 = "artx"
        time.sleep(sleeptime)

def Threadfun11(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb61,sb62,sb63,sb64,sb65,sb66
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1tuple = (string1 ,6454)
    s2tuple = (string2 ,6454)
    s3tuple = (string3 ,6454)
    s4tuple = (string4 ,6454)
    s5tuple = (string5 ,6454)
    s6tuple = (string6 ,6454)
    while(True):
        end1 = len(sb61)
        end2 = len(sb62)
        end3 = len(sb63)
        end4 = len(sb64)
        end5 = len(sb65)
        end6 = len(sb66)
        if end1 > 6:
            s1.sendto(sb61, s1tuple)
            sb61 = "artx"
        if end2 > 6:
            s2.sendto(sb62, s2tuple)
            sb62 = "artx"
        if end3 > 6:
            s3.sendto(sb63, s3tuple)
            sb63 = "artx"
        if end4 > 6:
            s4.sendto(sb64, s4tuple)
            sb64 = "artx"
        if end5 > 6:
            s5.sendto(sb65, s5tuple)
            sb65 = "artx"
        if end6 > 6:
            s6.sendto(sb66, s6tuple)
            sb66 = "artx"
        time.sleep(sleeptime)

# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False
def handle_timeout(self):
    self.timed_out = True

def user_callback(path, tags, args, source):
    global port
    global boidx,toidx,aoidx,soidx
    # which user will be determined by path:
    # we just throw away all slashes and join together what's left
    user = ''.join(path.split("/"))
    # user = path.split("/")
    # tags will contain 'fff'
    # args is a OSCMessage with data
    # source is where the message came from (in case you need to reply)
    if 'm' == user:
        #print (user[2],args[0],args[1],args[2],args[3]) 
        if args[2] == 0:
            if args[0] == 147:
                if pickidx[3].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[3][args[1]]), ("192.168.12." + str(pickidx[3][args[1]]), 5005) )
                    del pickidx[3][args[1]]
            elif args[0] == 146:
                if pickidx[2].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[2][args[1]]), ("192.168.12." + str(pickidx[2][args[1]]), 5005) )
                    del pickidx[2][args[1]]
            elif args[0] == 145:
                if pickidx[1].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[1][args[1]]), ("192.168.12." + str(pickidx[1][args[1]]), 5005) )
                    del pickidx[1][args[1]]
            elif args[0] == 144:
                if pickidx[0].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[0][args[1]]), ("192.168.12." + str(pickidx[0][args[1]]), 5005) )
                    del pickidx[0][args[1]]
            elif args[0] == 155:
                if pickidx[7].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[7][args[1]]), ("192.168.12." + str(pickidx[7][args[1]]), 5005) )
                    del pickidx[7][args[1]]
                if pickidx[11].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[11][args[1]]), ("192.168.12." + str(pickidx[11][args[1]]), 5005) )
                    del pickidx[11][args[1]]
            elif args[0] == 154:
                if pickidx[6].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[6][args[1]]), ("192.168.12." + str(pickidx[6][args[1]]), 5005) )
                    del pickidx[6][args[1]]
                if pickidx[10].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[10][args[1]]), ("192.168.12." + str(pickidx[10][args[1]]), 5005) )
                    del pickidx[10][args[1]]
            elif args[0] == 153:
                if pickidx[5].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[5][args[1]]), ("192.168.12." + str(pickidx[5][args[1]]), 5005) )
                    del pickidx[5][args[1]]
                if pickidx[9].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[9][args[1]]), ("192.168.12." + str(pickidx[9][args[1]]), 5005) )
                    del pickidx[9][args[1]]
            elif args[0] == 152:
                if pickidx[4].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[4][args[1]]), ("192.168.12." + str(pickidx[4][args[1]]), 5005) )
                    del pickidx[4][args[1]]
                if pickidx[8].has_key(args[1]):
                    port.sendto("144 " + str(args[1]) + " 0 " + str(pickidx[8][args[1]]), ("192.168.12." + str(pickidx[8][args[1]]), 5005) )
                    del pickidx[8][args[1]]
        else:
            if args[0] == 147:
                boidx = checkbound(3,boidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(boidx) , ("192.168.12." + str(boidx), 5005) )
                pickidx[3][args[1]] = boidx
                boidx += 1
            elif args[0] == 146:
                toidx = checkbound(2,toidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(toidx) , ("192.168.12." + str(toidx), 5005))
                pickidx[2][args[1]] = toidx
                toidx += 1
            elif args[0] == 145:
                aoidx = checkbound(1,aoidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(aoidx) , ("192.168.12." + str(aoidx), 5005))
                pickidx[1][args[1]] = aoidx
                aoidx += 1
            elif args[0] == 144:
                soidx = checkbound(0,soidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(soidx) , ("192.168.12." + str(soidx), 5005))
                pickidx[0][args[1]] = soidx
                soidx += 1
            elif args[0] == 155:
                boidx = checkbound(3,boidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(boidx) , ("192.168.12." + str(boidx), 5005) )
                pickidx[7][args[1]] = boidx
                boidx += 1
                boidx = checkbound(3,boidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(boidx) , ("192.168.12." + str(boidx), 5005) )
                pickidx[11][args[1]] = boidx
                boidx += 1
            elif args[0] == 154:
                toidx = checkbound(2,toidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(toidx) , ("192.168.12." + str(toidx), 5005))
                pickidx[6][args[1]] = toidx
                toidx += 1
                toidx = checkbound(2,toidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(toidx) , ("192.168.12." + str(toidx), 5005))
                pickidx[10][args[1]] = toidx
                toidx += 1
            elif args[0] == 153:
                aoidx = checkbound(1,aoidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(aoidx) , ("192.168.12." + str(aoidx), 5005))
                pickidx[5][args[1]] = aoidx
                aoidx += 1
                aoidx = checkbound(1,aoidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(aoidx) , ("192.168.12." + str(aoidx), 5005))
                pickidx[9][args[1]] = aoidx
                aoidx += 1
            elif args[0] == 152:
                soidx = checkbound(0,soidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(soidx) , ("192.168.12." + str(soidx), 5005))
                pickidx[4][args[1]] = soidx
                soidx += 1
                soidx = checkbound(0,soidx)
                port.sendto("144 " + str(args[1]) + " " + str(args[2]) + " " + str(soidx) , ("192.168.12." + str(soidx), 5005))
                pickidx[8][args[1]] = soidx
                soidx += 1
    elif 'c' == user:
        if args[0] == 0:
            change14(False)
        elif args[0] == 1:
            change14(True)	
    elif 's' == user:
        if args[2] == 0:
            port.sendto("224 " + str(args[1]) + " 0 " + str(args[0]), ("192.168.12." + str(args[0]), 5005) )
        else:
            port.sendto("224 " + str(args[1]) + " " + str(args[2]) + " " + str(args[0]), ("192.168.12." + str(args[0]), 5005) )

def change14(isslider):
    global port
    
    if True == isslider
        for ii range(27,41):
            ST[ii] = 0
            AT[ii] = 0
            TT[ii] = 0
            BT[ii] = 0
            port.sendto("249 0" , ("192.168.12." + str(ii), 5005))
            time.sleep(0.01)
    else:
        ST[33]=1
        ST[34]=1
        ST[35]=1
        AT[30]=1
        AT[31]=1
        AT[32]=1
        AT[36]=1
        AT[37]=1
        TT[29]=1
        TT[38]=1
        TT[39]=1
        BT[27]=1
        BT[28]=1
        BT[40]=1

    for ii range(27,41):
        port.sendto("249 1" , ("192.168.12." + str(ii), 5005))
        time.sleep(0.01)
       
    time.sleep(5)
        
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

server = OSCServer( ("0.0.0.0", 6666) )
server.timeout = 0.001
run = True
server.handle_timeout = types.MethodType(handle_timeout, server)

server.addMsgHandler( "/m", user_callback )
server.addMsgHandler( "/s", user_callback )
#server.addMsgHandler( "/quit", quit_callback )

data = ""
sleeptime = 0.001

sb1="artx"
sb2="artx"
sb3="artx"
sb4="artx"
sb5="artx"
sb6="artx"
sb7="artx"
sb8="artx"
sb9="artx"
sb10="artx"
sb11="artx"
sb12="artx"
sb13="artx"
sb14="artx"
sb15="artx"
sb16="artx"
sb17="artx"
sb18="artx"
sb19="artx"
sb20="artx"
sb21="artx"
sb22="artx"
sb23="artx"
sb24="artx"
sb25="artx"
sb26="artx"
sb27="artx"
sb28="artx"
sb29="artx"
sb30="artx"
sb31="artx"
sb32="artx"
sb33="artx"
sb34="artx"
sb35="artx"
sb36="artx"
sb37="artx"
sb38="artx"
sb39="artx"
sb40="artx"
sb41="artx"
sb42="artx"
sb43="artx"
sb44="artx"
sb45="artx"
sb46="artx"
sb47="artx"
sb48="artx"
sb49="artx"
sb50="artx"
sb51="artx"
sb52="artx"
sb53="artx"
sb54="artx"
sb55="artx"
sb56="artx"
sb57="artx"
sb58="artx"
sb59="artx"
sb60="artx"
sb61="artx"
sb62="artx"
sb63="artx"
sb64="artx"
sb65="artx"
sb66="artx"

i = 1
thread.start_new_thread(Threadfun1, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 7
thread.start_new_thread(Threadfun2, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 13
thread.start_new_thread(Threadfun3, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 19
thread.start_new_thread(Threadfun4, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 25
thread.start_new_thread(Threadfun5, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 31
thread.start_new_thread(Threadfun6, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 37
thread.start_new_thread(Threadfun7, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 43
thread.start_new_thread(Threadfun8, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 49
thread.start_new_thread(Threadfun9, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 55
thread.start_new_thread(Threadfun10, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )
i = 61
thread.start_new_thread(Threadfun11, ("192.168.12." + str(i), "192.168.12." + str(i+1), "192.168.12." + str(i+2), 
                                     "192.168.12." + str(i+3), "192.168.12." + str(i+4), "192.168.12." + str(i+5)
                                         ) )

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", 6454))
sock.settimeout(0.001)

    #27 28 29 30 31 32 33 34 35 36 37 38 39 40 
SS = [0 ,0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
AS = [0 ,0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0]
TS = [0 ,0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
BS = [1 ,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    
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

for i in range(1,67):
    port.sendto("253 " + str(i) + " 100", ("192.168.12." + str(i), 5005) )
    time.sleep(0.01)
for i in range(1,67):
    port.sendto("225 2", ("192.168.12." + str(i), 5005) )
    time.sleep(0.01)
    
# simulate a "game engine"
while run:
    try:
        data, addr = sock.recvfrom(1024)
        if ((len(data) > 18) and (data[0:8] == "Art-Net\x00")):
            rawbytes = map(ord, data)
            opcode = rawbytes[8] + (rawbytes[9] << 8)
            protocolVersion = (rawbytes[10] << 8) + rawbytes[11]
            if ((opcode == 0x5000) and (protocolVersion >= 14)):
                sequence = rawbytes[12]
                physical = rawbytes[13]
                sub_net = (rawbytes[14] & 0xF0) >> 4
                universe = rawbytes[14] & 0x0F
                net = rawbytes[15]
                rgb_length = (rawbytes[16] << 8) + rawbytes[17]
                #print "seq %d phy %d sub_net %d uni %d net %d len %d" % \
                #(sequence, physical, sub_net, universe, net, rgb_length)
                #print "sub_net %d uni %d" % (sub_net, universe)
                idx = 18
                nowx = universe * 4
                if sub_net == 1:
                    nowx = 64
                x = nowx + 1 # 1..66
                y = 0 #0..40
                while ((idx < (rgb_length+18)) and (x - nowx <= 4)):
                    r = rawbytes[idx]
                    idx += 1
                    g = rawbytes[idx]
                    idx += 1
                    b = rawbytes[idx]
                    idx += 1
                    
                    #print ("{0}, {1}, {2}, {3}, {4}".format(x, y, r, g, b) )  #unicorn.set_pixel(x, y, r, g, b)
                    if x == 1:
                        sb1 += str(r)
                        sb1 += " "
                        sb1 += str(g)
                        sb1 += " "
                        sb1 += str(b)
                        sb1 += " "
                        sb1 += str(y)
                        sb1 += " "
                    elif x == 2:
                        sb2 += str(r)
                        sb2 += " "
                        sb2 += str(g)
                        sb2 += " "
                        sb2 += str(b)
                        sb2 += " "
                        sb2 += str(y)
                        sb2 += " "
                    elif x == 3:
                        sb3 += str(r)
                        sb3 += " "
                        sb3 += str(g)
                        sb3 += " "
                        sb3 += str(b)
                        sb3 += " "
                        sb3 += str(y)
                        sb3 += " "
                    elif x == 4:
                        sb4 += str(r)
                        sb4 += " "
                        sb4 += str(g)
                        sb4 += " "
                        sb4 += str(b)
                        sb4 += " "
                        sb4 += str(y)
                        sb4 += " "
                    elif x == 5:
                        sb5 += str(r)
                        sb5 += " "
                        sb5 += str(g)
                        sb5 += " "
                        sb5 += str(b)
                        sb5 += " "
                        sb5 += str(y)
                        sb5 += " "
                    elif x == 6:
                        sb6 += str(r)
                        sb6 += " "
                        sb6 += str(g)
                        sb6 += " "
                        sb6 += str(b)
                        sb6 += " "
                        sb6 += str(y)
                        sb6 += " "
                    elif x == 7:
                        sb7 += str(r)
                        sb7 += " "
                        sb7 += str(g)
                        sb7 += " "
                        sb7 += str(b)
                        sb7 += " "
                        sb7 += str(y)
                        sb7 += " "
                    elif x == 8:
                        sb8 += str(r)
                        sb8 += " "
                        sb8 += str(g)
                        sb8 += " "
                        sb8 += str(b)
                        sb8 += " "
                        sb8 += str(y)
                        sb8 += " "
                    elif x == 9:
                        sb9 += str(r)
                        sb9 += " "
                        sb9 += str(g)
                        sb9 += " "
                        sb9 += str(b)
                        sb9 += " "
                        sb9 += str(y)
                        sb9 += " "
                    elif x == 10:
                        sb10 += str(r)
                        sb10 += " "
                        sb10 += str(g)
                        sb10 += " "
                        sb10 += str(b)
                        sb10 += " "
                        sb10 += str(y)
                        sb10 += " "
                    elif x == 11:
                        sb11 += str(r)
                        sb11 += " "
                        sb11 += str(g)
                        sb11 += " "
                        sb11 += str(b)
                        sb11 += " "
                        sb11 += str(y)
                        sb11 += " "
                    elif x == 12:
                        sb12 += str(r)
                        sb12 += " "
                        sb12 += str(g)
                        sb12 += " "
                        sb12 += str(b)
                        sb12 += " "
                        sb12 += str(y)
                        sb12 += " "
                    elif x == 13:
                        sb13 += str(r)
                        sb13 += " "
                        sb13 += str(g)
                        sb13 += " "
                        sb13 += str(b)
                        sb13 += " "
                        sb13 += str(y)
                        sb13 += " "
                    elif x == 14:
                        sb14 += str(r)
                        sb14 += " "
                        sb14 += str(g)
                        sb14 += " "
                        sb14 += str(b)
                        sb14 += " "
                        sb14 += str(y)
                        sb14 += " "
                    elif x == 15:
                        sb15 += str(r)
                        sb15 += " "
                        sb15 += str(g)
                        sb15 += " "
                        sb15 += str(b)
                        sb15 += " "
                        sb15 += str(y)
                        sb15 += " "
                    elif x == 16:
                        sb16 += str(r)
                        sb16 += " "
                        sb16 += str(g)
                        sb16 += " "
                        sb16 += str(b)
                        sb16 += " "
                        sb16 += str(y)
                        sb16 += " "
                    elif x == 17:
                        sb17 += str(r)
                        sb17 += " "
                        sb17 += str(g)
                        sb17 += " "
                        sb17 += str(b)
                        sb17 += " "
                        sb17 += str(y)
                        sb17 += " "
                    elif x == 18:
                        sb18 += str(r)
                        sb18 += " "
                        sb18 += str(g)
                        sb18 += " "
                        sb18 += str(b)
                        sb18 += " "
                        sb18 += str(y)
                        sb18 += " "
                    elif x == 19:
                        sb19 += str(r)
                        sb19 += " "
                        sb19 += str(g)
                        sb19 += " "
                        sb19 += str(b)
                        sb19 += " "
                        sb19 += str(y)
                        sb19 += " "
                    elif x == 20:
                        sb20 += str(r)
                        sb20 += " "
                        sb20 += str(g)
                        sb20 += " "
                        sb20 += str(b)
                        sb20 += " "
                        sb20 += str(y)
                        sb20 += " "
                    elif x == 21:
                        sb21 += str(r)
                        sb21 += " "
                        sb21 += str(g)
                        sb21 += " "
                        sb21 += str(b)
                        sb21 += " "
                        sb21 += str(y)
                        sb21 += " "
                    elif x == 22:
                        sb22 += str(r)
                        sb22 += " "
                        sb22 += str(g)
                        sb22 += " "
                        sb22 += str(b)
                        sb22 += " "
                        sb22 += str(y)
                        sb22 += " "
                    elif x == 23:
                        sb23 += str(r)
                        sb23 += " "
                        sb23 += str(g)
                        sb23 += " "
                        sb23 += str(b)
                        sb23 += " "
                        sb23 += str(y)
                        sb23 += " "
                    elif x == 24:
                        sb24 += str(r)
                        sb24 += " "
                        sb24 += str(g)
                        sb24 += " "
                        sb24 += str(b)
                        sb24 += " "
                        sb24 += str(y)
                        sb24 += " "
                    elif x == 25:
                        sb25 += str(r)
                        sb25 += " "
                        sb25 += str(g)
                        sb25 += " "
                        sb25 += str(b)
                        sb25 += " "
                        sb25 += str(y)
                        sb25 += " "
                    elif x == 26:
                        sb26 += str(r)
                        sb26 += " "
                        sb26 += str(g)
                        sb26 += " "
                        sb26 += str(b)
                        sb26 += " "
                        sb26 += str(y)
                        sb26 += " "
                    elif x == 27:
                        sb27 += str(r)
                        sb27 += " "
                        sb27 += str(g)
                        sb27 += " "
                        sb27 += str(b)
                        sb27 += " "
                        sb27 += str(y)
                        sb27 += " "
                    elif x == 28:
                        sb28 += str(r)
                        sb28 += " "
                        sb28 += str(g)
                        sb28 += " "
                        sb28 += str(b)
                        sb28 += " "
                        sb28 += str(y)
                        sb28 += " "
                    elif x == 29:
                        sb29 += str(r)
                        sb29 += " "
                        sb29 += str(g)
                        sb29 += " "
                        sb29 += str(b)
                        sb29 += " "
                        sb29 += str(y)
                        sb29 += " "
                    elif x == 30:
                        sb30 += str(r)
                        sb30 += " "
                        sb30 += str(g)
                        sb30 += " "
                        sb30 += str(b)
                        sb30 += " "
                        sb30 += str(y)
                        sb30 += " "
                    elif x == 31:
                        sb31 += str(r)
                        sb31 += " "
                        sb31 += str(g)
                        sb31 += " "
                        sb31 += str(b)
                        sb31 += " "
                        sb31 += str(y)
                        sb31 += " "
                    elif x == 32:
                        sb32 += str(r)
                        sb32 += " "
                        sb32 += str(g)
                        sb32 += " "
                        sb32 += str(b)
                        sb32 += " "
                        sb32 += str(y)
                        sb32 += " "
                    elif x == 33:
                        sb33 += str(r)
                        sb33 += " "
                        sb33 += str(g)
                        sb33 += " "
                        sb33 += str(b)
                        sb33 += " "
                        sb33 += str(y)
                        sb33 += " "
                    elif x == 34:
                        sb34 += str(r)
                        sb34 += " "
                        sb34 += str(g)
                        sb34 += " "
                        sb34 += str(b)
                        sb34 += " "
                        sb34 += str(y)
                        sb34 += " "
                    elif x == 35:
                        sb35 += str(r)
                        sb35 += " "
                        sb35 += str(g)
                        sb35 += " "
                        sb35 += str(b)
                        sb35 += " "
                        sb35 += str(y)
                        sb35 += " "
                    elif x == 36:
                        sb36 += str(r)
                        sb36 += " "
                        sb36 += str(g)
                        sb36 += " "
                        sb36 += str(b)
                        sb36 += " "
                        sb36 += str(y)
                        sb36 += " "
                    elif x == 37:
                        sb37 += str(r)
                        sb37 += " "
                        sb37 += str(g)
                        sb37 += " "
                        sb37 += str(b)
                        sb37 += " "
                        sb37 += str(y)
                        sb37 += " "
                    elif x == 38:
                        sb38 += str(r)
                        sb38 += " "
                        sb38 += str(g)
                        sb38 += " "
                        sb38 += str(b)
                        sb38 += " "
                        sb38 += str(y)
                        sb38 += " "
                    elif x == 39:
                        sb39 += str(r)
                        sb39 += " "
                        sb39 += str(g)
                        sb39 += " "
                        sb39 += str(b)
                        sb39 += " "
                        sb39 += str(y)
                        sb39 += " "
                    elif x == 40:
                        sb40 += str(r)
                        sb40 += " "
                        sb40 += str(g)
                        sb40 += " "
                        sb40 += str(b)
                        sb40 += " "
                        sb40 += str(y)
                        sb40 += " "
                    elif x == 41:
                        sb41 += str(r)
                        sb41 += " "
                        sb41 += str(g)
                        sb41 += " "
                        sb41 += str(b)
                        sb41 += " "
                        sb41 += str(y)
                        sb41 += " "
                    elif x == 42:
                        sb42 += str(r)
                        sb42 += " "
                        sb42 += str(g)
                        sb42 += " "
                        sb42 += str(b)
                        sb42 += " "
                        sb42 += str(y)
                        sb42 += " "
                    elif x == 43:
                        sb43 += str(r)
                        sb43 += " "
                        sb43 += str(g)
                        sb43 += " "
                        sb43 += str(b)
                        sb43 += " "
                        sb43 += str(y)
                        sb43 += " "
                    elif x == 44:
                        sb44 += str(r)
                        sb44 += " "
                        sb44 += str(g)
                        sb44 += " "
                        sb44 += str(b)
                        sb44 += " "
                        sb44 += str(y)
                        sb44 += " "
                    elif x == 45:
                        sb45 += str(r)
                        sb45 += " "
                        sb45 += str(g)
                        sb45 += " "
                        sb45 += str(b)
                        sb45 += " "
                        sb45 += str(y)
                        sb45 += " "
                    elif x == 46:
                        sb46 += str(r)
                        sb46 += " "
                        sb46 += str(g)
                        sb46 += " "
                        sb46 += str(b)
                        sb46 += " "
                        sb46 += str(y)
                        sb46 += " "
                    elif x == 47:
                        sb47 += str(r)
                        sb47 += " "
                        sb47 += str(g)
                        sb47 += " "
                        sb47 += str(b)
                        sb47 += " "
                        sb47 += str(y)
                        sb47 += " "
                    elif x == 48:
                        sb48 += str(r)
                        sb48 += " "
                        sb48 += str(g)
                        sb48 += " "
                        sb48 += str(b)
                        sb48 += " "
                        sb48 += str(y)
                        sb48 += " "
                    elif x == 49:
                        sb49 += str(r)
                        sb49 += " "
                        sb49 += str(g)
                        sb49 += " "
                        sb49 += str(b)
                        sb49 += " "
                        sb49 += str(y)
                        sb49 += " "
                    elif x == 50:
                        sb50 += str(r)
                        sb50 += " "
                        sb50 += str(g)
                        sb50 += " "
                        sb50 += str(b)
                        sb50 += " "
                        sb50 += str(y)
                        sb50 += " "
                    elif x == 51:
                        sb51 += str(r)
                        sb51 += " "
                        sb51 += str(g)
                        sb51 += " "
                        sb51 += str(b)
                        sb51 += " "
                        sb51 += str(y)
                        sb51 += " "
                    elif x == 52:
                        sb52 += str(r)
                        sb52 += " "
                        sb52 += str(g)
                        sb52 += " "
                        sb52 += str(b)
                        sb52 += " "
                        sb52 += str(y)
                        sb52 += " "
                    elif x == 53:
                        sb53 += str(r)
                        sb53 += " "
                        sb53 += str(g)
                        sb53 += " "
                        sb53 += str(b)
                        sb53 += " "
                        sb53 += str(y)
                        sb53 += " "
                    elif x == 54:
                        sb54 += str(r)
                        sb54 += " "
                        sb54 += str(g)
                        sb54 += " "
                        sb54 += str(b)
                        sb54 += " "
                        sb54 += str(y)
                        sb54 += " "
                    elif x == 55:
                        sb55 += str(r)
                        sb55 += " "
                        sb55 += str(g)
                        sb55 += " "
                        sb55 += str(b)
                        sb55 += " "
                        sb55 += str(y)
                        sb55 += " "
                    elif x == 56:
                        sb56 += str(r)
                        sb56 += " "
                        sb56 += str(g)
                        sb56 += " "
                        sb56 += str(b)
                        sb56 += " "
                        sb56 += str(y)
                        sb56 += " "
                    elif x == 57:
                        sb57 += str(r)
                        sb57 += " "
                        sb57 += str(g)
                        sb57 += " "
                        sb57 += str(b)
                        sb57 += " "
                        sb57 += str(y)
                        sb57 += " "
                    elif x == 58:
                        sb58 += str(r)
                        sb58 += " "
                        sb58 += str(g)
                        sb58 += " "
                        sb58 += str(b)
                        sb58 += " "
                        sb58 += str(y)
                        sb58 += " "
                    elif x == 59:
                        sb59 += str(r)
                        sb59 += " "
                        sb59 += str(g)
                        sb59 += " "
                        sb59 += str(b)
                        sb59 += " "
                        sb59 += str(y)
                        sb59 += " "
                    elif x == 60:
                        sb60 += str(r)
                        sb60 += " "
                        sb60 += str(g)
                        sb60 += " "
                        sb60 += str(b)
                        sb60 += " "
                        sb60 += str(y)
                        sb60 += " "
                    elif x == 61:
                        sb61 += str(r)
                        sb61 += " "
                        sb61 += str(g)
                        sb61 += " "
                        sb61 += str(b)
                        sb61 += " "
                        sb61 += str(y)
                        sb61 += " "
                    elif x == 62:
                        sb62 += str(r)
                        sb62 += " "
                        sb62 += str(g)
                        sb62 += " "
                        sb62 += str(b)
                        sb62 += " "
                        sb62 += str(y)
                        sb62 += " "
                    elif x == 63:
                        sb63 += str(r)
                        sb63 += " "
                        sb63 += str(g)
                        sb63 += " "
                        sb63 += str(b)
                        sb63 += " "
                        sb63 += str(y)
                        sb63 += " "
                    elif x == 64:
                        sb64 += str(r)
                        sb64 += " "
                        sb64 += str(g)
                        sb64 += " "
                        sb64 += str(b)
                        sb64 += " "
                        sb64 += str(y)
                        sb64 += " "
                    elif x == 65:
                        sb65 += str(r)
                        sb65 += " "
                        sb65 += str(g)
                        sb65 += " "
                        sb65 += str(b)
                        sb65 += " "
                        sb65 += str(y)
                        sb65 += " "
                    elif x == 66:
                        sb66 += str(r)
                        sb66 += " "
                        sb66 += str(g)
                        sb66 += " "
                        sb66 += str(b)
                        sb66 += " "
                        sb66 += str(y)
                        sb66 += " "
                    
                    y += 1
                    if (y >= 44):
                        y = 0
                        x += 1
    except socket.timeout:
        pass                    
    except ValueError:
        pass    
    except IndexError:
        pass
    each_frame()

server.close()
