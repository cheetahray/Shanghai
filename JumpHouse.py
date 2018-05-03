import socket
import struct
from struct import *
from OSC import *
import time
import random
import datetime
cc = OSCClient()
cc.connect(('127.0.0.1', 20000))   # localhost, port 57120

grp = [
      [114,113,112,111,133,155,156,157,158,180,202,201,179,178,200,177,199,221,243,244,245],[93,94,95,116],[13,14,36,35,57,58],[39,60,61,62,83],[20,21,43,42],
      [66,88,87,86,108,130,131,109,110,132,154],[193,194,195,173,172,171,149,150,151],[120,121,122,145,144,143,142,141,164,165,166],[232,253,254,255,276],
      [344,322,321,343,342],[337,338,316,315,293,294,272,271,248,249,250,251,228,227,205,206,184,183,161,162,140,139],[332,333,311,310,288,289],
      [370,363,369,375,368,361,367,373,372,366,360,359,365,371],[400,399,392,398,404,397,396,390,389,395,401,402],[147,169,191],[197,175]
      ]

grp2 = [
      [],[],[],
      [],[],[],[],[],
      [],[],[],
      [],[],[],
      [],[]
      ]

temp = [ 
      [],[],[],
      [],[],[],[],[],
      [],[],[],
      [],[],[],
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

def shiftcheck(item, forfrom, forto):
    for ii in range(forfrom, forto):
        if True == binary_search(grp2[ii], item, ii):
            print "Small Arena", item
            click("/SE", item)
            aa[ii] = datetime.datetime.now()
            try:
                if temp[ii].index(item) >= 0:
                    pass
            except ValueError, e:
                if( grp[ii].index(item) == len(temp[ii]) )        
                    temp[ii].append(item)
                    if 0 == cmp(temp[ii], grp[ii]):
                        print "Middle Arena", ii
                        click("/ME", ii)
                        del temp[ii][:]
                        print temp
                                                    
        else:    
            cc = datetime.datetime.now() - aa[ii]
            #print cc.seconds
            if cc.seconds > 3:
                del temp[ii][:]
            
port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#EMD8308 IP Port
thetuple = [("192.168.11.217", 6936)]
#Listen port
#port.bind(("0.0.0.0", 6936))
mycmd = 0x3D
port.settimeout(0.01)

for ii in range(0,len(grp)):
    for jj in range(0,len(grp[ii])):
        grp2[ii].append(grp[ii][jj])
    grp2[ii].sort()

while False:
    shiftcheck(random.randint(1,412),0,len(grp))

while True:
    try:
        for ii in range( 0, len(thetuple) ):
            port.sendto( pack('15sb32b', 'EMD821612345678',mycmd,127,127,127,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), thetuple[ii] )
            #
            rcv, addr = port.recvfrom(1024)
            if( ord( rcv[33] ) == mycmd ):
                #print ("This Command")
                if( ord( rcv[32] ) == 0x63 ):
                    #print ("successful")
                    '''
                    for ii in range(0,8):
                        print hex( ord( rcv[ii] ) ),
                    print
                    '''
                    num = ord( rcv[4] )
                    for jj in range(0,8): #7,6,5,4,3,2,1,0
                        bit = num & 1
                        if 1 == bit:
                            print '0{0}'.format(jj)
                            shiftcheck(random.randint(1,412),0,len(grp))
                        num >>= 1            
                    num = ord( rcv[5] ) 
                    for jj in range(0,8): #17,16,15,14,13,12,11,10
                        bit = num & 1
                        if 1 == bit:
                            print '1{0}'.format(jj)
                            shiftcheck(random.randint(1,412),0,len(grp))
                        num >>= 1            
                    
                    #bb = struct.unpack('>f', struct.pack('4B', ord(rcv[11]), ord(rcv[10]), ord(rcv[9]), ord(rcv[8])))
                    #print bb
                    #click("chicken" ,bb)
                else:
                    print ("Fail")
                    print ( hex ( ord ( rcv[32] )  ) )
            else:
                print ("Not this command")
    except socket.timeout, e:
        pass
    #time.sleep(0.001)
