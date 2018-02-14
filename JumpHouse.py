import socket
import struct
from struct import *
from OSC import *
import time
import random
import datetime
cc = OSCClient()
cc.connect(('192.168.11.128', 7777))   # localhost, port 57120

grp = [
      [147,169,191,175,197],[111,112,113,114,133,155,156,157,158,177,178,179,180,199,200,201,202,221,243,244,245],[93,94,95,116],
	  [13,14,35,36,57,58],[39,60,61,62,83],[20,21,42,43],[66,86,87,88,108,109,110,130,131,132,154],[149,150,151,171,172,173,193,194,195],
	  [120,121,122,141,142,143,144,145,164,165,166],[232,253,254,255,276],[321,322,342,343,344],
	  [139,140,161,162,183,184,205,206,227,228,248,249,250,251,271,272,293,294,315,316,337,338],[288,289,310,311,332,333],
	  [359,360,361,363,365,366,367,368,369,370,371,373,375],[389,390,392,395,396,397,398,399,400,401,402,404]
      ]

temp = [ 
      [],[],[],
	  [],[],[],[],[],
	  [],[],[],
	  [],[],
	  [],[]
      ]
      
aa = [datetime.datetime.now()] * len(grp)

def binary_search(a_list, item, idx):
    """Performs iterative binary search to find the position of an integer in a given, sorted, list.

    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """

    first = 0
    last = len(a_list) - 1

    while first <= last:
        i = (first + last) / 2
        #print a_list[i], item
        if a_list[i] == item:
            #print '{item} found at position {i} from {j}'.format(item=item, i=i, j=idx)
            return True
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        #else:
    #print '{item} not found in the list from {j}'.format(item=item, j=idx)
    return False 

def click(msg, val):
    global cc
    mymsg = "/" + msg
    oscmsg = OSCMessage()
    #print "%s" % (mymsg)
    oscmsg.setAddress("%s" % (mymsg) )
    oscmsg.append(val)
    cc.send(oscmsg)

while True:
    item = random.randint(1,412)
    for ii in range(0, len(grp)):
        if True == binary_search(grp[ii], item, ii):
            try:
                if temp[ii].index(item) >= 0:
                    pass
            except ValueError, e:
                aa[ii] = datetime.datetime.now()
                temp[ii].append(item)
                temp[ii].sort()
                if 0 == cmp(temp[ii], grp[ii]):
                    print "Middle Arena", ii
                    del temp[ii][:]
                    print temp            
        else:    
            cc = datetime.datetime.now() - aa[ii]
            #print cc.seconds
            if cc.microseconds > 2000:
                del temp[ii][:]
            
port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#EMD8308 IP Port
thetuple = ("192.168.11.217", 6936)
#Listen port
#port.bind(("0.0.0.0", 6936))
mycmd = 0x3D

while False:
    port.sendto( pack('15sb32b', 'EMD821612345678',mycmd,127,127,127,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), thetuple )
    #
    rcv, addr = port.recvfrom(1024)
    if( ord( rcv[33] ) == mycmd ):
        #print ("This Command")
        if( ord( rcv[32] ) == 0x63 ):
            #print ("successful")
            for ii in range(0,8):
                print hex( ord( rcv[ii] ) ),
                
            #bb = struct.unpack('>f', struct.pack('4B', ord(rcv[11]), ord(rcv[10]), ord(rcv[9]), ord(rcv[8])))
            #print bb
            #click("chicken" ,bb)
        else:
            print ("Fail")
            print ( hex ( ord ( rcv[32] )  ) )
    else:
        print ("Not this command")
    time.sleep(1)
