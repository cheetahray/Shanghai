import socket
import struct
from struct import *
from OSC import *
import time
import random
import datetime
import thread
from threading import Thread, Event, Timer

def TimerReset(*args, **kwargs):
    """ Global function for Timer """
    return _TimerReset(*args, **kwargs)


class _TimerReset(Thread):
    """Call a function after a specified number of seconds:

    t = TimerReset(30.0, f, args=[], kwargs={})
    t.start()
    t.cancel() # stop the timer's action if it's still waiting
    """

    def __init__(self, interval, function, args=[], kwargs={}):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()
        self.resetted = True

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.finished.set()

    def run(self):
        print "Time: %s - timer running..." % time.asctime()

        while self.resetted:
            print "Time: %s - timer waiting for timeout in %.2f..." % (time.asctime(), self.interval)
            self.resetted = False
            self.finished.wait(self.interval)

        if not self.finished.isSet():
            self.function(*self.args, **self.kwargs)
        self.finished.set()
        print "Time: %s - timer finished!" % time.asctime()

    def reset(self, interval=None):
        """ Reset the timer """

        if interval:
            print "Time: %s - timer resetting to %.2f..." % (time.asctime(), interval)
            self.interval = interval
        else:
            print "Time: %s - timer resetting..." % time.asctime()

        self.resetted = True
        self.finished.set()
        self.finished.clear()

cc = OSCClient()
cc.connect(('127.0.0.1', 20000))   # localhost, port 57120

grp = [
      [114,113,112,111,133,155,156,157,158,180,202,201,179,178,200,177,199,221,243,244,245],[332,333,311,310,288,289],[93,94,95,116],
      [337,338,316,315,293,294,272,271,248,249,250,251,228,227,205,206,184,183,161,162,140,139],[120,121,122,145,144,143,142,141,164,165,166],
      [232,253,254,255,276],[344,322,321,343,342],[13,14,36,35,57,58],[39,60,61,62,83],[193,194,195,173,172,171,149,150,151,147,169,191,197,175],
      [20,21,43,42],[66,88,87,86,108,130,131,109,110,132,154],     
      [370,363,369,375,368,361,367,373,372,366,360,359,365,371],[400,399,392,398,404,397,396,390,389,395,401,402]
      ]

grp2 = [
      [],[],[],
      [],[],[],[],[],
      [],[],[],
      [],[],[]
      ]

grpbool = [
      [],[],[],
      [],[],[],[],[],
      [],[],[],
      [],[],[]
      ]
'''
temp = [ 
      [],[],[],
      [],[],[],[],[],
      [],[],[],
      [],[],[]
      ]
'''
cntlist = [
      0,0,0,
      0,0,0,0,0,
      0,0,0,
      0,0,0
      ]

emd8216 = [
      [ 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 34, 35, 36, 37, 38],
      [ 39, 40, 41, 42, 43, 44, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65],
      [ 66, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92],
      [ 93, 94, 95, 96, 97, 98, 99,100,101,102,103,104,105,106,107,108],
      [109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124],
      [125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140],
      [141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156],
      [157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172],
      [173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188],
      [189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204],
      [205,206,207,208,209,210,211,212,221,222,223,224,225,226,227,228],
      [229,230,231,232,233,234,243,244,245,246,247,248,249,250,251,252],
      [253,254,255,256,265,266,267,268,269,270,271,272,273,274,275,276],
      [277,278,287,288,289,290,291,292,293,294,295,296,297,298,299,300],
      [309,310,311,312,313,314,315,316,317,318,319,320,321,322,331,332],
      [333,334,335,336,337,338,339,340,341,342,343,344,999,999,999,999],
      [353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368],
      [369,370,371,372,373,374,375,376,377,378,379,380,381,382,999,999],
      [383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398],
      [399,400,401,402,403,404,405,406,407,408,409,410,411,412,999,999]
      ]      
      
#aa = [datetime.datetime.now()] * len(grp)

TT = [ 
      None,None,None,
      None,None,None,None,None,
      None,None,None,
      None,None,None
      ]

IN = [ 
      False,False,False,
      False,False,False,False,False,
      False,False,False,
      False,False,False
      ]

def tensec(idx,idx2):
    cntlist[idx] = 0
    IN[idx] = False
    
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
            return i
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        #else:
    #print '{item} not found in the list from {j}'.format(item=item, j=idx)
    return -1 

def click(msg, val):
    global cc
    mymsg = "/" + msg
    oscmsg = OSCMessage()
    #print "%s" % (mymsg)
    oscmsg.setAddress("%s" % (mymsg) )
    oscmsg.append(val)
    print oscmsg
    cc.send(oscmsg)

