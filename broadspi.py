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
            sb1 = "artnet"
        if end2 > 6:
            s2.sendto(sb2, s2tuple)
            sb2 = "artnet"
        if end3 > 6:
            s3.sendto(sb3, s3tuple)
            sb3 = "artnet"
        if end4 > 6:
            s4.sendto(sb4, s4tuple)
            sb4 = "artnet"
        if end5 > 6:
            s5.sendto(sb5, s5tuple)
            sb5 = "artnet"
        if end6 > 6:
            s6.sendto(sb6, s6tuple)
            sb6 = "artnet"
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
            sb7 = "artnet"
        if end2 > 6:
            s2.sendto(sb8, s2tuple)
            sb8 = "artnet"
        if end3 > 6:
            s3.sendto(sb9, s3tuple)
            sb9 = "artnet"
        if end4 > 6:
            s4.sendto(sb10, s4tuple)
            sb10 = "artnet"
        if end5 > 6:
            s5.sendto(sb11, s5tuple)
            sb11 = "artnet"
        if end6 > 6:
            s6.sendto(sb12, s6tuple)
            sb12 = "artnet"
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
            sb13 = "artnet"
        if end2 > 6:
            s2.sendto(sb14, s2tuple)
            sb14 = "artnet"
        if end3 > 6:
            s3.sendto(sb15, s3tuple)
            sb15 = "artnet"
        if end4 > 6:
            s4.sendto(sb16, s4tuple)
            sb16 = "artnet"
        if end5 > 6:
            s5.sendto(sb17, s5tuple)
            sb17 = "artnet"
        if end6 > 6:
            s6.sendto(sb18, s6tuple)
            sb18 = "artnet"
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
            sb19 = "artnet"
        if end2 > 6:
            s2.sendto(sb20, s2tuple)
            sb20 = "artnet"
        if end3 > 6:
            s3.sendto(sb21, s3tuple)
            sb21 = "artnet"
        if end4 > 6:
            s4.sendto(sb22, s4tuple)
            sb22 = "artnet"
        if end5 > 6:
            s5.sendto(sb23, s5tuple)
            sb23 = "artnet"
        if end6 > 6:
            s6.sendto(sb24, s6tuple)
            sb24 = "artnet"
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
            sb25 = "artnet"
        if end2 > 6:
            s2.sendto(sb26, s2tuple)
            sb26 = "artnet"
        if end3 > 6:
            s3.sendto(sb27, s3tuple)
            sb27 = "artnet"
        if end4 > 6:
            s4.sendto(sb28, s4tuple)
            sb28 = "artnet"
        if end5 > 6:
            s5.sendto(sb29, s5tuple)
            sb29 = "artnet"
        if end6 > 6:
            s6.sendto(sb30, s6tuple)
            sb30 = "artnet"
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
            sb31 = "artnet"
        if end2 > 6:
            s2.sendto(sb32, s2tuple)
            sb32 = "artnet"
        if end3 > 6:
            s3.sendto(sb33, s3tuple)
            sb33 = "artnet"
        if end4 > 6:
            s4.sendto(sb34, s4tuple)
            sb34 = "artnet"
        if end5 > 6:
            s5.sendto(sb35, s5tuple)
            sb35 = "artnet"
        if end6 > 6:
            s6.sendto(sb36, s6tuple)
            sb36 = "artnet"
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
            sb37 = "artnet"
        if end2 > 6:
            s2.sendto(sb38, s2tuple)
            sb38 = "artnet"
        if end3 > 6:
            s3.sendto(sb39, s3tuple)
            sb39 = "artnet"
        if end4 > 6:
            s4.sendto(sb40, s4tuple)
            sb40 = "artnet"
        if end5 > 6:
            s5.sendto(sb41, s5tuple)
            sb41 = "artnet"
        if end6 > 6:
            s6.sendto(sb42, s6tuple)
            sb42 = "artnet"
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
            sb43 = "artnet"
        if end2 > 6:
            s2.sendto(sb44, s2tuple)
            sb44 = "artnet"
        if end3 > 6:
            s3.sendto(sb45, s3tuple)
            sb45 = "artnet"
        if end4 > 6:
            s4.sendto(sb46, s4tuple)
            sb46 = "artnet"
        if end5 > 6:
            s5.sendto(sb47, s5tuple)
            sb47 = "artnet"
        if end6 > 6:
            s6.sendto(sb48, s6tuple)
            sb48 = "artnet"
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
            sb49 = "artnet"
        if end2 > 6:
            s2.sendto(sb50, s2tuple)
            sb50 = "artnet"
        if end3 > 6:
            s3.sendto(sb51, s3tuple)
            sb51 = "artnet"
        if end4 > 6:
            s4.sendto(sb52, s4tuple)
            sb52 = "artnet"
        if end5 > 6:
            s5.sendto(sb53, s5tuple)
            sb53 = "artnet"
        if end6 > 6:
            s6.sendto(sb54, s6tuple)
            sb54 = "artnet"
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
            sb55 = "artnet"
        if end2 > 6:
            s2.sendto(sb56, s2tuple)
            sb56 = "artnet"
        if end3 > 6:
            s3.sendto(sb57, s3tuple)
            sb57 = "artnet"
        if end4 > 6:
            s4.sendto(sb58, s4tuple)
            sb58 = "artnet"
        if end5 > 6:
            s5.sendto(sb59, s5tuple)
            sb59 = "artnet"
        if end6 > 6:
            s6.sendto(sb60, s6tuple)
            sb60 = "artnet"
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
            sb61 = "artnet"
        if end2 > 6:
            s2.sendto(sb62, s2tuple)
            sb62 = "artnet"
        if end3 > 6:
            s3.sendto(sb63, s3tuple)
            sb63 = "artnet"
        if end4 > 6:
            s4.sendto(sb64, s4tuple)
            sb64 = "artnet"
        if end5 > 6:
            s5.sendto(sb65, s5tuple)
            sb65 = "artnet"
        if end6 > 6:
            s6.sendto(sb66, s6tuple)
            sb66 = "artnet"
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
                        sb1 += pack('BBBB', r, g, b, y)
                    elif x == 2:
                        sb2 += pack('BBBB', r, g, b, y)
                    elif x == 3:
                        sb3 += pack('BBBB', r, g, b, y)
                    elif x == 4:
                        sb4 += pack('BBBB', r, g, b, y)
                    elif x == 5:
                        sb5 += pack('BBBB', r, g, b, y)
                    elif x == 6:
                        sb6 += pack('BBBB', r, g, b, y)
                    elif x == 7:
                        sb7 += pack('BBBB', r, g, b, y)
                    elif x == 8:
                        sb8 += pack('BBBB', r, g, b, y)
                    elif x == 9:
                        sb9 += pack('BBBB', r, g, b, y)
                    elif x == 10:
                        sb10 += pack('BBBB', r, g, b, y)
                    elif x == 11:
                        sb11 += pack('BBBB', r, g, b, y)
                    elif x == 12:
                        sb12 += pack('BBBB', r, g, b, y)
                    elif x == 13:
                        sb13 += pack('BBBB', r, g, b, y)
                    elif x == 14:
                        sb14 += pack('BBBB', r, g, b, y)
                    elif x == 15:
                        sb15 += pack('BBBB', r, g, b, y)
                    elif x == 16:
                        sb16 += pack('BBBB', r, g, b, y)
                    elif x == 17:
                        sb17 += pack('BBBB', r, g, b, y)
                    elif x == 18:
                        sb18 += pack('BBBB', r, g, b, y)
                    elif x == 19:
                        sb19 += pack('BBBB', r, g, b, y)
                    elif x == 20:
                        sb20 += pack('BBBB', r, g, b, y)
                    elif x == 21:
                        sb21 += pack('BBBB', r, g, b, y)
                    elif x == 22:
                        sb22 += pack('BBBB', r, g, b, y)
                    elif x == 23:
                        sb23 += pack('BBBB', r, g, b, y)
                    elif x == 24:
                        sb24 += pack('BBBB', r, g, b, y)
                    elif x == 25:
                        sb25 += pack('BBBB', r, g, b, y)
                    elif x == 26:
                        sb26 += pack('BBBB', r, g, b, y)
                    elif x == 27:
                        sb27 += pack('BBBB', r, g, b, y)
                    elif x == 28:
                        sb28 += pack('BBBB', r, g, b, y)
                    elif x == 29:
                        sb29 += pack('BBBB', r, g, b, y)
                    elif x == 30:
                        sb30 += pack('BBBB', r, g, b, y)
                    elif x == 31:
                        sb31 += pack('BBBB', r, g, b, y)
                    elif x == 32:
                        sb32 += pack('BBBB', r, g, b, y)
                    elif x == 33:
                        sb33 += pack('BBBB', r, g, b, y)
                    elif x == 34:
                        sb34 += pack('BBBB', r, g, b, y)
                    elif x == 35:
                        sb35 += pack('BBBB', r, g, b, y)
                    elif x == 36:
                        sb36 += pack('BBBB', r, g, b, y)
                    elif x == 37:
                        sb37 += pack('BBBB', r, g, b, y)
                    elif x == 38:
                        sb38 += pack('BBBB', r, g, b, y)
                    elif x == 39:
                        sb39 += pack('BBBB', r, g, b, y)
                    elif x == 40:
                        sb40 += pack('BBBB', r, g, b, y)
                    elif x == 41:
                        sb41 += pack('BBBB', r, g, b, y)
                    elif x == 42:
                        sb42 += pack('BBBB', r, g, b, y)
                    elif x == 43:
                        sb43 += pack('BBBB', r, g, b, y)
                    elif x == 44:
                        sb44 += pack('BBBB', r, g, b, y)
                    elif x == 45:
                        sb45 += pack('BBBB', r, g, b, y)
                    elif x == 46:
                        sb46 += pack('BBBB', r, g, b, y)
                    elif x == 47:
                        sb47 += pack('BBBB', r, g, b, y)
                    elif x == 48:
                        sb48 += pack('BBBB', r, g, b, y)
                    elif x == 49:
                        sb49 += pack('BBBB', r, g, b, y)
                    elif x == 50:
                        sb50 += pack('BBBB', r, g, b, y)
                    elif x == 51:
                        sb51 += pack('BBBB', r, g, b, y)
                    elif x == 52:
                        sb52 += pack('BBBB', r, g, b, y)
                    elif x == 53:
                        sb53 += pack('BBBB', r, g, b, y)
                    elif x == 54:
                        sb54 += pack('BBBB', r, g, b, y)
                    elif x == 55:
                        sb55 += pack('BBBB', r, g, b, y)
                    elif x == 56:
                        sb56 += pack('BBBB', r, g, b, y)
                    elif x == 57:
                        sb57 += pack('BBBB', r, g, b, y)
                    elif x == 58:
                        sb58 += pack('BBBB', r, g, b, y)
                    elif x == 59:
                        sb59 += pack('BBBB', r, g, b, y)
                    elif x == 60:
                        sb60 += pack('BBBB', r, g, b, y)
                    elif x == 61:
                        sb61 += pack('BBBB', r, g, b, y)
                    elif x == 62:
                        sb62 += pack('BBBB', r, g, b, y)
                    elif x == 63:
                        sb63 += pack('BBBB', r, g, b, y)
                    elif x == 64:
                        sb64 += pack('BBBB', r, g, b, y)
                    elif x == 65:
                        sb65 += pack('BBBB', r, g, b, y)
                    elif x == 66:
                        sb66 += pack('BBBB', r, g, b, y)
                                
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
