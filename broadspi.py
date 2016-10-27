import socket  
import thread
import time
import os
from argparse import ArgumentParser
from moviepy.editor import VideoFileClip
import numpy as np
from PIL import Image
from tqdm import tqdm
from struct import *
def Threadfun1(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb1,sb2,sb3,sb4,sb5,sb6
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"
        
        time.sleep(sleeptime)

def Threadfun2(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb7,sb8,sb9,sb10,sb11,sb12
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def Threadfun3(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb13,sb14,sb15,sb16,sb17,sb18
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def Threadfun4(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb19,sb20,sb21,sb22,sb23,sb24
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def Threadfun5(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb25,sb26,sb27,sb28,sb29,sb30
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def Threadfun6(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb31,sb32,sb33,sb34,sb35,sb36
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def Threadfun7(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb37,sb38,sb39,sb40,sb41,sb42
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def Threadfun8(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb43,sb44,sb45,sb46,sb47,sb48
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def Threadfun9(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb49,sb50,sb51,sb52,sb53,sb54
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def Threadfun10(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb55,sb56,sb57,sb58,sb59,sb60
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def Threadfun11(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb61,sb62,sb63,sb64,sb65,sb66
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    B1 = False
    B2 = False
    B3 = False
    B4 = False
    B5 = False
    B6 = False
    while(True):
        if False == B1:
            try:
                s1.connect((string1, 6454))
                B1 = True
            except socket.error:
                pass
        else:
            end1 = len(sb1)
            if end1 > 6:
                s1.send(sb1)
        sb1 = "artnet"
        if False == B2:
            try:
                s2.connect((string2, 6454))
                B2 = True
            except socket.error:
                pass
        else:
            end2 = len(sb2)
            if end2 > 6:
                s2.send(sb2)
        sb2 = "artnet"
        if False == B3:
            try:
                s3.connect((string3, 6454))
                B3 = True
            except socket.error:
                pass
        else:
            end3 = len(sb3)
            if end3 > 6:
                s3.send(sb3)
        sb3 = "artnet"
        if False == B4:
            try:
                s4.connect((string4, 6454))
                B4 = True
            except socket.error:
                pass
        else:
            end4 = len(sb4)
            if end4 > 6:
                s4.send(sb4)
        sb4 = "artnet"
        if False == B5:
            try:
                s5.connect((string5, 6454))
                B5 = True
            except socket.error:
                pass
        else:
            end5 = len(sb5)
            if end5 > 6:
                s5.send(sb5)
        sb5 = "artnet"
        if False == B6:
            try:
                s6.connect((string6, 6454))
                B6 = True
            except socket.error:
                pass
        else:
            end6 = len(sb6)
            if end6 > 6:
                s6.send(sb6)
        sb6 = "artnet"

        time.sleep(sleeptime)

def frange(x, y, inc):
    while x < y:
        yield x
        x += inc


def average_video(filepath, outpath, start=None, end=None, sample_every=1):
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
    """Calculate average of video frames"""

    # Load video
    vid = VideoFileClip(filepath, audio=False).resize(width=66)
    width = vid.w
    height = vid.h

    if start is None and end is None:
        frame_generator = vid.iter_frames(progress_bar=True, dtype=np.uint8)
    else:
        if start is None:
            start = 0
        if end is None:
            end = vid.duration
        # compute time increment for sampling by frames
        sample_inc = sample_every / vid.fps
        frame_generator = tqdm(vid.get_frame(f) for f in frange(start, end, sample_inc))

    # create starting matrix of zeros
    sum_fs = np.zeros(shape=(height, width, 3), dtype=int)
    ma_sum_fs = np.zeros(shape=(height, width, 3), dtype=int)
    prev_f = np.zeros(shape=(height, width, 3), dtype=int)
    sum_delta_fs = np.zeros(shape=(height, width, 3), dtype=int)

    n_frames = 0
    for f in frame_generator:
        #delta = f - prev_f
        #sum_delta_fs += delta
        #sum_fs += f

        #ma_sum_fs += f
        #if divmod(n_frames, 100)[1] == 0 and n_frames > 0:
        #    ma_f = ma_sum_fs / 100
        #    Image.fromarray(ma_f.astype(np.uint8))\
        #        .save(os.path.join(outpath, 'movavg_{}.png'.format(n_frames)))
        #    ma_sum_fs = np.zeros(shape=(height, width, 3), dtype=int)

        #n_frames += 1
        #prev_f = f
        
        #print len(f[0])
        for x in range(1,len(f[0])+1):
            for y in range(0,len(f)):
                if y < 41:
                    r = f[y][x-1][0]
                    g = f[y][x-1][1]
                    b = f[y][x-1][2]
                    if x == 1:
                        sb1 += pack('BBBBB', r, g, b, y, x)
                    elif x == 2:
                        sb2 += pack('BBBBB', r, g, b, y, x)
                    elif x == 3:
                        sb3 += pack('BBBBB', r, g, b, y, x)
                    elif x == 4:
                        sb4 += pack('BBBBB', r, g, b, y, x)
                    elif x == 5:
                        sb5 += pack('BBBBB', r, g, b, y, x)
                    elif x == 6:
                        sb6 += pack('BBBBB', r, g, b, y, x)
                    elif x == 7:
                        sb7 += pack('BBBBB', r, g, b, y, x)
                    elif x == 8:
                        sb8 += pack('BBBBB', r, g, b, y, x)
                    elif x == 9:
                        sb9 += pack('BBBBB', r, g, b, y, x)
                    elif x == 10:
                        sb10 += pack('BBBBB', r, g, b, y, x)
                    elif x == 11:
                        sb11 += pack('BBBBB', r, g, b, y, x)
                    elif x == 12:
                        sb12 += pack('BBBBB', r, g, b, y, x)
                    elif x == 13:
                        sb13 += pack('BBBBB', r, g, b, y, x)
                    elif x == 14:
                        sb14 += pack('BBBBB', r, g, b, y, x)
                    elif x == 15:
                        sb15 += pack('BBBBB', r, g, b, y, x)
                    elif x == 16:
                        sb16 += pack('BBBBB', r, g, b, y, x)
                    elif x == 17:
                        sb17 += pack('BBBBB', r, g, b, y, x)
                    elif x == 18:
                        sb18 += pack('BBBBB', r, g, b, y, x)
                    elif x == 19:
                        sb19 += pack('BBBBB', r, g, b, y, x)
                    elif x == 20:
                        sb20 += pack('BBBBB', r, g, b, y, x)
                    elif x == 21:
                        sb21 += pack('BBBBB', r, g, b, y, x)
                    elif x == 22:
                        sb22 += pack('BBBBB', r, g, b, y, x)
                    elif x == 23:
                        sb23 += pack('BBBBB', r, g, b, y, x)
                    elif x == 24:
                        sb24 += pack('BBBBB', r, g, b, y, x)
                    elif x == 25:
                        sb25 += pack('BBBBB', r, g, b, y, x)
                    elif x == 26:
                        sb26 += pack('BBBBB', r, g, b, y, x)
                    elif x == 27:
                        sb27 += pack('BBBBB', r, g, b, y, x)
                    elif x == 28:
                        sb28 += pack('BBBBB', r, g, b, y, x)
                    elif x == 29:
                        sb29 += pack('BBBBB', r, g, b, y, x)
                    elif x == 30:
                        sb30 += pack('BBBBB', r, g, b, y, x)
                    elif x == 31:
                        sb31 += pack('BBBBB', r, g, b, y, x)
                    elif x == 32:
                        sb32 += pack('BBBBB', r, g, b, y, x)
                    elif x == 33:
                        sb33 += pack('BBBBB', r, g, b, y, x)
                    elif x == 34:
                        sb34 += pack('BBBBB', r, g, b, y, x)
                    elif x == 35:
                        sb35 += pack('BBBBB', r, g, b, y, x)
                    elif x == 36:
                        sb36 += pack('BBBBB', r, g, b, y, x)
                    elif x == 37:
                        sb37 += pack('BBBBB', r, g, b, y, x)
                    elif x == 38:
                        sb38 += pack('BBBBB', r, g, b, y, x)
                    elif x == 39:
                        sb39 += pack('BBBBB', r, g, b, y, x)
                    elif x == 40:
                        sb40 += pack('BBBBB', r, g, b, y, x)
                    elif x == 41:
                        sb41 += pack('BBBBB', r, g, b, y, x)
                    elif x == 42:
                        sb42 += pack('BBBBB', r, g, b, y, x)
                    elif x == 43:
                        sb43 += pack('BBBBB', r, g, b, y, x)
                    elif x == 44:
                        sb44 += pack('BBBBB', r, g, b, y, x)
                    elif x == 45:
                        sb45 += pack('BBBBB', r, g, b, y, x)
                    elif x == 46:
                        sb46 += pack('BBBBB', r, g, b, y, x)
                    elif x == 47:
                        sb47 += pack('BBBBB', r, g, b, y, x)
                    elif x == 48:
                        sb48 += pack('BBBBB', r, g, b, y, x)
                    elif x == 49:
                        sb49 += pack('BBBBB', r, g, b, y, x)
                    elif x == 50:
                        sb50 += pack('BBBBB', r, g, b, y, x)
                    elif x == 51:
                        sb51 += pack('BBBBB', r, g, b, y, x)
                    elif x == 52:
                        sb52 += pack('BBBBB', r, g, b, y, x)
                    elif x == 53:
                        sb53 += pack('BBBBB', r, g, b, y, x)
                    elif x == 54:
                        sb54 += pack('BBBBB', r, g, b, y, x)
                    elif x == 55:
                        sb55 += pack('BBBBB', r, g, b, y, x)
                    elif x == 56:
                        sb56 += pack('BBBBB', r, g, b, y, x)
                    elif x == 57:
                        sb57 += pack('BBBBB', r, g, b, y, x)
                    elif x == 58:
                        sb58 += pack('BBBBB', r, g, b, y, x)
                    elif x == 59:
                        sb59 += pack('BBBBB', r, g, b, y, x)
                    elif x == 60:
                        sb60 += pack('BBBBB', r, g, b, y, x)
                    elif x == 61:
                        sb61 += pack('BBBBB', r, g, b, y, x)
                    elif x == 62:
                        sb62 += pack('BBBBB', r, g, b, y, x)
                    elif x == 63:
                        sb63 += pack('BBBBB', r, g, b, y, x)
                    elif x == 64:
                        sb64 += pack('BBBBB', r, g, b, y, x)
                    elif x == 65:
                        sb65 += pack('BBBBB', r, g, b, y, x)
                    elif x == 66:
                        sb66 += pack('BBBBB', r, g, b, y, x)
                                
        time.sleep(1.0/float(sample_every))

    # average out the values for each frame
    #average_delta_f = sum_delta_fs / n_frames
    #average_f = sum_fs / n_frames

    # Create images
    #delta_img = Image.fromarray(average_delta_f.astype(np.uint8))
    #delta_img.save(os.path.join(outpath, 'average_delta.png'))
    #final_img = Image.fromarray(average_f.astype(np.uint8))
    #final_img.save(os.path.join(outpath, 'average.png'))


#address = ('0.0.0.0', 6454)  
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
#s.bind(address)  

#data = ""
sleeptime = 0.001

sb1="artnet"
sb2="artnet"
sb3="artnet"
sb4="artnet"
sb5="artnet"
sb6="artnet"
sb7="artnet"
sb8="artnet"
sb9="artnet"
sb10="artnet"
sb11="artnet"
sb12="artnet"
sb13="artnet"
sb14="artnet"
sb15="artnet"
sb16="artnet"
sb17="artnet"
sb18="artnet"
sb19="artnet"
sb20="artnet"
sb21="artnet"
sb22="artnet"
sb23="artnet"
sb24="artnet"
sb25="artnet"
sb26="artnet"
sb27="artnet"
sb28="artnet"
sb29="artnet"
sb30="artnet"
sb31="artnet"
sb32="artnet"
sb33="artnet"
sb34="artnet"
sb35="artnet"
sb36="artnet"
sb37="artnet"
sb38="artnet"
sb39="artnet"
sb40="artnet"
sb41="artnet"
sb42="artnet"
sb43="artnet"
sb44="artnet"
sb45="artnet"
sb46="artnet"
sb47="artnet"
sb48="artnet"
sb49="artnet"
sb50="artnet"
sb51="artnet"
sb52="artnet"
sb53="artnet"
sb54="artnet"
sb55="artnet"
sb56="artnet"
sb57="artnet"
sb58="artnet"
sb59="artnet"
sb60="artnet"
sb61="artnet"
sb62="artnet"
sb63="artnet"
sb64="artnet"
sb65="artnet"
sb66="artnet"

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

parser = ArgumentParser(description="Creates image with averaged pixels"
                                        "for a given movie clip")
parser.add_argument("-i", default="video_effect_for_light.mov", type=str,
                        help="filepath to movie clip")
parser.add_argument("-o", default="/home/oem/Shanghai/", type=str,
                        help="filepath to save image to")
parser.add_argument("-s", type=int, required=False,
                        help="Start time for image processing, in seconds")
parser.add_argument("-e", type=int, required=False,
                        help="End time for image processing, in seconds")
parser.add_argument("-f", type=int, default=5,
                        help="Sample every f frames (default 24)")
args = parser.parse_args()
    
while True:  
    average_video(args.i, args.o, args.s, args.e, args.f)
       
#s.close()  
