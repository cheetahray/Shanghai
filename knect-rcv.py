#!/usr/bin/env python3
from OSC import OSCServer
import sys
# funny python's way to add a method to an instance of a class
import types
import thread
import time
import socket

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
    global sb1
    global sb2
    global sb3
    global sb4
    global sb5
    global sb6
    global sb7
    global sb8
    global sb9
    global sb10
    global sb11
    global sb12
    global sb13
    global sb14
    global sb15
    global sb16
    global sb17
    global sb18
    global sb19
    global sb20
    global sb21
    global sb22
    global sb23
    global sb24
    global sb25
    global sb26
    global sb27
    global sb28
    global sb29
    global sb30
    global sb31
    global sb32
    global sb33
    global sb34
    global sb35
    global sb36
    global sb37
    global sb38
    global sb39
    global sb40
    global sb41
    global sb42
    global sb43
    global sb44
    global sb45
    global sb46
    global sb47
    global sb48
    global sb49
    global sb50
    global sb51
    global sb52
    global sb53
    global sb54
    global sb55
    global sb56
    global sb57
    global sb58
    global sb59
    global sb60
    global sb61
    global sb62
    global sb63
    global sb64
    global sb65
    global sb66
    # which user will be determined by path:
    # we just throw away all slashes and join together what's left
    # user = ''.join(path.split("/"))
    user = path.split("/")
    # tags will contain 'fff'
    # args is a OSCMessage with data
    # source is where the message came from (in case you need to reply)
    x = int(user[2])
    if x == 1:
        sb1 += str(args[1])
        sb1 += " "
        sb1 += str(args[2])
        sb1 += " "
        sb1 += str(args[3])
        sb1 += " "
        sb1 += str(args[0])
        sb1 += " "
    elif x == 2:
        sb2 += str(args[1])
        sb2 += " "
        sb2 += str(args[2])
        sb2 += " "
        sb2 += str(args[3])
        sb2 += " "
        sb2 += str(args[0])
        sb2 += " "
    elif x == 3:
        sb3 += str(args[1])
        sb3 += " "
        sb3 += str(args[2])
        sb3 += " "
        sb3 += str(args[3])
        sb3 += " "
        sb3 += str(args[0])
        sb3 += " "
    elif x == 4:
        sb4 += str(args[1])
        sb4 += " "
        sb4 += str(args[2])
        sb4 += " "
        sb4 += str(args[3])
        sb4 += " "
        sb4 += str(args[0])
        sb4 += " "
    elif x == 5:
        sb5 += str(args[1])
        sb5 += " "
        sb5 += str(args[2])
        sb5 += " "
        sb5 += str(args[3])
        sb5 += " "
        sb5 += str(args[0])
        sb5 += " "
    elif x == 6:
        sb6 += str(args[1])
        sb6 += " "
        sb6 += str(args[2])
        sb6 += " "
        sb6 += str(args[3])
        sb6 += " "
        sb6 += str(args[0])
        sb6 += " "
    elif x == 7:
        sb7 += str(args[1])
        sb7 += " "
        sb7 += str(args[2])
        sb7 += " "
        sb7 += str(args[3])
        sb7 += " "
        sb7 += str(args[0])
        sb7 += " "
    elif x == 8:
        sb8 += str(args[1])
        sb8 += " "
        sb8 += str(args[2])
        sb8 += " "
        sb8 += str(args[3])
        sb8 += " "
        sb8 += str(args[0])
        sb8 += " "
    elif x == 9:
        sb9 += str(args[1])
        sb9 += " "
        sb9 += str(args[2])
        sb9 += " "
        sb9 += str(args[3])
        sb9 += " "
        sb9 += str(args[0])
        sb9 += " "
    elif x == 10:
        sb10 += str(args[1])
        sb10 += " "
        sb10 += str(args[2])
        sb10 += " "
        sb10 += str(args[3])
        sb10 += " "
        sb10 += str(args[0])
        sb10 += " "
    elif x == 11:
        sb11 += str(args[1])
        sb11 += " "
        sb11 += str(args[2])
        sb11 += " "
        sb11 += str(args[3])
        sb11 += " "
        sb11 += str(args[0])
        sb11 += " "
    elif x == 12:
        sb12 += str(args[1])
        sb12 += " "
        sb12 += str(args[2])
        sb12 += " "
        sb12 += str(args[3])
        sb12 += " "
        sb12 += str(args[0])
        sb12 += " "
    elif x == 13:
        sb13 += str(args[1])
        sb13 += " "
        sb13 += str(args[2])
        sb13 += " "
        sb13 += str(args[3])
        sb13 += " "
        sb13 += str(args[0])
        sb13 += " "
    elif x == 14:
        sb14 += str(args[1])
        sb14 += " "
        sb14 += str(args[2])
        sb14 += " "
        sb14 += str(args[3])
        sb14 += " "
        sb14 += str(args[0])
        sb14 += " "
    elif x == 15:
        sb15 += str(args[1])
        sb15 += " "
        sb15 += str(args[2])
        sb15 += " "
        sb15 += str(args[3])
        sb15 += " "
        sb15 += str(args[0])
        sb15 += " "
    elif x == 16:
        sb16 += str(args[1])
        sb16 += " "
        sb16 += str(args[2])
        sb16 += " "
        sb16 += str(args[3])
        sb16 += " "
        sb16 += str(args[0])
        sb16 += " "
    elif x == 17:
        sb17 += str(args[1])
        sb17 += " "
        sb17 += str(args[2])
        sb17 += " "
        sb17 += str(args[3])
        sb17 += " "
        sb17 += str(args[0])
        sb17 += " "
    elif x == 18:
        sb18 += str(args[1])
        sb18 += " "
        sb18 += str(args[2])
        sb18 += " "
        sb18 += str(args[3])
        sb18 += " "
        sb18 += str(args[0])
        sb18 += " "
    elif x == 19:
        sb19 += str(args[1])
        sb19 += " "
        sb19 += str(args[2])
        sb19 += " "
        sb19 += str(args[3])
        sb19 += " "
        sb19 += str(args[0])
        sb19 += " "
    elif x == 20:
        sb20 += str(args[1])
        sb20 += " "
        sb20 += str(args[2])
        sb20 += " "
        sb20 += str(args[3])
        sb20 += " "
        sb20 += str(args[0])
        sb20 += " "
    elif x == 21:
        sb21 += str(args[1])
        sb21 += " "
        sb21 += str(args[2])
        sb21 += " "
        sb21 += str(args[3])
        sb21 += " "
        sb21 += str(args[0])
        sb21 += " "
    elif x == 22:
        sb22 += str(args[1])
        sb22 += " "
        sb22 += str(args[2])
        sb22 += " "
        sb22 += str(args[3])
        sb22 += " "
        sb22 += str(args[0])
        sb22 += " "
    elif x == 23:
        sb23 += str(args[1])
        sb23 += " "
        sb23 += str(args[2])
        sb23 += " "
        sb23 += str(args[3])
        sb23 += " "
        sb23 += str(args[0])
        sb23 += " "
    elif x == 24:
        sb24 += str(args[1])
        sb24 += " "
        sb24 += str(args[2])
        sb24 += " "
        sb24 += str(args[3])
        sb24 += " "
        sb24 += str(args[0])
        sb24 += " "
    elif x == 25:
        sb25 += str(args[1])
        sb25 += " "
        sb25 += str(args[2])
        sb25 += " "
        sb25 += str(args[3])
        sb25 += " "
        sb25 += str(args[0])
        sb25 += " "
    elif x == 26:
        sb26 += str(args[1])
        sb26 += " "
        sb26 += str(args[2])
        sb26 += " "
        sb26 += str(args[3])
        sb26 += " "
        sb26 += str(args[0])
        sb26 += " "
    elif x == 27:
        sb27 += str(args[1])
        sb27 += " "
        sb27 += str(args[2])
        sb27 += " "
        sb27 += str(args[3])
        sb27 += " "
        sb27 += str(args[0])
        sb27 += " "
    elif x == 28:
        sb28 += str(args[1])
        sb28 += " "
        sb28 += str(args[2])
        sb28 += " "
        sb28 += str(args[3])
        sb28 += " "
        sb28 += str(args[0])
        sb28 += " "
    elif x == 29:
        sb29 += str(args[1])
        sb29 += " "
        sb29 += str(args[2])
        sb29 += " "
        sb29 += str(args[3])
        sb29 += " "
        sb29 += str(args[0])
        sb29 += " "
    elif x == 30:
        sb30 += str(args[1])
        sb30 += " "
        sb30 += str(args[2])
        sb30 += " "
        sb30 += str(args[3])
        sb30 += " "
        sb30 += str(args[0])
        sb30 += " "
    elif x == 31:
        sb31 += str(args[1])
        sb31 += " "
        sb31 += str(args[2])
        sb31 += " "
        sb31 += str(args[3])
        sb31 += " "
        sb31 += str(args[0])
        sb31 += " "
    elif x == 32:
        sb32 += str(args[1])
        sb32 += " "
        sb32 += str(args[2])
        sb32 += " "
        sb32 += str(args[3])
        sb32 += " "
        sb32 += str(args[0])
        sb32 += " "
    elif x == 33:
        sb33 += str(args[1])
        sb33 += " "
        sb33 += str(args[2])
        sb33 += " "
        sb33 += str(args[3])
        sb33 += " "
        sb33 += str(args[0])
        sb33 += " "
    elif x == 34:
        sb34 += str(args[1])
        sb34 += " "
        sb34 += str(args[2])
        sb34 += " "
        sb34 += str(args[3])
        sb34 += " "
        sb34 += str(args[0])
        sb34 += " "
    elif x == 35:
        sb35 += str(args[1])
        sb35 += " "
        sb35 += str(args[2])
        sb35 += " "
        sb35 += str(args[3])
        sb35 += " "
        sb35 += str(args[0])
        sb35 += " "
    elif x == 36:
        sb36 += str(args[1])
        sb36 += " "
        sb36 += str(args[2])
        sb36 += " "
        sb36 += str(args[3])
        sb36 += " "
        sb36 += str(args[0])
        sb36 += " "
    elif x == 37:
        sb37 += str(args[1])
        sb37 += " "
        sb37 += str(args[2])
        sb37 += " "
        sb37 += str(args[3])
        sb37 += " "
        sb37 += str(args[0])
        sb37 += " "
    elif x == 38:
        sb38 += str(args[1])
        sb38 += " "
        sb38 += str(args[2])
        sb38 += " "
        sb38 += str(args[3])
        sb38 += " "
        sb38 += str(args[0])
        sb38 += " "
    elif x == 39:
        sb39 += str(args[1])
        sb39 += " "
        sb39 += str(args[2])
        sb39 += " "
        sb39 += str(args[3])
        sb39 += " "
        sb39 += str(args[0])
        sb39 += " "
    elif x == 40:
        sb40 += str(args[1])
        sb40 += " "
        sb40 += str(args[2])
        sb40 += " "
        sb40 += str(args[3])
        sb40 += " "
        sb40 += str(args[0])
        sb40 += " "
    elif x == 41:
        sb41 += str(args[1])
        sb41 += " "
        sb41 += str(args[2])
        sb41 += " "
        sb41 += str(args[3])
        sb41 += " "
        sb41 += str(args[0])
        sb41 += " "
    elif x == 42:
        sb42 += str(args[1])
        sb42 += " "
        sb42 += str(args[2])
        sb42 += " "
        sb42 += str(args[3])
        sb42 += " "
        sb42 += str(args[0])
        sb42 += " "
    elif x == 43:
        sb43 += str(args[1])
        sb43 += " "
        sb43 += str(args[2])
        sb43 += " "
        sb43 += str(args[3])
        sb43 += " "
        sb43 += str(args[0])
        sb43 += " "
    elif x == 44:
        sb44 += str(args[1])
        sb44 += " "
        sb44 += str(args[2])
        sb44 += " "
        sb44 += str(args[3])
        sb44 += " "
        sb44 += str(args[0])
        sb44 += " "
    elif x == 45:
        sb45 += str(args[1])
        sb45 += " "
        sb45 += str(args[2])
        sb45 += " "
        sb45 += str(args[3])
        sb45 += " "
        sb45 += str(args[0])
        sb45 += " "
    elif x == 46:
        sb46 += str(args[1])
        sb46 += " "
        sb46 += str(args[2])
        sb46 += " "
        sb46 += str(args[3])
        sb46 += " "
        sb46 += str(args[0])
        sb46 += " "
    elif x == 47:
        sb47 += str(args[1])
        sb47 += " "
        sb47 += str(args[2])
        sb47 += " "
        sb47 += str(args[3])
        sb47 += " "
        sb47 += str(args[0])
        sb47 += " "
    elif x == 48:
        sb48 += str(args[1])
        sb48 += " "
        sb48 += str(args[2])
        sb48 += " "
        sb48 += str(args[3])
        sb48 += " "
        sb48 += str(args[0])
        sb48 += " "
    elif x == 49:
        sb49 += str(args[1])
        sb49 += " "
        sb49 += str(args[2])
        sb49 += " "
        sb49 += str(args[3])
        sb49 += " "
        sb49 += str(args[0])
        sb49 += " "
    elif x == 50:
        sb50 += str(args[1])
        sb50 += " "
        sb50 += str(args[2])
        sb50 += " "
        sb50 += str(args[3])
        sb50 += " "
        sb50 += str(args[0])
        sb50 += " "
    elif x == 51:
        sb51 += str(args[1])
        sb51 += " "
        sb51 += str(args[2])
        sb51 += " "
        sb51 += str(args[3])
        sb51 += " "
        sb51 += str(args[0])
        sb51 += " "
    elif x == 52:
        sb52 += str(args[1])
        sb52 += " "
        sb52 += str(args[2])
        sb52 += " "
        sb52 += str(args[3])
        sb52 += " "
        sb52 += str(args[0])
        sb52 += " "
    elif x == 53:
        sb53 += str(args[1])
        sb53 += " "
        sb53 += str(args[2])
        sb53 += " "
        sb53 += str(args[3])
        sb53 += " "
        sb53 += str(args[0])
        sb53 += " "
    elif x == 54:
        sb54 += str(args[1])
        sb54 += " "
        sb54 += str(args[2])
        sb54 += " "
        sb54 += str(args[3])
        sb54 += " "
        sb54 += str(args[0])
        sb54 += " "
    elif x == 55:
        sb55 += str(args[1])
        sb55 += " "
        sb55 += str(args[2])
        sb55 += " "
        sb55 += str(args[3])
        sb55 += " "
        sb55 += str(args[0])
        sb55 += " "
    elif x == 56:
        sb56 += str(args[1])
        sb56 += " "
        sb56 += str(args[2])
        sb56 += " "
        sb56 += str(args[3])
        sb56 += " "
        sb56 += str(args[0])
        sb56 += " "
    elif x == 57:
        sb57 += str(args[1])
        sb57 += " "
        sb57 += str(args[2])
        sb57 += " "
        sb57 += str(args[3])
        sb57 += " "
        sb57 += str(args[0])
        sb57 += " "
    elif x == 58:
        sb58 += str(args[1])
        sb58 += " "
        sb58 += str(args[2])
        sb58 += " "
        sb58 += str(args[3])
        sb58 += " "
        sb58 += str(args[0])
        sb58 += " "
    elif x == 59:
        sb59 += str(args[1])
        sb59 += " "
        sb59 += str(args[2])
        sb59 += " "
        sb59 += str(args[3])
        sb59 += " "
        sb59 += str(args[0])
        sb59 += " "
    elif x == 60:
        sb60 += str(args[1])
        sb60 += " "
        sb60 += str(args[2])
        sb60 += " "
        sb60 += str(args[3])
        sb60 += " "
        sb60 += str(args[0])
        sb60 += " "
    elif x == 61:
        sb61 += str(args[1])
        sb61 += " "
        sb61 += str(args[2])
        sb61 += " "
        sb61 += str(args[3])
        sb61 += " "
        sb61 += str(args[0])
        sb61 += " "
    elif x == 62:
        sb62 += str(args[1])
        sb62 += " "
        sb62 += str(args[2])
        sb62 += " "
        sb62 += str(args[3])
        sb62 += " "
        sb62 += str(args[0])
        sb62 += " "
    elif x == 63:
        sb63 += str(args[1])
        sb63 += " "
        sb63 += str(args[2])
        sb63 += " "
        sb63 += str(args[3])
        sb63 += " "
        sb63 += str(args[0])
        sb63 += " "
    elif x == 64:
        sb64 += str(args[1])
        sb64 += " "
        sb64 += str(args[2])
        sb64 += " "
        sb64 += str(args[3])
        sb64 += " "
        sb64 += str(args[0])
        sb64 += " "
    elif x == 65:
        sb65 += str(args[1])
        sb65 += " "
        sb65 += str(args[2])
        sb65 += " "
        sb65 += str(args[3])
        sb65 += " "
        sb65 += str(args[0])
        sb65 += " "
    elif x == 66:
        sb66 += str(args[1])
        sb66 += " "
        sb66 += str(args[2])
        sb66 += " "
        sb66 += str(args[3])
        sb66 += " "
        sb66 += str(args[0])
        sb66 += " "
                
    #print (user[2],args[0],args[1],args[2],args[3]) 

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
server.timeout = 0
run = True
server.handle_timeout = types.MethodType(handle_timeout, server)

