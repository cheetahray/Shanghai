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

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
            if args[0] == 131:
                if pickidx[3].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[3][args[1]]), ("192.168.12." + str(pickidx[3][args[1]]), 5005) )
                    del pickidx[3][args[1]]
            elif args[0] == 130:
                if pickidx[2].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[2][args[1]]), ("192.168.12." + str(pickidx[2][args[1]]), 5005) )
                    del pickidx[2][args[1]]
            elif args[0] == 129:
                if pickidx[1].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[1][args[1]]), ("192.168.12." + str(pickidx[1][args[1]]), 5005) )
                    del pickidx[1][args[1]]
            elif args[0] == 140:
                if pickidx[0].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[0][args[1]]), ("192.168.12." + str(pickidx[0][args[1]]), 5005) )
                    del pickidx[0][args[1]]
            elif args[0] == 139:
                if pickidx[7].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[7][args[1]]), ("192.168.12." + str(pickidx[7][args[1]]), 5005) )
                    del pickidx[7][args[1]]
                if pickidx[11].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[11][args[1]]), ("192.168.12." + str(pickidx[11][args[1]]), 5005) )
                    del pickidx[11][args[1]]
            elif args[0] == 138:
                if pickidx[6].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[6][args[1]]), ("192.168.12." + str(pickidx[6][args[1]]), 5005) )
                    del pickidx[6][args[1]]
                if pickidx[10].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[10][args[1]]), ("192.168.12." + str(pickidx[10][args[1]]), 5005) )
                    del pickidx[10][args[1]]
            elif args[0] == 137:
                if pickidx[5].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[5][args[1]]), ("192.168.12." + str(pickidx[5][args[1]]), 5005) )
                    del pickidx[5][args[1]]
                if pickidx[9].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[9][args[1]]), ("192.168.12." + str(pickidx[9][args[1]]), 5005) )
                    del pickidx[9][args[1]]
            elif args[0] == 136:
                if pickidx[4].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[4][args[1]]), ("192.168.12." + str(pickidx[4][args[1]]), 5005) )
                    del pickidx[4][args[1]]
                if pickidx[8].has_key(args[1]):
                    port.sendto("128 " + str(args[1]) + " 0 " + str(pickidx[8][args[1]]), ("192.168.12." + str(pickidx[8][args[1]]), 5005) )
                    del pickidx[8][args[1]]
            elif args[0] == 147:
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
    
    if True == isslider:
        for ii in range(27,41):
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

    for ii in range(27,41):
        port.sendto("249 1" , ("192.168.12." + str(ii), 5005))
        time.sleep(0.01)
       
    time.sleep(5)
        
def quit_callback(path, tags, args, source):
    # don't do this at home (or it'll quit blender)
    global run
    run = False

# user script that's called by the game engine every frame
def each_frame(*args):
    while True:
        # clear timed_out flag
        server.timed_out = False
        # handle all pending requests then return
        if not server.timed_out:
            server.handle_request()
        time.sleep(0.001)

server = OSCServer( ("0.0.0.0", 6666) )
server.timeout = 0.001
run = True
server.handle_timeout = types.MethodType(handle_timeout, server)

server.addMsgHandler( "/m", user_callback )
server.addMsgHandler( "/s", user_callback )
#server.addMsgHandler( "/quit", quit_callback )

data = ""
sleeptime = 0.001

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
    port.sendto("249 3", ("192.168.12." + str(i), 5005) )
    time.sleep(0.01)
for i in range(1,67):
    port.sendto("225 2", ("192.168.12." + str(i), 5005) )
    time.sleep(0.01)

thread.start_new_thread(each_frame)
    
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
                x = 1 # 1..66
                y = 0 #0..40
                while ((idx < (rgb_length+18)) and (x <= 66)):
                    
                    #print ("{0}, {1}, {2}, {3}, {4}".format(x, y, r, g, b) )  #unicorn.set_pixel(x, y, r, g, b)
                    if 0 == universe:
                        r = rawbytes[idx]
                        idx += 1
                        g = rawbytes[idx]
                        idx += 1
                        b = rawbytes[idx]
                        idx += 1
                        sb66 = "RGBW"
                        sb66 += str(r)
                        sb66 += " "
                        sb66 += str(g)
                        sb66 += " "
                        sb66 += str(b)
                        s1.sendto(sb66, ("192.168.12." + str(x) ,6454))
                    elif 1 == universe:
                        r = rawbytes[idx]
                        idx += 1
                        sb66 = "COLD"
                        sb66 += str(r)
                        s1.sendto(sb66, ("192.168.12." + str(x) ,6454))   
                    elif 2 == universe:
                        r = rawbytes[idx]
                        idx += 1
                        sb66 = "WARM"
                        sb66 += str(r)
                        s1.sendto(sb66, ("192.168.12." + str(x) ,6454))   
                         
                    x += 1    
    except socket.timeout:
        pass                    
    except ValueError:
        pass    
    except IndexError:
        pass
    #each_frame()

server.close()
