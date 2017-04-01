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

server = OSCServer( ("0.0.0.0", 6666) )
server.timeout = 0.01
run = True

def handle_timeout(self):
    self.timed_out = True

server.handle_timeout = types.MethodType(handle_timeout, server)

def user_callback(path, tags, args, source):
    # which user will be determined by path:
    # we just throw away all slashes and join together what's left
    #user = ''.join(path.split("/"))
    # tags will contain 'fff'
    # args is a OSCMessage with data
    # source is where the message came from (in case you need to reply)
    global mid1,mid2,mid3,mid4,mid5,mid6,mid7
    global isplay
    print args[0]
    isplay = args[0]
    if 0 == args[0]:
       play_head() 
    elif 1 == args[0]:
       thread.start_new_thread(play_midi,(mid1,))
       time.sleep(1)
    elif 2 == args[0]:
       thread.start_new_thread(play_midi,(mid2,))
       time.sleep(1)
    elif 3 == args[0]:
       thread.start_new_thread(play_midi,(mid3,))
       time.sleep(1)
    elif 4 == args[0]:
       thread.start_new_thread(play_midi,(mid4,))
       time.sleep(1)
    elif 5 == args[0]:
       thread.start_new_thread(play_midi,(mid5,))
       time.sleep(1)
    elif False: #6 == args[0]:
       thread.start_new_thread(play_midi,(mid6,))
       time.sleep(1)
    elif False: #7 == args[0]:
       thread.start_new_thread(play_midi,(mid7,))
       time.sleep(1)
    elif -1 == args[0]:
       play_foot()
        
    #print ("Now do something with", user,args[2],args[0],1-args[1]) 

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

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
    return Color(int(RList[pos] * BrightList[pos] / 255), int(GList[pos] * BrightList[pos] / 255), int(BList[pos] * BrightList[pos] / 255))
    			
def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=10):
	"""Rainbow movie theater light style chaser animation."""
    while True:
	    for i in range(0, strip.numPixels()):
	        strip.setPixelColor(i, wheel(i))
            strip.show()
		time.sleep(wait_ms/1000.0)
	time.sleep(wait_ms/1000.0)


# Main program logic follows:
if __name__ == '__main__':

    for ii in range(32):
        BrightList.append(255)
        RList.append(0)
	GList.append(0)
	BList.append(0)
     
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')

server.addMsgHandler( "/cue", user_callback )
server.addMsgHandler( "/backLight", light_callback )
server.addMsgHandler( "/movie", movie_callback )

try:
    while run:
        # do the game stuff:
        #sleep(1)
        # call user script
        each_frame()


    server.close()

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
	
