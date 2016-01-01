import socket  
import thread
import time

def Threadfun1(string1, string2, string3, string4, string5, string6, *args):
    global sleeptime
    global sb1,sb2,sb3,sb4,sb5,sb6
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while(True):
        if len(sb1) > 19:
            s1.sendto(sb1, (string1 ,6454) )
            sb1 = "artnet"
        if len(sb2) > 19:
            s2.sendto(sb2, (string2, 6454) )
            sb2 = "artnet"
        if len(sb3) > 19:
            s3.sendto(sb3, (string3, 6454) )
            sb3 = "artnet"
        if len(sb4) > 19:
            s4.sendto(sb4, (string4, 6454) )
            sb4 = "artnet"
        if len(sb5) > 19:
            s5.sendto(sb5, (string5, 6454) )
            sb5 = "artnet"
        if len(sb6) > 19:
            s6.sendto(sb6, (string6, 6454) )
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
    while(True):
        if len(sb7) > 19:
            s1.sendto(sb7, (string1 ,6454) )
            sb7 = "artnet"
        if len(sb8) > 19:
            s2.sendto(sb8, (string2, 6454) )
            sb8 = "artnet"
        if len(sb9) > 19:
            s3.sendto(sb9, (string3, 6454) )
            sb9 = "artnet"
        if len(sb10) > 19:
            s4.sendto(sb10, (string4, 6454) )
            sb10 = "artnet"
        if len(sb11) > 19:
            s5.sendto(sb11, (string5, 6454) )
            sb11 = "artnet"
        if len(sb12) > 19:
            s6.sendto(sb12, (string6, 6454) )
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
    while(True):
        if len(sb13) > 19:
            s1.sendto(sb13, (string1 ,6454) )
            sb13 = "artnet"
        if len(sb14) > 19:
            s2.sendto(sb14, (string2, 6454) )
            sb14 = "artnet"
        if len(sb15) > 19:
            s3.sendto(sb15, (string3, 6454) )
            sb15 = "artnet"
        if len(sb16) > 19:
            s4.sendto(sb16, (string4, 6454) )
            sb16 = "artnet"
        if len(sb17) > 19:
            s5.sendto(sb17, (string5, 6454) )
            sb17 = "artnet"
        if len(sb18) > 19:
            s6.sendto(sb18, (string6, 6454) )
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
    while(True):
        if len(sb19) > 19:
            s1.sendto(sb19, (string1 ,6454) )
            sb19 = "artnet"
        if len(sb20) > 19:
            s2.sendto(sb20, (string2, 6454) )
            sb20 = "artnet"
        if len(sb21) > 19:
            s3.sendto(sb21, (string3, 6454) )
            sb21 = "artnet"
        if len(sb22) > 19:
            s4.sendto(sb22, (string4, 6454) )
            sb22 = "artnet"
        if len(sb23) > 19:
            s5.sendto(sb23, (string5, 6454) )
            sb23 = "artnet"
        if len(sb24) > 19:
            s6.sendto(sb24, (string6, 6454) )
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
    while(True):
        if len(sb25) > 19:
            s1.sendto(sb25, (string1 ,6454) )
            sb25 = "artnet"
        if len(sb26) > 19:
            s2.sendto(sb26, (string2, 6454) )
            sb26 = "artnet"
        if len(sb27) > 19:
            s3.sendto(sb27, (string3, 6454) )
            sb27 = "artnet"
        if len(sb28) > 19:
            s4.sendto(sb28, (string4, 6454) )
            sb28 = "artnet"
        if len(sb29) > 19:
            s5.sendto(sb29, (string5, 6454) )
            sb29 = "artnet"
        if len(sb30) > 19:
            s6.sendto(sb30, (string6, 6454) )
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
    while(True):
        if len(sb31) > 19:
            s1.sendto(sb31, (string1 ,6454) )
            sb31 = "artnet"
        if len(sb32) > 19:
            s2.sendto(sb32, (string2, 6454) )
            sb32 = "artnet"
        if len(sb33) > 19:
            s3.sendto(sb33, (string3, 6454) )
            sb33 = "artnet"
        if len(sb34) > 19:
            s4.sendto(sb34, (string4, 6454) )
            sb34 = "artnet"
        if len(sb35) > 19:
            s5.sendto(sb35, (string5, 6454) )
            sb35 = "artnet"
        if len(sb36) > 19:
            s6.sendto(sb36, (string6, 6454) )
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
    while(True):
        if len(sb37) > 19:
            s1.sendto(sb37, (string1 ,6454) )
            sb37 = "artnet"
        if len(sb38) > 19:
            s2.sendto(sb38, (string2, 6454) )
            sb38 = "artnet"
        if len(sb39) > 19:
            s3.sendto(sb39, (string3, 6454) )
            sb39 = "artnet"
        if len(sb40) > 19:
            s4.sendto(sb40, (string4, 6454) )
            sb40 = "artnet"
        if len(sb41) > 19:
            s5.sendto(sb41, (string5, 6454) )
            sb41 = "artnet"
        if len(sb42) > 19:
            s6.sendto(sb42, (string6, 6454) )
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
    while(True):
        if len(sb43) > 19:
            s1.sendto(sb43, (string1 ,6454) )
            sb43 = "artnet"
        if len(sb44) > 19:
            s2.sendto(sb44, (string2, 6454) )
            sb44 = "artnet"
        if len(sb45) > 19:
            s3.sendto(sb45, (string3, 6454) )
            sb45 = "artnet"
        if len(sb46) > 19:
            s4.sendto(sb46, (string4, 6454) )
            sb46 = "artnet"
        if len(sb47) > 19:
            s5.sendto(sb47, (string5, 6454) )
            sb47 = "artnet"
        if len(sb48) > 19:
            s6.sendto(sb48, (string6, 6454) )
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
    while(True):
        if len(sb49) > 19:
            s1.sendto(sb49, (string1 ,6454) )
            sb49 = "artnet"
        if len(sb50) > 19:
            s2.sendto(sb50, (string2, 6454) )
            sb50 = "artnet"
        if len(sb51) > 19:
            s3.sendto(sb51, (string3, 6454) )
            sb51 = "artnet"
        if len(sb52) > 19:
            s4.sendto(sb52, (string4, 6454) )
            sb52 = "artnet"
        if len(sb53) > 19:
            s5.sendto(sb53, (string5, 6454) )
            sb53 = "artnet"
        if len(sb54) > 19:
            s6.sendto(sb54, (string6, 6454) )
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
    while(True):
        if len(sb55) > 19:
            s1.sendto(sb55, (string1 ,6454) )
            sb55 = "artnet"
        if len(sb56) > 19:
            s2.sendto(sb56, (string2, 6454) )
            sb56 = "artnet"
        if len(sb57) > 19:
            s3.sendto(sb57, (string3, 6454) )
            sb57 = "artnet"
        if len(sb58) > 19:
            s4.sendto(sb58, (string4, 6454) )
            sb58 = "artnet"
        if len(sb59) > 19:
            s5.sendto(sb59, (string5, 6454) )
            sb59 = "artnet"
        if len(sb60) > 19:
            s6.sendto(sb60, (string6, 6454) )
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
    while(True):
        if len(sb61) > 19:
            s1.sendto(sb61, (string1 ,6454) )
            sb61 = "artnet"
        if len(sb62) > 19:
            s2.sendto(sb62, (string2, 6454) )
            sb62 = "artnet"
        if len(sb63) > 19:
            s3.sendto(sb63, (string3, 6454) )
            sb63 = "artnet"
        if len(sb64) > 19:
            s4.sendto(sb64, (string4, 6454) )
            sb64 = "artnet"
        if len(sb65) > 19:
            s5.sendto(sb65, (string5, 6454) )
            sb65 = "artnet"
        if len(sb66) > 19:
            s6.sendto(sb66, (string6, 6454) )
            sb66 = "artnet"
        time.sleep(sleeptime)