def releasejump(item, forfrom, forto):
    for ii in range(forfrom, forto):
        index = binary_search(grp2[ii], item, ii)
        if index >= 0:
            #if True == grpbool[ii][index]:
            grpbool[ii][index] = False

def shiftcheck(item, forfrom, forto):
    smallii = -1
    for ii in range(forfrom, forto):
        index = binary_search(grp2[ii], item, ii)
        if index >= 0:
            if False == grpbool[ii][index]:
                if 0 == cntlist[ii]:
                    TT[ii] = TimerReset(10, tensec, (ii,ii))
                    TT[ii].start()
                else:
                    TT[ii].reset()
                grpbool[ii][index] = True
                if False == IN[smallii]:
                    IN[smallii] = True
                    smallii = ii
                
            #aa[ii] = datetime.datetime.now()
            '''            
            try:
                if temp[ii].index(item) >= 0:
                    pass
            except ValueError, e:
                if( grp[ii].index(item) == len(temp[ii]) ):    
                    temp[ii].append(item)
                    if 0 == cmp(temp[ii], grp[ii]):
                        print "Middle Arena", ii
                        click("/ME", ii)
                        del temp[ii][:]
                        print temp
            ''' 
        '''            
        else:    
            cc = datetime.datetime.now() - aa[ii]
            if cc.seconds > 3:
                #del temp[ii][:]
                cntlist[ii] = 0
                print cc.seconds
        '''
    if smallii >= 0:
        arena = 4
        cntlist[smallii]+=1
        print cntlist
        if len(grp2[smallii]) == cntlist[smallii]:
            print "Middle Arena", smallii + arena
            click("ME", smallii + arena)
            cntlist[smallii] = 0
            TT[smallii].cancel()
        else:                
            print "Small Arena", smallii+arena
            click("SE", smallii+arena)
        
def each_frame(leftfrom, rightto):
    while True:
        for ii in range( leftfrom, rightto ):
            try:
                if 0 == leftfrom:
                    port.sendto( pack('15sb32b', 'EMD821612345678',mycmd,127,127,127,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), thetuple[ii] )
                    rcv, addr = port.recvfrom(64)
                else:
                    port2.sendto( pack('15sb32b', 'EMD821612345678',mycmd,127,127,127,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), thetuple[ii] )
                    rcv, addr = port2.recvfrom(64)
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
                            if emd8216[ii][jj] == 999:
                                pass
                            elif 1 == bit:
                                #print thetuple[ii]
                                #print 'IO_0{0}'.format(jj)
                                shiftcheck(emd8216[ii][jj],0,len(grp))
                                #print "Small Arena", emd8216[ii][jj]
                                #click("SE", emd8216[ii][jj])
                            else:
                                releasejump(emd8216[ii][jj],0,len(grp))
                            num >>= 1            
                        num = ord( rcv[5] ) 
                        for jj in range(8,16): #17,16,15,14,13,12,11,10
                            bit = num & 1
                            if emd8216[ii][jj] == 999:
                                pass
                            elif 1 == bit:
                                #print thetuple[ii]
                                #print 'IO_1{0}'.format(jj)
                                shiftcheck(emd8216[ii][jj],0,len(grp))
                                #print "Small Arena", emd8216[ii][jj]
                                #click("SE", emd8216[ii][jj])
                            else:
                                releasejump(emd8216[ii][jj],0,len(grp))
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
                pass #print e
        for kk in range(0, len(IN)):
            IN[kk] = False
        
port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#port2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#EMD8308 IP Port
thetuple = [
            ("192.168.0.1", 6936), ("192.168.0.2", 6936), ("192.168.0.3", 6936), ("192.168.0.4", 6936), ("192.168.0.5", 6936),
            ("192.168.0.6", 6936), ("192.168.0.7", 6936), ("192.168.0.8", 6936), ("192.168.0.9", 6936), ("192.168.0.10",6936),
            ("192.168.0.11",6936), ("192.168.0.12",6936), ("192.168.0.13",6936), ("192.168.0.14",6936), ("192.168.0.15",6936),
            ("192.168.0.16",6936), ("192.168.0.17",6936), ("192.168.0.18",6936), ("192.168.0.19",6936), ("192.168.0.20",6936)
           ]
#Listen port
#port.bind(("0.0.0.0", 6936))
mycmd = 0x3D
port.settimeout(0.01)
#print grp
for ii in range(0,len(grp)):
    for jj in range(0,len(grp[ii])):
        grp2[ii].append(grp[ii][jj])
        grpbool[ii].append(False)
    grp2[ii].sort()
#print grp2
#print grpbool
while False:
    shiftcheck(random.randint(1,412),0,len(grp))

#thread.start_new_thread(each_frame,(0,len(thetuple)/2))

each_frame(0,len(thetuple))

