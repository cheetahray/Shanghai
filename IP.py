# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *
from threading import Thread
from OSC import *
from datetime import datetime

# LED strip configuration:
LED_COUNT      = 32      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
BrightList = 255
RList = []
GList = []
BList = []
wait_ms_breathe = 0.5
wait_ms_round = 1.0
howmanytail = 2
roundpos = -1
breathonoff = False
breathdirection = 1

server = OSCServer( ("0.0.0.0", 6666) )
server.timeout = 0.01
run = True

def handle_timeout(self):
    self.timed_out = True

server.handle_timeout = types.MethodType(handle_timeout, server)

def breathe():
    global strip
    global BrightList,RList,GList,BList
    global LED_COUNT
    global breathonoff
    global wait_ms_breathe
    global breathdirection
    while True == breathonoff:
        if BrightList >= 255:
            breathdirection = -1
        elif BrightList <= 0:
            breathdirection = 1
        if breathdirection == 1:
            BrightList = BrightList+1
        elif breathdirection == -1:
            BrightList = BrightList-1
        strip.setBrightness(BrightList);
        if roundpos < 0:
            for j in range(LED_COUNT):
                strip.setPixelColor(j, wheel(j))
            strip.show()
        time.sleep(wait_ms_breathe / 255.0)

def breathe_callback(path, tags, args, source):
    global wait_ms_breathe
    global breathonoff
    if args[0] == 0.0:
        breathonoff = False
    elif args[0] == 1.0:
        if len(args) == 2:
            wait_ms_breathe = float(args[1]) * 0.27260029
            if wait_ms_breathe < 0.255:
                wait_ms_breathe = 0.255
        if breathonoff == False:
            breathonoff = True
            threading.Thread( target = breathe ).start()
        
def roundround():
    global strip
    global BrightList,RList,GList,BList
    global LED_COUNT
    global roundpos
    global wait_ms_round
    global howmanytail
    while 0 <= roundpos:
        for j in range(0, LED_COUNT):
            mytail = roundpos - howmanytail
            if mytail < 0:
                mytail = mytail + LED_COUNT
                if j <= roundpos or j > mytail:
                    strip.setPixelColor(j, wheel(j))
                else:
                    strip.setPixelColor(j, 0)
            else:
                if j == roundpos:
                    strip.setPixelColor(j, wheel(j))
                elif j <= mytail:
                    strip.setPixelColor(j, 0)
        strip.show()
        time.sleep( wait_ms_round / float(LED_COUNT+1) )
        roundpos = roundpos + 1
        if roundpos == LED_COUNT:
            roundpos = 0

def round_callback(path, tags, args, source):
    global wait_ms_round
    global roundpos
    global howmanytail
    if args[0] == 0.0:
        roundpos = -2
    elif args[0] == 1.0:
        if len(args) >= 2:
            wait_ms_round = float(args[1])
            if wait_ms_round < 0.01:
                wait_ms_round = 0.01
            if len(args) == 3:
                howmanytail = int(args[2])
        if roundpos <= -1:                
            roundpos = 0
            threading.Thread( target = roundround ).start()

def rgb_callback(path, tags, args, source):
    global RList,GList,BList
    mylen = len(args)
    if mylen >= 3:
        for j in range(LED_COUNT):
            my3 = j%(mylen/3)
            RList[j] = args[my3]
            GList[j] = args[my3+1]
            BList[j] = args[my3+2]
            if roundpos < 0 and breathonoff == False:
                strip.setPixelColor(j, wheel(j))
        strip.show()

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

def wheel(pos):
    return Color( RList[pos] , GList[pos] , BList[pos] )
    
# Main program logic follows:
#if __name__ == '__main__':

for ii in range(LED_COUNT):
    RList.append(255)
    GList.append(255)
    BList.append(255)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

print ('Press Ctrl-C to quit.')

server.addMsgHandler( "/breathe", breathe_callback )
server.addMsgHandler( "/round", round_callback )
server.addMsgHandler( "/RGB", rgb_callback )

try:
    while run:
        # do the game stuff:
        #sleep(1)
        # call user script
        each_frame()

    server.close()

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