address = ('0.0.0.0', 6454)  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s.bind(address)  

data = ""
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

while True:  
    data, addr = s.recvfrom(8192)  
    if ((len(data) > 19) and (data[0:8] == "Art-Net\x00")):
        rawbytes = map(ord, data)
        opcode = rawbytes[8] + (rawbytes[9] << 8)
        protocolVersion = (rawbytes[10] << 8) + rawbytes[11]
        if ((opcode == 0x5000) and (protocolVersion >= 14)):
            sub_net = (rawbytes[14] & 0xF0) >> 4
            universe = rawbytes[14] & 0x0F
            nowy = (sub_net << 4) + universe
            rgb_length = (rawbytes[16] << 8) + rawbytes[17]
            idx = 18
            x = 1
            y = nowy 
            while ((idx < (rgb_length+18)) ):
                if x == 1:
                    r = rawbytes[idx]
                    idx += 1
                    sb1 += str(r)
                    sb1 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb1 += str(g)
                    sb1 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb1 += str(b)
                    sb1 += " "
                    sb1 += str(y)
                elif x == 2:
                    r = rawbytes[idx]
                    idx += 1
                    sb2 += str(r)
                    sb2 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb2 += str(g)
                    sb2 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb2 += str(b)
                    sb2 += " "
                    sb2 += str(y)
                elif x == 3:
                    r = rawbytes[idx]
                    idx += 1
                    sb3 += str(r)
                    sb3 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb3 += str(g)
                    sb3 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb3 += str(b)
                    sb3 += " "
                    sb3 += str(y)
                elif x == 4:
                    r = rawbytes[idx]
                    idx += 1
                    sb4 += str(r)
                    sb4 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb4 += str(g)
                    sb4 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb4 += str(b)
                    sb4 += " "
                    sb4 += str(y)
                elif x == 5:
                    r = rawbytes[idx]
                    idx += 1
                    sb5 += str(r)
                    sb5 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb5 += str(g)
                    sb5 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb5 += str(b)
                    sb5 += " "
                    sb5 += str(y)
                elif x == 6:
                    r = rawbytes[idx]
                    idx += 1
                    sb6 += str(r)
                    sb6 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb6 += str(g)
                    sb6 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb6 += str(b)
                    sb6 += " "
                    sb6 += str(y)
                elif x == 7:
                    r = rawbytes[idx]
                    idx += 1
                    sb7 += str(r)
                    sb7 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb7 += str(g)
                    sb7 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb7 += str(b)
                    sb7 += " "
                    sb7 += str(y)
                elif x == 8:
                    r = rawbytes[idx]
                    idx += 1
                    sb8 += str(r)
                    sb8 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb8 += str(g)
                    sb8 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb8 += str(b)
                    sb8 += " "
                    sb8 += str(y)
                elif x == 9:
                    r = rawbytes[idx]
                    idx += 1
                    sb9 += str(r)
                    sb9 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb9 += str(g)
                    sb9 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb9 += str(b)
                    sb9 += " "
                    sb9 += str(y)
                elif x == 10:
                    r = rawbytes[idx]
                    idx += 1
                    sb10 += str(r)
                    sb10 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb10 += str(g)
                    sb10 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb10 += str(b)
                    sb10 += " "
                    sb10 += str(y)
                elif x == 11:
                    r = rawbytes[idx]
                    idx += 1
                    sb11 += str(r)
                    sb11 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb11 += str(g)
                    sb11 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb11 += str(b)
                    sb11 += " "
                    sb11 += str(y)
                elif x == 12:
                    r = rawbytes[idx]
                    idx += 1
                    sb12 += str(r)
                    sb12 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb12 += str(g)
                    sb12 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb12 += str(b)
                    sb12 += " "
                    sb12 += str(y)
                elif x == 13:
                    r = rawbytes[idx]
                    idx += 1
                    sb13 += str(r)
                    sb13 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb13 += str(g)
                    sb13 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb13 += str(b)
                    sb13 += " "
                    sb13 += str(y)
                elif x == 14:
                    r = rawbytes[idx]
                    idx += 1
                    sb14 += str(r)
                    sb14 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb14 += str(g)
                    sb14 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb14 += str(b)
                    sb14 += " "
                    sb14 += str(y)
                elif x == 15:
                    r = rawbytes[idx]
                    idx += 1
                    sb15 += str(r)
                    sb15 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb15 += str(g)
                    sb15 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb15 += str(b)
                    sb15 += " "
                    sb15 += str(y)
                elif x == 16:
                    r = rawbytes[idx]
                    idx += 1
                    sb16 += str(r)
                    sb16 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb16 += str(g)
                    sb16 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb16 += str(b)
                    sb16 += " "
                    sb16 += str(y)
                elif x == 17:
                    r = rawbytes[idx]
                    idx += 1
                    sb17 += str(r)
                    sb17 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb17 += str(g)
                    sb17 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb17 += str(b)
                    sb17 += " "
                    sb17 += str(y)
                elif x == 18:
                    r = rawbytes[idx]
                    idx += 1
                    sb18 += str(r)
                    sb18 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb18 += str(g)
                    sb18 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb18 += str(b)
                    sb18 += " "
                    sb18 += str(y)
                elif x == 19:
                    r = rawbytes[idx]
                    idx += 1
                    sb19 += str(r)
                    sb19 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb19 += str(g)
                    sb19 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb19 += str(b)
                    sb19 += " "
                    sb19 += str(y)
                elif x == 20:
                    r = rawbytes[idx]
                    idx += 1
                    sb20 += str(r)
                    sb20 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb20 += str(g)
                    sb20 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb20 += str(b)
                    sb20 += " "
                    sb20 += str(y)
                elif x == 21:
                    r = rawbytes[idx]
                    idx += 1
                    sb21 += str(r)
                    sb21 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb21 += str(g)
                    sb21 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb21 += str(b)
                    sb21 += " "
                    sb21 += str(y)
                elif x == 22:
                    r = rawbytes[idx]
                    idx += 1
                    sb22 += str(r)
                    sb22 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb22 += str(g)
                    sb22 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb22 += str(b)
                    sb22 += " "
                    sb22 += str(y)
                elif x == 23:
                    r = rawbytes[idx]
                    idx += 1
                    sb23 += str(r)
                    sb23 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb23 += str(g)
                    sb23 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb23 += str(b)
                    sb23 += " "
                    sb23 += str(y)
                elif x == 24:
                    r = rawbytes[idx]
                    idx += 1
                    sb24 += str(r)
                    sb24 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb24 += str(g)
                    sb24 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb24 += str(b)
                    sb24 += " "
                    sb24 += str(y)
                elif x == 25:
                    r = rawbytes[idx]
                    idx += 1
                    sb25 += str(r)
                    sb25 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb25 += str(g)
                    sb25 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb25 += str(b)
                    sb25 += " "
                    sb25 += str(y)
                elif x == 26:
                    r = rawbytes[idx]
                    idx += 1
                    sb26 += str(r)
                    sb26 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb26 += str(g)
                    sb26 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb26 += str(b)
                    sb26 += " "
                    sb26 += str(y)
                elif x == 27:
                    r = rawbytes[idx]
                    idx += 1
                    sb27 += str(r)
                    sb27 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb27 += str(g)
                    sb27 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb27 += str(b)
                    sb27 += " "
                    sb27 += str(y)
                elif x == 28:
                    r = rawbytes[idx]
                    idx += 1
                    sb28 += str(r)
                    sb28 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb28 += str(g)
                    sb28 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb28 += str(b)
                    sb28 += " "
                    sb28 += str(y)
                elif x == 29:
                    r = rawbytes[idx]
                    idx += 1
                    sb29 += str(r)
                    sb29 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb29 += str(g)
                    sb29 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb29 += str(b)
                    sb29 += " "
                    sb29 += str(y)
                elif x == 30:
                    r = rawbytes[idx]
                    idx += 1
                    sb30 += str(r)
                    sb30 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb30 += str(g)
                    sb30 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb30 += str(b)
                    sb30 += " "
                    sb30 += str(y)
                elif x == 31:
                    r = rawbytes[idx]
                    idx += 1
                    sb31 += str(r)
                    sb31 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb31 += str(g)
                    sb31 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb31 += str(b)
                    sb31 += " "
                    sb31 += str(y)
                elif x == 32:
                    r = rawbytes[idx]
                    idx += 1
                    sb32 += str(r)
                    sb32 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb32 += str(g)
                    sb32 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb32 += str(b)
                    sb32 += " "
                    sb32 += str(y)
                elif x == 33:
                    r = rawbytes[idx]
                    idx += 1
                    sb33 += str(r)
                    sb33 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb33 += str(g)
                    sb33 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb33 += str(b)
                    sb33 += " "
                    sb33 += str(y)
                elif x == 34:
                    r = rawbytes[idx]
                    idx += 1
                    sb34 += str(r)
                    sb34 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb34 += str(g)
                    sb34 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb34 += str(b)
                    sb34 += " "
                    sb34 += str(y)
                elif x == 35:
                    r = rawbytes[idx]
                    idx += 1
                    sb35 += str(r)
                    sb35 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb35 += str(g)
                    sb35 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb35 += str(b)
                    sb35 += " "
                    sb35 += str(y)
                elif x == 36:
                    r = rawbytes[idx]
                    idx += 1
                    sb36 += str(r)
                    sb36 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb36 += str(g)
                    sb36 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb36 += str(b)
                    sb36 += " "
                    sb36 += str(y)
                elif x == 37:
                    r = rawbytes[idx]
                    idx += 1
                    sb37 += str(r)
                    sb37 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb37 += str(g)
                    sb37 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb37 += str(b)
                    sb37 += " "
                    sb37 += str(y)
                elif x == 38:
                    r = rawbytes[idx]
                    idx += 1
                    sb38 += str(r)
                    sb38 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb38 += str(g)
                    sb38 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb38 += str(b)
                    sb38 += " "
                    sb38 += str(y)
                elif x == 39:
                    r = rawbytes[idx]
                    idx += 1
                    sb39 += str(r)
                    sb39 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb39 += str(g)
                    sb39 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb39 += str(b)
                    sb39 += " "
                    sb39 += str(y)
                elif x == 40:
                    r = rawbytes[idx]
                    idx += 1
                    sb40 += str(r)
                    sb40 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb40 += str(g)
                    sb40 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb40 += str(b)
                    sb40 += " "
                    sb40 += str(y)
                elif x == 41:
                    r = rawbytes[idx]
                    idx += 1
                    sb41 += str(r)
                    sb41 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb41 += str(g)
                    sb41 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb41 += str(b)
                    sb41 += " "
                    sb41 += str(y)
                elif x == 42:
                    r = rawbytes[idx]
                    idx += 1
                    sb42 += str(r)
                    sb42 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb42 += str(g)
                    sb42 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb42 += str(b)
                    sb42 += " "
                    sb42 += str(y)
                elif x == 43:
                    r = rawbytes[idx]
                    idx += 1
                    sb43 += str(r)
                    sb43 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb43 += str(g)
                    sb43 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb43 += str(b)
                    sb43 += " "
                    sb43 += str(y)
                elif x == 44:
                    r = rawbytes[idx]
                    idx += 1
                    sb44 += str(r)
                    sb44 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb44 += str(g)
                    sb44 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb44 += str(b)
                    sb44 += " "
                    sb44 += str(y)
                elif x == 45:
                    r = rawbytes[idx]
                    idx += 1
                    sb45 += str(r)
                    sb45 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb45 += str(g)
                    sb45 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb45 += str(b)
                    sb45 += " "
                    sb45 += str(y)
                elif x == 46:
                    r = rawbytes[idx]
                    idx += 1
                    sb46 += str(r)
                    sb46 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb46 += str(g)
                    sb46 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb46 += str(b)
                    sb46 += " "
                    sb46 += str(y)
                elif x == 47:
                    r = rawbytes[idx]
                    idx += 1
                    sb47 += str(r)
                    sb47 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb47 += str(g)
                    sb47 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb47 += str(b)
                    sb47 += " "
                    sb47 += str(y)
                elif x == 48:
                    r = rawbytes[idx]
                    idx += 1
                    sb48 += str(r)
                    sb48 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb48 += str(g)
                    sb48 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb48 += str(b)
                    sb48 += " "
                    sb48 += str(y)
                elif x == 49:
                    r = rawbytes[idx]
                    idx += 1
                    sb49 += str(r)
                    sb49 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb49 += str(g)
                    sb49 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb49 += str(b)
                    sb49 += " "
                    sb49 += str(y)
                elif x == 50:
                    r = rawbytes[idx]
                    idx += 1
                    sb50 += str(r)
                    sb50 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb50 += str(g)
                    sb50 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb50 += str(b)
                    sb50 += " "
                    sb50 += str(y)
                elif x == 51:
                    r = rawbytes[idx]
                    idx += 1
                    sb51 += str(r)
                    sb51 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb51 += str(g)
                    sb51 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb51 += str(b)
                    sb51 += " "
                    sb51 += str(y)
                elif x == 52:
                    r = rawbytes[idx]
                    idx += 1
                    sb52 += str(r)
                    sb52 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb52 += str(g)
                    sb52 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb52 += str(b)
                    sb52 += " "
                    sb52 += str(y)
                elif x == 53:
                    r = rawbytes[idx]
                    idx += 1
                    sb53 += str(r)
                    sb53 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb53 += str(g)
                    sb53 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb53 += str(b)
                    sb53 += " "
                    sb53 += str(y)
                elif x == 54:
                    r = rawbytes[idx]
                    idx += 1
                    sb54 += str(r)
                    sb54 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb54 += str(g)
                    sb54 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb54 += str(b)
                    sb54 += " "
                    sb54 += str(y)
                elif x == 55:
                    r = rawbytes[idx]
                    idx += 1
                    sb55 += str(r)
                    sb55 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb55 += str(g)
                    sb55 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb55 += str(b)
                    sb55 += " "
                    sb55 += str(y)
                elif x == 56:
                    r = rawbytes[idx]
                    idx += 1
                    sb56 += str(r)
                    sb56 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb56 += str(g)
                    sb56 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb56 += str(b)
                    sb56 += " "
                    sb56 += str(y)
                elif x == 57:
                    r = rawbytes[idx]
                    idx += 1
                    sb57 += str(r)
                    sb57 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb57 += str(g)
                    sb57 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb57 += str(b)
                    sb57 += " "
                    sb57 += str(y)
                elif x == 58:
                    r = rawbytes[idx]
                    idx += 1
                    sb58 += str(r)
                    sb58 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb58 += str(g)
                    sb58 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb58 += str(b)
                    sb58 += " "
                    sb58 += str(y)
                elif x == 59:
                    r = rawbytes[idx]
                    idx += 1
                    sb59 += str(r)
                    sb59 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb59 += str(g)
                    sb59 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb59 += str(b)
                    sb59 += " "
                    sb59 += str(y)
                elif x == 60:
                    r = rawbytes[idx]
                    idx += 1
                    sb60 += str(r)
                    sb60 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb60 += str(g)
                    sb60 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb60 += str(b)
                    sb60 += " "
                    sb60 += str(y)
                elif x == 61:
                    r = rawbytes[idx]
                    idx += 1
                    sb61 += str(r)
                    sb61 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb61 += str(g)
                    sb61 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb61 += str(b)
                    sb61 += " "
                    sb61 += str(y)
                elif x == 62:
                    r = rawbytes[idx]
                    idx += 1
                    sb62 += str(r)
                    sb62 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb62 += str(g)
                    sb62 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb62 += str(b)
                    sb62 += " "
                    sb62 += str(y)
                elif x == 63:
                    r = rawbytes[idx]
                    idx += 1
                    sb63 += str(r)
                    sb63 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb63 += str(g)
                    sb63 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb63 += str(b)
                    sb63 += " "
                    sb63 += str(y)
                elif x == 64:
                    r = rawbytes[idx]
                    idx += 1
                    sb64 += str(r)
                    sb64 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb64 += str(g)
                    sb64 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb64 += str(b)
                    sb64 += " "
                    sb64 += str(y)
                elif x == 65:
                    r = rawbytes[idx]
                    idx += 1
                    sb65 += str(r)
                    sb65 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb65 += str(g)
                    sb65 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb65 += str(b)
                    sb65 += " "
                    sb65 += str(y)
                elif x == 66:
                    r = rawbytes[idx]
                    idx += 1
                    sb66 += str(r)
                    sb66 += " "
                    g = rawbytes[idx]
                    idx += 1
                    sb66 += str(g)
                    sb66 += " "
                    b = rawbytes[idx]
                    idx += 1
                    sb66 += str(b)
                    sb66 += " "
                    sb66 += str(y)
                #print (str(x) + ":" + str(y))
                x += 1
                #if (x >= 66):
                #    x = 0
                #    y += 1
        
    time.sleep(sleeptime)
    
s.close()  