server.addMsgHandler( "/AS/1", user_callback )
server.addMsgHandler( "/AS/2", user_callback )
server.addMsgHandler( "/AS/3", user_callback )
server.addMsgHandler( "/AS/4", user_callback )
server.addMsgHandler( "/AS/5", user_callback )
server.addMsgHandler( "/AS/6", user_callback )
server.addMsgHandler( "/AS/7", user_callback )
server.addMsgHandler( "/AS/8", user_callback )
server.addMsgHandler( "/AS/9", user_callback )
server.addMsgHandler( "/AS/10", user_callback )
server.addMsgHandler( "/AS/11", user_callback )
server.addMsgHandler( "/AS/12", user_callback )
server.addMsgHandler( "/AS/13", user_callback )
server.addMsgHandler( "/AS/14", user_callback )
server.addMsgHandler( "/AS/15", user_callback )
server.addMsgHandler( "/AS/16", user_callback )
server.addMsgHandler( "/AS/17", user_callback )
server.addMsgHandler( "/AS/18", user_callback )
server.addMsgHandler( "/AS/19", user_callback )
server.addMsgHandler( "/AS/20", user_callback )
server.addMsgHandler( "/AS/21", user_callback )
server.addMsgHandler( "/AS/22", user_callback )
server.addMsgHandler( "/AS/23", user_callback )
server.addMsgHandler( "/AS/24", user_callback )
server.addMsgHandler( "/AS/25", user_callback )
server.addMsgHandler( "/AS/26", user_callback )
server.addMsgHandler( "/AS/27", user_callback )
server.addMsgHandler( "/AS/28", user_callback )
server.addMsgHandler( "/AS/29", user_callback )
server.addMsgHandler( "/AS/30", user_callback )
server.addMsgHandler( "/AS/31", user_callback )
server.addMsgHandler( "/AS/32", user_callback )
server.addMsgHandler( "/AS/33", user_callback )
server.addMsgHandler( "/AS/34", user_callback )
server.addMsgHandler( "/AS/35", user_callback )
server.addMsgHandler( "/AS/36", user_callback )
server.addMsgHandler( "/AS/37", user_callback )
server.addMsgHandler( "/AS/38", user_callback )
server.addMsgHandler( "/AS/39", user_callback )
server.addMsgHandler( "/AS/40", user_callback )
server.addMsgHandler( "/AS/41", user_callback )
server.addMsgHandler( "/AS/42", user_callback )
server.addMsgHandler( "/AS/43", user_callback )
server.addMsgHandler( "/AS/44", user_callback )
server.addMsgHandler( "/AS/45", user_callback )
server.addMsgHandler( "/AS/46", user_callback )
server.addMsgHandler( "/AS/47", user_callback )
server.addMsgHandler( "/AS/48", user_callback )
server.addMsgHandler( "/AS/49", user_callback )
server.addMsgHandler( "/AS/50", user_callback )
server.addMsgHandler( "/AS/51", user_callback )
server.addMsgHandler( "/AS/52", user_callback )
server.addMsgHandler( "/AS/53", user_callback )
server.addMsgHandler( "/AS/54", user_callback )
server.addMsgHandler( "/AS/55", user_callback )
server.addMsgHandler( "/AS/56", user_callback )
server.addMsgHandler( "/AS/57", user_callback )
server.addMsgHandler( "/AS/58", user_callback )
server.addMsgHandler( "/AS/59", user_callback )
server.addMsgHandler( "/AS/60", user_callback )
server.addMsgHandler( "/AS/61", user_callback )
server.addMsgHandler( "/AS/62", user_callback )
server.addMsgHandler( "/AS/63", user_callback )
server.addMsgHandler( "/AS/64", user_callback )
server.addMsgHandler( "/AS/65", user_callback )
server.addMsgHandler( "/AS/66", user_callback )
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

# simulate a "game engine"
while run:
    # do the game stuff:
    time.sleep(sleeptime)
    # call user script
    each_frame()

server.close()
