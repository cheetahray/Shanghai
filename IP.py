# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *
from threading import Thread
from OSC import *

# LED strip configuration:
LED_COUNT      = 32      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
BrightList = []
RList = []
GList = []
BList = []
wait_ms_breathe = 1
wait_ms_round = 1
howmanytail = 2
roundonoff = False
breathonoff = False

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
    """Movie theater light style chaser animation."""
    while True == breathonoff:
        for j in range(LED_COUNT):
            BrightList[j] = ((BrightList[j]+1) % 255) 
            strip.setPixelColor(j, wheel(j))
            strip.show()
            time.sleep(wait_ms_breathe / 255)

def breathe_callback(path, tags, args, source):
    global wait_ms_breathe
	global breathonoff
    if args[0] == 0.0:
        breathonoff = False
    elif args[0] == 1.0:
        if len(args) == 2:
		    wait_ms_breathe = float(args[1])
            if wait_ms_breathe < 0.255:
                wait_ms_breathe = 0.255
        if breathonoff == False:
            threading.Thread( target = roundround )	
        breathonoff = True        
        
def roundround():
    global strip
    global BrightList,RList,GList,BList
    global LED_COUNT
    global roundonoff
	global wait_ms_round
	global howmanytail
    """Movie theater light style chaser animation."""
    while True == roundonoff:
        for j in range(LED_COUNT):
            BrightList[j] = ((BrightList[j]+1) % 255) 
            strip.setPixelColor(j, wheel(j))
            strip.show()
            time.sleep( wait_ms_round * 1000 / (33-howmanytail) )
            if j-howmanytail+1 :
                strip.setPixelColor(j, 0)

def round_callback(path, tags, args, source):
    global wait_ms_round
	global roundonoff
    if args[0] == 0.0:
        roundonoff = False
    elif args[0] == 1.0:
        if len(args) >= 2:
		    wait_ms_round = float(args[1])
			if wait_ms_round < 0.01
		        wait_ms_round = 0.01
            if len(args) == 3:
			    howmanytail = int(args[2])
        if roundonoff == False:				
		    threading.Thread( target = roundround )
		roundonoff = True

def rgb_callback(path, tags, args, source):
    global RList,GList,BList
    r = int(arg[0])
	g = int(arg[1])
	b = int(arg[2])
    for ii in range(LED_COUNT):
        RList[ii] = r
        GList[ii] = g
        BList[ii] = b

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
    return Color(int(RList[pos] * BrightList[pos] / 255), int(GList[pos] * BrightList[pos] / 255), int(BList[pos] * BrightList[pos] / 255))
    
# Main program logic follows:
#if __name__ == '__main__':

for ii in range(LED_COUNT):
    BrightList.append(255)
    RList.append(0)
    GList.append(0)
    BList.append(0)

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
